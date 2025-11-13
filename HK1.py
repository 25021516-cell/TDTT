#Biểu thức, Toán tử, Nhập xuất dữ lịệu
#W2A1
print('W2A1 \n')

print('Hello World')
print('\n')

#W2A2
print('W2A2 \n')
Ten_Nguoi = str(input('Nhập tên của bạn: '))
print('Xin chào', Ten_Nguoi)
print('\n')

#W2A3
print('W2A3 \n')
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
print('Tổng của a và b là:', a + b)
print('Hiệu của a và b là:', a - b)
print('Tích của a và b là:', a * b)
print('Phần nguyên cùa a chia b là:', a // b)
print('Phần dư của a chia b là:', a % b)
print('Phần thực của a chia b là:', a / b)
print('\n')

#W2A4
print('W2A4 \n')

a1, b1, c1, a2, b2, a3 = map(int, input('Nhập điểm: ').split())

Diem_TB = (a1 + b1 + c1 + a2*2 + b2*2 + a3*3)/10

print('Điểm trung bình cả môn là:', round(Diem_TB, 1))
print('\n')

#W2A5
print('W2A5 \n')

A, B = map(int, input('Nhập hai số a và b: ').split())

print('Kết quả:', A**B)
print('\n')

#W2A6
print('W2A6 \n')

Word = input()
print(ord(Word))
print(Word.upper())
print('\n')

#W2A7
print('W2A7 \n')

print('A = ', ((13**2)*3) + 5)
print('B = ', 13**2*3 + 5)
print('\n')

#W2A8
print('W2A8 \n')

Do_C = float(input('Nhập nhiệt độ Celcius: '))
Do_F = 9/5*Do_C + 32

print('Nhiệt độ Fabrenhein tương ứng là:',round(Do_F, 2))
print('\n')

#W2A9
print('W2A9 \n')

Watch_Price = float(input('Nhập giá đồng hồ: '))
Real_Price = Watch_Price*1.4 + 10

print('Cái giá phải trả là:',round(Real_Price, 2))
print('\n')

#W2A10
print('W2A10 \n')

Name_1, Name_2, Name_3 = map(str,input('Nhập tên 3 người: ').split())

print('Hi', Name_3 + ',', Name_2 + ',', Name_1)
print('\n')

#W2A11
print('W2A11 \n')

Hours = int(input('Nhập số giờ: '))
Minutes = int(input('Nhập số phút: '))

Seconds = Hours*(60**2) + Minutes*60

print('Số giây là:', Seconds)
print('\n') 

#W2A12
print('W2A12 \n')

n = int(input('Nhập độ dài cạnh rubik: '))

print('Số miếng dán cần là:', n*n*6)
print('\n')

#W2A13
print('W2A13 \n')

So_a = int(input('Nhập số a: '))
So_b = int(input('Nhập số b: '))

print('Hàng đơn vị số tích của a và b là:', (So_a*So_b)%10)
print('\n')

#W2A14
print('W2A14 \n')

So_A = int(input('Nhập số a: '))
So_B = int(input('Nhập số b: '))

So_A = So_A + So_B
So_B = So_A - So_B
So_A = So_A - So_B

print(So_A, So_B)
print('\n')

#W2A15
print('W2A15 \n')

N = int(input('Nhập số n: '))

Star_N = 6 * N * (N - 1) + 1

print('Số sao là:',Star_N)
print('\n')

#W2A16
print('W2A16 \n')

print('Spring \nSummer \nAutumn \nWinter')
print('\n')

#W2A17
print('W2A17 \n')

print('''  * \n *** \n***** ''')
print('\n')

#W2A18
print('W2A18 \n')

print('### ##   ### ###')
print(' #  # #   #   #')
print(' #  #  #  #   #')
print(' #  # #   #   #')
print(' #  ##    #   #')

print('### ##   ### ### \n #  # #   #   # \n #  #  #  #   # \n #  # #   #   # \n #  ##    #   #')
print('\n')

#W2A19
print('W2A19 \n')

print('Monday \nTuesday \nWednesday \nThursday \nFriday \nSaturday \nSunday')
print('\n')

#W2A20
print('W2A1920 \n')

print('January \nFebruary \nMarch \nApril \nMay \nJune \nJuly \nAugust \nSeptember \nOctober \nNovember \nDecember')
print('\n')

#W2A21
print('W2A21 \n')

for i in range(10):
    print('Hello World')

print('\n')