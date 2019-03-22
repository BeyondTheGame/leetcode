def recurTest(test, res):
    test += [5, 6]
    res += 1
    # recurTest(test, res)

test = [2, 3, 4]
res = 0
recurTest(test, res)
print(res)
print(test)