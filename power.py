# power calculation without using epxonentaisl

multiplication_count = 0
# input is a, b output should be the result of a to the power b
# a is a non-zero positive integer
# b can be any positive integer including 0
def mypower(a, b):
    global multiplication_count
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        l = b % 2
        k = b // 2
        c = mypower(a,k)
        if l == 0:
            #c = mypower(a,k)
            multiplication_count += 1
            return (c * c)
        multiplication_count += 2
        #return (mypower(a, k) * mypower(a, k + 1))
        return (c * c * a)

# Sample run
#print mypower(5, 5)

# Testing
test_cases = [
    (3, 0, 1),
    (3, 5, 243),
    (2, 10, 1024),
    (3, 10, 59049),
]

for test_case in test_cases:
    a, b, expected = test_case
    print a, b, expected
    assert mypower(a, b) == expected
    print "It took %d multiplications to calculate mypower(%d, %d)" % (multiplication_count, a, b)

print ("All tests passed!")



# Simple power just multiples a by itself repeatedly.  It requires
# b - 1 multiplications to calculate simplepower(a, b).
multiplication_count = 0
def simple_power(a, b):
    global multiplication_count
    if b == 0:
        return 1
    result = a
    for i in range(1, b):
        multiplication_count += 1
        result *= a
    return result

for test_case in test_cases:
    a, b, expected = test_case
    print a, b, expected
    assert simple_power(a, b) == expected
    print "It took %d multiplications to calculate simple_power(%d, %d)" % (multiplication_count, a, b)

print ("All tests passed!")

assert simple_power(3, 0) == 1
assert simple_power(3, 5) == 243
assert simple_power(2, 10) == 1024
assert simple_power(3, 10) == 59049

