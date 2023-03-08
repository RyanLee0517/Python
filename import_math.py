"""
a = 10
b = 3
#Chia lấy thương /
print(a/b)
#Chia lấy nguyên //
print(a//b)
#Chia lấy dư %
print(a%b)
#Luỹ thừa với cơ số **
print(a**b)
"""
import math   # lấy nội dung của thư viện math về sử dụng

#Trả về số nguyên là phân nguyên của x toán tử math.trunc trả về số nguyên gần nhất luôn luôn <= x


print(math.trunc(3.9))


#Trả về số thực là giá trị tuyệt đối của x : |x|
print(math.fabs(-3))

#Trả về giá trị căn bậc 2 của x square root
print(math.sqrt(16))

#Trả về số nguyên là ước chung lớn nhất của x và y
print(math.gcd(6, 4))

#Trả về số nguyên là bội số chung nhỏ nhất của x và y
print(math.lcm(4, 5))

print(math.ceil(9.4))
print(math.floor(9.4))
