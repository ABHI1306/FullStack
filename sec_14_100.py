def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))

def stringBits(str):
    return str[::2]
print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

def end_other(a,b):
    a = a.lower()
    b = b.lower()
    #return(b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or a == b[-len(a):]
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiabC'))
print(end_other('abc', 'abXabc'))

def dubleChar(myString):
    res = ''
    for i in myString:
        res += i*2
    return res
print(dubleChar("The"))
print(dubleChar('AAbb'))
print(dubleChar('Hi-There'))

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n in [13,14,16,17,18,19]:
        return 0
    return n
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count
print(count_evens([2,1,2,3,4]))
print(count_evens([2,2,0]))
print(count_evens([1,3,5]))
