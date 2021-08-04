# Text Wrap

# Recursively splits the string into blocks of
# strings of width 'max_width'
def wrap(string, max_width):
    if len(string) <= max_width:
        return string
    return string[:max_width] + '\n' + wrap(string[max_width:], max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
