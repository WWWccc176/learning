# 方key圆value
schoolDict = {}
schoolDict["TsingHua University"] = "CN"
schoolDict["Oxford"] = "UK"  # 1.直接加就好 2.若重复添加同一个键，原值会被覆盖。

print(schoolDict)
print("UC Berkeley" in schoolDict)

newDict = dict([("UC Berkeley", "USA"), ("Liverpool", "UK")])  # 将Tuple转化为Dictionary

schoolDict.update(newDict)  # 直接使用即可，不要使用赋值
print(schoolDict)

print("UC Berkeley" in schoolDict)
