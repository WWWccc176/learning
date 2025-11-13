import numpy as np


def my_trig_sum(a, b):
    """
    function to demo return multiple
    author
    date
    """
    out1 = np.sin(a) + np.cos(b)
    out2 = np.sin(b) + np.cos(a)
    return out1, out2, [out1, out2]


c, d, e = my_trig_sum(2, 3)
print(f"c ={c}, d={d}, e={e}")
help(my_trig_sum)

