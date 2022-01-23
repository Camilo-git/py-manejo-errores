def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2

    # print(my_dict)

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


    # list comprehension multiplos de 4, 6, y 9

    # number = [i for i in range(1, 100000) if i % 36 == 0]
    number = [i for i in range(1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(number)

    # 
    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}

    print(my_dict)

if __name__ == "__main__":
    run()