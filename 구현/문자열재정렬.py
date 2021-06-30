s = input()

sum_num = 0
arr = []
for i in range(len(s)):
    if s[i].isdigit():
        sum_num += int(s[i])
    else:
        arr.append(s[i])

arr.sort()
string = ''.join(arr)
print(string+str(sum_num))