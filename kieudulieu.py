#import tất cả từ thư viên decimal (số thập phân)
from decimal import*
#Câu lệnh nâng cao lấy số chữ số sau dấu thập phân
getcontext().prec = 5

print(type(Decimal(10)/Decimal(3)))

