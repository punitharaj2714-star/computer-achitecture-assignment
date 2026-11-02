
def rotate_left_without_carry(binary, positions):
    print("\nRotate Left Without Carry (ROL)")
    print("Original number:", binary)

    for i in range(positions):
        binary = binary[1:] + binary[0]
        print("After rotation", i + 1, ":", binary)

    return binary


def rotate_left_with_carry(binary, carry, positions):
    print("\nRotate Left With Carry (RCL)")
    print("Original number:", binary)
    print("Initial Carry:", carry)

    for i in range(positions):
        new_carry = binary[0]
        binary = binary[1:] + carry
        carry = new_carry

        print("After rotation", i + 1, ":", binary,
              "Carry:", carry)

    return binary, carry


# Original 8-bit binary number
binary = "10110110"

# (a) ROL operation
print("Original Binary Number:", binary)

result = rotate_left_without_carry(binary, 2)
print("Final ROL Result:", result)

# (b) RCL operation
initial_carry = "0"

result, final_carry = rotate_left_with_carry(
    binary, initial_carry, 2
)

print("Final RCL Result:", result)
print("Final Carry:", final_carry)
