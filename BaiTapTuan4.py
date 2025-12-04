#W4A1
print('W4A1')

sum_W4A1 = 0
n_W4A1 = 0

while n_W4A1 <= 1000:
    sum_W4A1 += n_W4A1
    n_W4A1 +=1
    
print(sum_W4A1)

#W4A2
print('W4A2')

n_W4A2 = int(input('Nhập số nguyên dương: '))

while n_W4A2 <= 0:
    print(f'{n_W4A2} không phải số nguyên dương')
    n_W4A2 = int(input('Nhập số nguyên dương: '))
    
a_4A2 = True

if n_W4A2 < 2:
    print(f'{n_W4A2} không phải số nguyên tố')
    a_4A2 = False
else:
    for i in range(2, n_W4A2):
        if n_W4A2 % (i) == 0:
            print(f'{n_W4A2} không phải số nguyên tố')
            a_4A2 = False
            break

if a_4A2:
    print(f'{n_W4A2} là số nguyên tố')
    
#W4A3
print('W4A3')

n_W4A3 = int(input('Nhập số nguyên dương: '))

while n_W4A3 <= 0 or n_W4A3 >= 100:
    print(f'{n_W4A3} không phải số cần lấy')
    n_W4A3 = int(input('Nhập lại: '))
    
Giai_Thua_W4A3 = 1
    
for i in range(1, n_W4A3 + 1):
    Giai_Thua_W4A3 *= i
    
print(Giai_Thua_W4A3)

#W4A4
print('W4A4')

n_W4A4 = int(input('Nhập số nguyên n: '))
from math import*
n_W4A4 = abs(n_W4A4)

count_W4A4 = 0

if n_W4A4 == 0:
    count_W4A4 = 1
else:
    while n_W4A4 > 0:
        count_W4A4 += 1
        n_W4A4 //= 10
    
print(count_W4A4)

#W4A5
print('W4A5')

n_W4A5 = int(input('Nhập số nguyên dương: '))
range_W4A5 = map(int, input('Nhập dãy số có n phần tử: ').split())

lst_W4A5 = list(range_W4A5)
a_W4A5 = True

for i in range(len(lst_W4A5)):
    if lst_W4A5[i] == 42:
        print("I've found the meaning of life")
        a_W4A5 = False
        break
    
if a_W4A5:
    print("It's a joke")

#W4A6
print('W4A6')

a_W4A6 = int(input('Nhập số nguyên dương a: '))
b_W4A6 = int(input('Nhập số nguyên dương b: '))

if a_W4A6 > b_W4A6:
    a_W4A6 = a_W4A6 ^ b_W4A6
    b_W4A6 = a_W4A6 ^ b_W4A6
    a_W4A6 = a_W4A6 ^ b_W4A6
    
summ__W4A6 = 0

for i in range(a_W4A6, b_W4A6 + 1):
    if i < 2:
        continue
    else:
        bool__W4A6 = True
        for j in range(2, i):
            if(i % j == 0):
                bool__W4A6 = False
                
        if bool__W4A6:
            summ__W4A6 += i
                
print(summ__W4A6)