# Debugging exercise Aug 2022 - Used a lot of help to get this though
# Original code
'''
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)               # Formula sould be mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1                         # should be ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1                    # should be ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
'''
# My debugging
def findZigZagSequence(a, n):
    a.sort()
    mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# Testing
'''
test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
'''
#a1 = [2,3,5,1,4]
a = [1,2,3,4,5,6,7]
aseq = findZigZagSequence(a,7)
