if __name__ == '__main__':
    def obfusication(anorm):
        stripped = anorm.replace(" ", "")
        encrypted = stripped[::-1]
        print(encrypted)
        return encrypted


    norm = input("What string would you like to encrypt?: ")
    obfusication(norm)