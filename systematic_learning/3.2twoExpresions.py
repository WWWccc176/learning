age = 15
status = None
if (age > 12) and age < 20:
    status = "teenager"
else:
    status = "not teenager"
print(status)

status = "teenager" if age > 12 and age < 20 else "not teenager"
print(status)
