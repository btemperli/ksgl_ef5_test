values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
hexnumber = []
y = int(input("please insert a decimal-number."))

while y > 0:
    rest = y % 16
    y = y // 16
    hexnumber.append(values[rest])
    
hexnumber.reverse()

print(hexnumber)
print(''.join(str(x) for x in hexnumber))
