num1 = 6
num2 = 382

# simboliza-se a formatação int com :d (de dígito)
print(f"num1: {num1:d}".format) # apenas int.

print(f"num1: {num1:7d} ".format) # int com 7 digitos.
print(f"num2: {num1:7d}".format)

print("num1: {:670}" .format (num1)) # int 7 dígitos, preenchendo com zeros.
print("num2: {:67d}" .format (num2))
