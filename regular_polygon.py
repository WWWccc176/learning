import mpmath

mpmath.mp.dps = 50

s_str = input("Enter the length of each side:")
n_str = input("Enter the number of sides of your polygon:")


def calculate_area(leng_str, num_str):

    leng = mpmath.mpf(leng_str)
    num = mpmath.mpf(num_str)

    area = (num * leng**2) / (4 * mpmath.tan(mpmath.pi / num))
    PPi = area / (leng / (2 * mpmath.sin(mpmath.pi / num))) ** 2

    return area, PPi


area_result, ppi_result = calculate_area(s_str, n_str)


print(f"The area of the polygon is: {area_result}")
print(f"The calculated 'Pi' value is: {ppi_result}")
