# String Validators


if __name__ == '__main__':
    string_list = [i for i in input()]
    print('\n'.join(map(lambda x: str(x),
                        [True in map(lambda x: x.isalnum(), string_list),
                         True in map(lambda x: x.isalpha(), string_list),
                         True in map(lambda x: x.isdigit(), string_list),
                         True in map(lambda x: x.islower(), string_list),
                         True in map(lambda x: x.isupper(), string_list)])))
