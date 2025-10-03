#3.5

a = [1,2,3,4,5]
b = a[-1:] + a[:len(a)-1]
print(b)

#3.6
a = [1,2,3,4,5,2,3,6,8,8]
count = 0 
for i in a:
    for j in a:
        if i == j:
            count+=1
    if count == 1:
        print(i, end=" ")
    count = 0

#3.7
a = [1,2,3,4,5,2,3,6,8,8,8]
count = 0
count_max = 0 
digit = 0
for i in a:
    for j in a:
        if i == j:
            count+=1
    if count > count_max:
        count = count_max
        digit = i
print(digit)

#3.8
arr = [5,4,8,9,6,7,16,1,15]
median_pos = len(arr) // 2

for num in arr:
    count_left = 0
    count_right = 0
    
    for other in arr:
        if other < num:
            count_left += 1
        elif other > num:
            count_right += 1
    
    if count_left == count_right:
        print(num)
        break
