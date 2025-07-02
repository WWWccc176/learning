import cupy as cp
import matplotlib.pyplot as plt
import os  # 新增：用于构造桌面路径

# ---- 1. 全局常量 & 预分配向量 ----
DTYPE = cp.float32

_u200 = cp.arange(1, 201, dtype=DTYPE)[:, None, None]
_s70 = cp.arange(1, 71, dtype=DTYPE)[:, None, None]
_r50 = cp.arange(1, 51, dtype=DTYPE)[:, None, None]


# ---- 2. 工具函数 Cs, Cp ----
def Cs(X):
    return cp.sum(X, axis=0)


def Cp(X):
    return cp.prod(X, axis=0)


# ---- 3. 子函数（与之前完全一致） ----
def L(x, y):
    u = _u200
    A = (
        (2 + u**5 / 30) * (cp.cos(4 * u**2) * x / 4 + cp.sin(4 * u**2) * y / 4)
        + u**2
        + u**4
    )
    B = (
        (2 + u ** (6 / 5) / 30) * (cp.sin(4 * u**2) * x / 4 - cp.cos(4 * u**2) * y / 4)
        + u**2
        + u**4
    )
    inner = cp.cos(A) ** 10 * cp.cos(B) ** 10 - 1 + 3 / 200 * u ** (-23 / 20)
    return cp.sum(2 * cp.exp(-cp.exp(-70 * inner)), axis=0)


def Q(x, y):
    return 0.3 * x + 0.15 * y


def P_(x, y):
    return y - 0.5 * x


def E(x, y):
    a = Q(x, y)
    b = P_(x, y)
    c = 0.5 + (1 / cp.pi) * cp.arctan(-10000 * b)
    inner = cp.sqrt((10 / 3 - (7 / 3) * c) ** 2 * a**2 + b**2)
    expo = -(20 + 40 * c) * (inner - 1.5 + (21 / 20) * c)
    return cp.sqrt(a**2 + b**2) * cp.exp(-cp.exp(expo))


def J(x, y, r):
    a = Q(x, y)
    b = P_(x, y)
    e = E(x, y)
    theta = cp.pi * r / 4 - 4.5 * cp.log(e)
    t1 = (a - e * cp.cos(theta)) ** 2 + (b - e * cp.sin(theta)) ** 2
    t2 = 10 * (e - 1.3 * cp.abs(cp.cos(r**4)) - 0.2) ** 2 - 2
    return cp.exp(-7 * t1 - cp.exp(t2))


def K(x, y):
    s = _s70
    A1 = (5 + s / 6) * (cp.cos(s**2) * x + cp.sin(s**2) * y) + 10 * cp.sin(10 * s)
    B1 = (5 + s / 6) * (cp.sin(s**2) * x - cp.cos(s**2) * y) + 10 * cp.sin(17 * s)
    inner = cp.cos(A1) ** 10 * cp.cos(B1) ** 10 - 0.5
    return cp.sum((4 / 25) * cp.exp(-cp.exp(-100 * inner)), axis=0)


def W(x, y):
    t = x + y / 2 + 3 / 50 * cp.cos(10 * (y - x / 2) + 3 * cp.cos(7 * (y - x / 2)))
    return cp.exp(
        -cp.exp(20 * (cp.abs(t) - 0.03 - 0.012 * (y - x / 2) ** 2))
        - cp.exp(1000 * (y - x / 2))
    )


def R_sub(x, y):
    t = x + y / 2 + 3 / 50 * cp.cos(10 * (y - x / 2) + 3 * cp.cos(7 * (y - x / 2)))
    return cp.exp(
        -cp.exp(20 * (cp.abs(t) - 0.03 - 0.012 * (y - x / 2) ** 2))
        - cp.exp(-1000 * (y - x / 2 - 1.5))
    )


def H(x, y, v):
    Rv = R_sub(x, y)
    Wv = W(x, y)
    Kv = K(x, y)
    Lv = L(x, y)
    J_all = J(x, y, _r50)
    A_sub = cp.sum(cp.cos(7 * _r50) ** 2 * J_all, axis=0)
    Cp1mJ = cp.prod(1 - J_all, axis=0)

    c1 = (3 * v * v - 5 * v + 7) / 4
    c2 = (2 - v) / 2
    c3 = (23 * v * v - 38 * v + 55) / 20
    c4a = c1
    c4b = (14 + 3 * v * v - 3 * v) / 20
    c5 = (25 - 12 * v + 2 * v * v) / 6

    G1 = -20 * ((x - 1.7) ** 2 + (y - 0.4) ** 2 - 0.03)
    G2 = -20 * ((x + 2.5) ** 2 + (y + 0.8) ** 2 - 0.02)
    T2 = cp.exp(-cp.exp(G1) - cp.exp(G2))

    G3 = 15 * ((x - 1.7) ** 2 + (y - 0.4) ** 2) - 0.45
    G4 = -2 * (0.3 * x + 0.15 * y) ** 2 - 1.8 * (y - x / 2) ** 2 + 6.4
    T4 = cp.exp(-cp.exp(G4))
    G5 = 20 * (((x + 2.5) ** 2 + (y + 0.8) ** 2) - 0.02)

    term1 = c1 * Rv * Kv
    term2 = c2 * A_sub * Kv * (1 - Rv) * T2
    term3 = c3 * cp.exp(-cp.exp(G3))
    term4 = (c4a * Wv * Kv + c4b * Lv * (1 - Wv) * (1 - Rv)) * Cp1mJ * T4
    term5 = c5 * cp.exp(-cp.exp(G5))

    return term1 + term2 + term3 + term4 + term5


def F(x):
    return cp.floor(
        255 * cp.exp(-cp.exp(-1000 * x)) * cp.abs(x) ** cp.exp(-cp.exp(1000 * (x - 1)))
    )


# ---- 4. 主程序：分块 + 坐标映射 (m,n)->(x,y) ----
def main():
    # 像素坐标 m,n
    x_pix = cp.arange(1, 2000 + 1e-6, 0.1, dtype=DTYPE)
    y_pix = cp.arange(1, 1200 + 1e-6, 0.1, dtype=DTYPE)
    Ny, Nx = y_pix.size, x_pix.size

    # 最终 RGB 图像 （GPU 上 uint8）
    img_gpu = cp.empty((Ny, Nx, 3), dtype=cp.uint8)

    block_y = 50  # 每次处理 50 行
    for y0 in range(0, Ny, block_y):
        y1 = min(Ny, y0 + block_y)
        y_block = y_pix[y0:y1]
        m, n = cp.meshgrid(x_pix, y_block)

        # 坐标映射
        x_norm = (m - 1000.0) / 160.0
        y_norm = (601.0 - n) / 160.0

        for c_idx, v in enumerate((0.0, 1.0, 2.0)):
            Hval = H(x_norm, y_norm, DTYPE(v))
            Fval = F(Hval).astype(cp.uint8)
            img_gpu[y0:y1, :, c_idx] = Fval

        print(f"Processed rows {y0} – {y1}")

    # 拷回 CPU
    img = cp.asnumpy(img_gpu)

    # —— 新增：自动保存到桌面 ——
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    # 如果你的系统桌面文件夹不是 Desktop，请自行改成中文“桌面”或完整路径
    save_path = os.path.join(desktop, "raw_image.png")
    # 使用 matplotlib 直接保存原始像素阵列
    plt.imsave(save_path, img)
    print(f"已将最原始（最清晰）图片保存到：{save_path}")

    # —— 保留原来显示部分 ——
    plt.figure(figsize=(10, 6))
    plt.imshow(img)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
