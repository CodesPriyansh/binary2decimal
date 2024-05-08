def binary_to_decimal(binary):
    decimal = 0
    power = 0
    
    # Iterate through the binary digits from right to left
    for digit in reversed(binary):
        if digit == '1':
            # Add the value of the current digit multiplied by 2^power to the decimal number
            decimal += 2 ** power
        # Increment the power for the next digit
        power += 1
    
    return decimal

# Example usage:
binary_number = input("enter binary number:")
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of binary number {binary_number} is: {decimal_number}")
