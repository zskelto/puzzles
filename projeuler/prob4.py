'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers
'''

def isPalin(num):
    org = str(num)
    rev = ""
    for i in range(len(org)-1,-1,-1):
        rev+=org[i]
    if rev==org:
        return True
    else:
        return False

def prob4():
    ans = []
    for i in range(999, 99, -1):
        for j in range(i,99,-1):
            if(isPalin(i*j)):
                ans.append(i*j)
    return max(ans)

print(prob4())
