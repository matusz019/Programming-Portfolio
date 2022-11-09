if __name__ == '__main__':
    num = int(input("Please type a positive integer: "))
    binary = bin(num)
    print(f"the unsigned binary value for that number is: {binary[2:]}")
