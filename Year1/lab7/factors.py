if __name__ == '__main__':
    def print_factors(x):
        print("The factors of", x, "are:")
        for i in range(1, x + 1):
            if x % i == 0:
                print(i)


    num = int(input("Which number would you like to factorise?: "))

    print_factors(num)
