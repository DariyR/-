while True:
    f_num = int(input("Введіть перше число"))
    s_num = int(input("Введіть друге число"))
    oper = input("Введіть дію")

    if oper == "+":
        print(f_num + s_num)
    if oper == "-":
        print(f_num - s_num)
    if oper == "*":
        print(f_num * s_num)
    if oper == "/":
        if oper == "/" and s_num == 0:
            print("На нуль ділити не можна")
        else:
            print(f_num / s_num)
