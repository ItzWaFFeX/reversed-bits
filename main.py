def reverse_bits(n):
    binary_str = bin(n)[2:]
    
    
    reversed_binary_str = binary_str[::-1]
    
   
    reversed_number = int(reversed_binary_str, 2)
    
    return reversed_number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = reverse_bits(number)
    print(f"The number with its bits reversed is: {result}")
