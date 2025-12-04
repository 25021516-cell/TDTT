# Bài 1
print('Bài 1')

n_B1 = int(input('Nhập số nguyên n: '))

print('Số gấp đôi n là:', n_B1*2)

print('\n')

# Bài 2
print('Bài 2')

a_B2 = float(input('Nhập chiều rộng: '))
b_B2 = float(input('Nhập chiều dài: '))

while (a_B2 <= 0 or  b_B2 <= 0):
    if (a_B2 <= 0):
        print('Chiều rộng không hợp lệ')
        a_B2 = float(input('Nhập lại chiều rộng: '))
    elif (b_B2 <= 0):
        print('Chiều rộng không hợp lệ')
        b_B2 = float(input('Nhập lại chiều dài: '))    

if a_B2 > b_B2:
    c = a_B2
    a_B2 = b_B2
    b_B2 = a_B2

def S_Trong_Cay (a, b):
    S = a * b
    ST = ((a/2)**2)*3.14
    
    print('Diện tích trông cây là:', S - ST)

S_Trong_Cay(a_B2, b_B2)

print('\n')

