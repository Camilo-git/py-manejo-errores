def run():
    # estructura de una lista
    my_list = [1, "Hello", True, 4.5]
    # estructura de un diccionario
    my_dict = {"firstname": "Facundo", "lastname": "GarcÃ­a"}

    # estructura de una lista que contiene varios diccionarios 
    super_list = [
        {"firstname": "Facundo", "lastname": "GarcÃ­a"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "JosÃ©", "lastname": "Fernandez"},
    ]

    # estructura de un diccionario que contiene varias lastas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    # formas de recorrer lo anterior
    for key, value in super_dict.items():
        print(key, ">", value)

    # for key, value in super_list():
    #     print(key, ">", value)

    # for values in super_list:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')

    for i in super_list:
        print(i)


if __name__ == '__main__':
    run()