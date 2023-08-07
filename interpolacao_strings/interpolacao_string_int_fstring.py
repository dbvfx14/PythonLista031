num1 = 6
num2 = 382

# simboliza-se a formatação int com :d (de dígito)
print("num1: {:d}".format(num1)) # apenas int.

print("num1: {:7d} ".format (num1)) # int com 7 digitos.
print("num2: {:7d}".format (num2))

print("num1: {:670}" .format (num1)) # int 7 dígitos, preenchendo com zeros.
print("num2: {:67d}" .format (num2))