def multipliction(a, b):
    multi = a * b
    return (multi)

def addition(*num):
    sum = 0
    for nums in num:
        
        sum += nums
        return sum


multipl = multipliction(12, 12)
summ = addition(12, 2, 3, 4, 5)

print("The sum multiplication is: ", multipl)
print("The sum of the tuple is : ", summ)
    