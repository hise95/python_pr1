#1
var_int = 10
var_float = 8.4
var_str = "No"

#2
big_int = var_int * 3.5

#3
var_float -= 1

#4
var_int_div_var_float = var_int / var_float
big_int_div_var_float = big_int / var_float

#5

var_str = "No" * 2 + "Yes" * 3

#6

a1 = int(input("Введіть а1: "))
a2 = int(input("Введіть а2: "))
b1 = int(input("Введіть b1: "))
b2 = int(input("Введіть b2: "))
m = int(input("Введіть m: "))

C = ((a1*b1) - (a2*b2)) / (m*a1-(a2**2))

print("Результат: ", C)
