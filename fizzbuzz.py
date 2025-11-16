ubound = 100
diviser = [3, 5]


def n_multiple(bound, num):

    results = []
    for i in num:
        if not isinstance(i, int) or i < 2:
            print(f"Element should be a integer larger than '2'.")
            return []

    for j in range(1, bound + 1):
        
        output = ""
        
        if j % num[0] == 0:
            output += "fizz"
            
        if j % num[1] == 0:
            output += "buzz"
        
        results.append(j if output == "" else output)
        
    return results

result = n_multiple(ubound, diviser)
print("full result list: ")
for item in result:
    print(item)

