# power calculation without using epxonentaisl

# input is a, b output should be the result of a to the power b
# a is a non-zero positive integer
# b can be any positive integer including 0
def mypower(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    else:
        l = b % 2
        k = b//2
        if l == 0:
            return (mypower(a, k) * mypower(a, k))
        return (mypower(a, k) * mypower(a, k+1))

# Sample run
print mypower(5, 5)

# Testing
test_cases = [
    (3, 0, 1),
    (3, 5, 243),
    (2, 10, 1024)
]

for test_case in test_cases:
    a, b, expected = test_case
    print a, b, expected
    assert mypower(a, b) == expected

print ("All tests passed!")