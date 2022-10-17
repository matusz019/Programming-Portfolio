def greeting(name):
    name = str.lower(name)
    print(f"Hello {name.title()}. Pleased to meet you")
greeting(input("What is your name? "))
