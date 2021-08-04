# Designer Door Mat


# line starts from 1
# Recursively prints each line of the door mat
def print_line(line=1, width=3, length=9):
    if line == width // 2 + 1:
        print('WELCOME'.center(length, '-'))
    else:
        pattern = ('.|.' + (line - 1) * '.|..|.').center(length, '-')
        print(pattern)
        print_line(line + 1, width, length)
        print(pattern)


width, length = map(lambda x: int(x), str(input()).split(' '))
print_line(width=width, length=length)
