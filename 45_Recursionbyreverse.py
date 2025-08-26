


def reverse_list():
    list = [1, 2, 3, 4, 5]
    if not list:
        return []
    return [list[-1]]+list[:-1]


print(reverse_list())
