def get_even_list(l):
    new_list = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new_list.append(l[i])
    return new_list

# default_list = [1,4,5,-1,10]
# print(get_even_list(default_list))
