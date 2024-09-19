number_list = []
a = int(input("numero a: "))
number_list.append(a)
b = int(input("numero b: "))
number_list.append(b)
c = int(input("numero c: "))
number_list.append(c)



for i in range(1, min(number_list)):
    divisor_list = []
    if (a-b) % i == 0 and (a-c) % i == 0:
        divisor_list.append(i)
    print(max(divisor_list))
