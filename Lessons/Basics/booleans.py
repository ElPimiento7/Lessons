"""
 True(1) and False(0)
"""

falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), ""]
for e in falsy:
    print(bool(e))
print("-----------------------")

print(bool(1))
print(bool("zsfddhgjjf"))
print(bool([]))
print(bool(None))
print("-----------------------")


def check(x) -> bool:
    print(f"{x}>0 is {bool(x > 0)}")
    return x > 0


if check(1) and check(-2) and check(3) and check(4):
    print("YES")
