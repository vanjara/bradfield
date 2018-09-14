def reverseString(s):
    k = []
    for c in s:
        k.append(c)

    for i in range(len(k)):
        print k.pop()

reverseString("hello")