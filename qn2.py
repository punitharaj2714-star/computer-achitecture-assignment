
def to_binary(n):
    return format(n & 0xFF, '08b')

def signed_value(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value

def addition(a, b):
    result = (a + b) & 0xFF
    overflow = (a >= 0 and b >= 0 and result >= 128) or \
               (a < 0 and b < 0 and result < 128)
    return result, overflow

def subtraction(a, b):
    return addition(a, -b)

# Expression (a): 34 + (+27)
a, b = 34, 27

print("Expression (a): 34 + (+27)")
print("Operand 1:", to_binary(a))
print("Operand 2:", to_binary(b))

result, overflow = addition(a, b)

print("Result:", format(result, '08b'))
print("Decimal Result:", signed_value(format(result, '08b')))
print("Overflow:", overflow)

print()

# Expression (b): (-34) - (-27)
a, b = -34, -27

print("Expression (b): (-34) - (-27)")
print("Operand 1:", to_binary(a))
print("Operand 2:", to_binary(b))

result, overflow = subtraction(a, b)

print("Result:", format(result, '08b'))
print("Decimal Result:", signed_value(format(result, '08b')))
print("Overflow:", overflow)
