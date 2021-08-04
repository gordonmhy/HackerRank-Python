# String Formatting
# Input: string where 0 < len(string) < 1000
# Output: Print True in each line if string has any
# alphanumeric characters, alphabetical characters,
# digits, lowercase characters and uppercase characters
# respectively.


if __name__ == '__main__':
    string_list = [i for i in input()]
    print('\n'.join(map(lambda x: str(x),
                        [True in map(lambda x: x.isalnum(), string_list),
                         True in map(lambda x: x.isalpha(), string_list),
                         True in map(lambda x: x.isdigit(), string_list),
                         True in map(lambda x: x.islower(), string_list),
                         True in map(lambda x: x.isupper(), string_list)])))
