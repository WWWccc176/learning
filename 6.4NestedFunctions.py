import numpy as np

def my_dist_xyz(x, y, z):#三维点的距离

    def my_dist(x, y):#二维点的距离
        
        out = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
        return out
    
    d0 = my_dist(x, y)
    d1 = my_dist(x, z)
    d2 = my_dist(y, z)
    
    d=np.sqrt(d0**2+d1**2+d2**2)
    return np.array([d]).tolist()  # 转换为 Python 原生列表

print(my_dist_xyz([1,2],[3,5],[7,5]))
print(my_dist_xyz((1,2),(3,5),(7,5)))