int_list = []
for n in range(1, 101): 
    if (n + 10) % 17 == 0 and (n + 5) % 12 == 0:
        int_list.append(n)

if int_list:
    print(min(int_list))
else:
    print("No se encontró ningún valor de n en el rango dado.")
