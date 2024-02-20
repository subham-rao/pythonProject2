def sample():
    name = "subham"
    def sample2():
        nonlocal name
        print(name)
        name = "tested "
    print(name)

    sample2()
    print(name)

sample()