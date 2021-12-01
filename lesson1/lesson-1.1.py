duration = int(input("введите число которое хотите преобразовать в секундны, минуты, дни:"))
day = duration // 86400
data_hourse = duration % 86400
data_minets = data_hourse % 3600
hour = data_hourse // 3600
minets = data_minets // 60
seconds = data_minets % 60

print(day, "день",hour,"час",minets,"минут",seconds,"секунд")
