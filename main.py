# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
j = input().split()

lst = [int(i) for i in j]

c = Counter(lst)

for i in c:
    key = i
    value = c[i]
    if value == 1:
        print(key)
