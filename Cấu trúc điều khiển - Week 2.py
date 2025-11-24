# Bài 1
print('Bài 1')

Chieu_Dai = float(input('Nhập chiều dài: '))
Chieu_Rong = float(input('Nhập chiều rộng: '))

Chu_Vi_HCN = (Chieu_Dai + Chieu_Rong)*2
Dien_Tich_HCN = (Chieu_Dai*Chieu_Rong)

print('Chu vi hình chữ nhật là:', Chu_Vi_HCN)
print('Diện tích hình chữ nhật là:', Dien_Tich_HCN)

print('\n')

# Bài 2
print('Bài 2')

from math import*
Ban_Kinh = float(input('Nhập bán kính hình tròn: '))

Chu_Vi_HT = Ban_Kinh*2*3.14
Dien_Tich_HT = (Ban_Kinh**2)*3.14

print('Chu vi hình tròn là:', Chu_Vi_HT)
print('Diện tích hnhf tròn là:', Dien_Tich_HT)

print('\n')

# Bài 3
print('Bài 3')

Canh_Thu_Nhat = float(input('Nhập cạnh thứ nhất của tam giác: '))
Canh_Thu_Hai = float(input('Nhập cạnh thứ hai của tam giác: '))
Canh_Thu_Ba = float(input('Nhập cạnh thứ ba của tam giác: '))

Chu_Vi_TG = Canh_Thu_Hai + Canh_Thu_Ba + Canh_Thu_Nhat

Nua_Chu_Vi_TG = (Canh_Thu_Hai + Canh_Thu_Ba + Canh_Thu_Nhat)/2

Dien_Tich_TG = sqrt(Nua_Chu_Vi_TG*(Nua_Chu_Vi_TG - Canh_Thu_Nhat)*(Nua_Chu_Vi_TG - Canh_Thu_Hai)*(Nua_Chu_Vi_TG - Canh_Thu_Ba))

if (Canh_Thu_Nhat + Canh_Thu_Hai <= Canh_Thu_Ba) | (Canh_Thu_Nhat + Canh_Thu_Ba <= Canh_Thu_Hai) | (Canh_Thu_Ba + Canh_Thu_Hai <= Canh_Thu_Nhat):
    print('Đây không phải ba cạnh của tam giác.')

else:
    if (Canh_Thu_Nhat == Canh_Thu_Hai == Canh_Thu_Ba):
        print('Đây là tam giác đều')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)

    elif (Canh_Thu_Ba == Canh_Thu_Hai) | (Canh_Thu_Ba == Canh_Thu_Nhat) | (Canh_Thu_Nhat == Canh_Thu_Hai):
        print('Đây là tam giác cân')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)
    elif (((Canh_Thu_Nhat*Canh_Thu_Hai)/2) == Dien_Tich_TG) | (((Canh_Thu_Nhat*Canh_Thu_Ba)/2) == Dien_Tich_TG) | (((Canh_Thu_Ba*Canh_Thu_Hai)/2) == Dien_Tich_TG):
        print('Đây là tam giác vuông')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)
    else:
        print('Đây là tam giác thường')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)

print('\n')

