# ⚠️ Two pointer

list = [int(input()) for i in range(5)]
target = int(input("Enter target value (a + b = )"))
l = 0
r = len(list) - 1

while l < r :
    if list[l] + list[r] == target:
        print(l, r)
        break
    elif list[l] + list[r] < target:
        l += 1 
    elif list[l] + list[r] > target:
        r -= 1 
    
else:
    print("No combination found..")


'''for _ in range(len(list)): #Using For loop
    if list[l] + list[r] == target:
        print(l, r)
        break
    elif list[l] + list[r] < target: 
        l += 1'''
    


# ⚠️ Two pointer palindrome

def palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r :
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
print(palindrome('abaca'))