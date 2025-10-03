# 注意：这段代码生成的迷宫的出口和入口都在边界上
import numpy as np
import cupy as cp
import matplotlib.pyplot as plt


def generate_maze_wilson(H, W, showMap=True):
    """
    在 CPU 上用 Wilson 算法生成 H×W 迷宫，并且如果 showMap=True,
    实时用 matplotlib.imshow() 做动画。返回四面墙矩阵 U,D,L,R，
    入口 start，出口 exit_pos，以及最终的栅格图 grid（0=通道，1=墙）。
    """
    # 1) 迷宫访问标记（True=未访问），入口(0,0)置为已访问
    mazeMat = np.ones((H, W), dtype=bool)
    start = (0, 0)
    mazeMat[start] = False

    # 2) 四面墙矩阵，True=该边有墙
    U = np.ones((H, W), dtype=bool)
    D = np.ones((H, W), dtype=bool)
    L = np.ones((H, W), dtype=bool)
    R = np.ones((H, W), dtype=bool)

    # 3) 用一张“栅格图”来做动画：图像大小 (2H+1)×(2W+1)
    #    交替排列：奇数行奇数列是通道，其它位置为墙
    grid = np.ones((2 * H + 1, 2 * W + 1), dtype=np.uint8)
    grid[1::2, 1::2] = 0
    # 打开入口(1,0)
    grid[1, 0] = 0

    # 固定出口为 (H-1,W-2) 右边界口
    exit_pos = (H - 1, W - 2)
    # 对应像素坐标 (2*exit_y+1, 2*exit_x+2)
    grid[2 * exit_pos[0] + 1, 2 * exit_pos[1] + 2] = 0

    update_every = 50  # 每走 50 步更新一次画面
    step = 0

    # 如果要动画，就用 plt.ion() + imshow
    if showMap:
        plt.ion()
        fig, ax = plt.subplots(figsize=(6, 6))
        im = ax.imshow(grid, cmap="binary", interpolation="nearest")
        ax.set_axis_off()
        plt.show()

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
    unvisited = H * W - 1

    # 主循环：还有未访问的格子就继续
    while unvisited > 0:
        # 随机在 mazeMat==True（未访问）中选一点做游走起点
        ys, xs = np.nonzero(mazeMat)
        idx = np.random.randint(len(ys))
        path = [(ys[idx], xs[idx])]
        pr, pc = path[0]

        # Loop‐Erased Random Walk
        while mazeMat[pr, pc]:
            dy, dx = dirs[np.random.randint(4)]
            r2, c2 = pr + dy, pc + dx
            # 边界检查
            if r2 < 0 or r2 >= H or c2 < 0 or c2 >= W:
                continue
            # 如果新格在 path 里，删环
            if (r2, c2) in path:
                loop_idx = path.index((r2, c2))
                path = path[:loop_idx]
            path.append((r2, c2))
            pr, pc = r2, c2

        # 把 path 上的每条边都打通并更新栅格图
        for (r1, c1), (r2, c2) in zip(path, path[1:]):
            if r2 == r1 - 1 and c2 == c1:  # 上
                U[r1, c1] = False
                D[r2, c2] = False
                grid[2 * r1, 2 * c1 + 1] = 0
            elif r2 == r1 + 1 and c2 == c1:  # 下
                D[r1, c1] = False
                U[r2, c2] = False
                grid[2 * r1 + 2, 2 * c1 + 1] = 0
            elif r2 == r1 and c2 == c1 - 1:  # 左
                L[r1, c1] = False
                R[r2, c2] = False
                grid[2 * r1 + 1, 2 * c1] = 0
            elif r2 == r1 and c2 == c1 + 1:  # 右
                R[r1, c1] = False
                L[r2, c2] = False
                grid[2 * r1 + 1, 2 * c1 + 2] = 0

            # 标记访问
            if mazeMat[r1, c1]:
                mazeMat[r1, c1] = False
                unvisited -= 1
            if mazeMat[r2, c2]:
                mazeMat[r2, c2] = False
                unvisited -= 1

        # 动画更新
        step += 1
        if showMap and (step % update_every == 0 or unvisited == 0):
            im.set_data(grid)
            plt.pause(0.001)

    # 生成完毕，关闭交互模式（但保留窗口）
    if showMap:
        plt.ioff()
        plt.draw()

    return U, D, L, R, start, exit_pos, grid


def bfs_gpu(U, D, L, R, start, exit_pos):
    """
    在 GPU 上用“波次扩散”做 BFS，计算从 start 到每个点的最短距离，
    未到达点距离保持为 -1。返回一个 cupy 数组 dist。
    """
    H, W = U.shape
    # 拷贝到 GPU
    Uc = cp.array(U)
    Dc = cp.array(D)
    Lc = cp.array(L)
    Rc = cp.array(R)

    dist = cp.full((H, W), -1, dtype=cp.int32)
    sy, sx = start
    ey, ex = exit_pos
    dist[sy, sx] = 0
    frontier = cp.zeros((H, W), dtype=bool)
    frontier[sy, sx] = True
    wave = 0

    while True:
        # 四个方向扩散
        # 下方：frontier 且没有下墙 -> 下移一格
        m = frontier & (~Dc)
        down = cp.roll(m, 1, axis=0)
        down[0, :] = False
        # 上方
        m = frontier & (~Uc)
        up = cp.roll(m, -1, axis=0)
        up[-1, :] = False
        # 右方
        m = frontier & (~Rc)
        right = cp.roll(m, 1, axis=1)
        right[:, 0] = False
        # 左方
        m = frontier & (~Lc)
        left = cp.roll(m, -1, axis=1)
        left[:, -1] = False

        newf = (down | up | right | left) & (dist == -1)
        if not newf.any():
            break
        wave += 1
        dist[newf] = wave
        frontier = newf

    return dist


def main():
    H, W = 300, 300

    # 1) 迷宫生成 + 动画
    U, D, L, R, start, exit_pos, grid = generate_maze_wilson(H, W, showMap=True)

    # 2) GPU 上做 BFS（不动画，直接计算最短路）
    dist_gpu = bfs_gpu(U, D, L, R, start, exit_pos)

    # 3) 把距离搬回 CPU 并叠加到迷宫图上，生成最终效果
    dist = cp.asnumpy(dist_gpu)

    fig, ax = plt.subplots(figsize=(6, 6))
    # 先画迷宫的黑白栅格
    ax.imshow(
        grid,
        cmap="binary",
        interpolation="nearest",
        origin="upper",
        extent=[0, 2 * W + 1, 2 * H + 1, 0],
    )  # 注意上下左右的坐标区间

    # 画热度图，并让它也拉伸到同样的范围
    im2 = ax.imshow(
        dist,
        cmap="pink",
        alpha=0.7,
        interpolation="nearest",
        origin="upper",
        extent=[0, 2 * W + 1, 2 * H + 1, 0],
    )
    # 标记入口(绿)和出口(红)
    sy, sx = start
    ey, ex = exit_pos
    ax.plot(2 * sx + 1, 2 * sy + 1, "go")  # 注意：imshow 的 x 对应列 index
    ax.plot(2 * ex + 1, 2 * ey + 1, "r*")
    ax.set_axis_off()
    plt.colorbar(im2, ax=ax, label="Distance from start")
    plt.title(f"Maze {H}×{W} + BFS distance")
    plt.show()


if __name__ == "__main__":
    main()
