#Chuỗi trần vô hiệu hoá các escape squence

print("con ca\n to cha ba")
print()
print(r"con ca\n to cha ba")

#Cộng (nối) chuỗi (str)

strA = "aduma"
strB = "VTEC"
strC = strA + strB
print(strC)

strA = "aduma"
strB = "VTEC"
strC = strA +'\n'+ strB
print(strC)

strC = strA *5
print(strC)

strC = strB in strA
print(strC)