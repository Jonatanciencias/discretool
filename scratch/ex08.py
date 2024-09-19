import math

int_list = []
for n in range(1, 10000):
    if math.lcm(n, 21) == 105 and math.lcm(n, 35) == 35:
        int_list.append(n)

if int_list:
    print(f"Lista: {int_list}")
else:
    print("no existe un n")
    
    