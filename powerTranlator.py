def power_estimator(num,base):
    cout = 1
    n0 = num

    while n0 / base >= base:
        n0 = n0 / base
        cout += 1
    return cout


bigInteger=int(input("Type in your large_number:"))
estimator=int(input("Type in your base:"))
power=power_estimator(bigInteger,estimator)
print(f"the number lies between {estimator}^{power-1} and {estimator}^{power}")
