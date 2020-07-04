# Write your code here
alpha = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
j = 0
for i in range(len(alpha)):
    j = j + 1
    dic[alpha[i]] = j
s = input()
i = 0   
for u in s:
    i = dic[u] + i
print(i)
