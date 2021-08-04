# Alphabet Rangoli
# Input: 0 < size < 27
# Output: A Rangoli of the inputted size

def print_rangoli(size):
    alphabets = '.abcdefghijklmnopqrstuvwxyz'

    # Recursively generate one line of the Rangoli
    def get_line(line_num, i=0):
        if line_num == i + 1:
            return alphabets[size - i]
        return '{0}-{1}-{0}'.format(alphabets[size - i], get_line(line_num, i + 1))

    length = len(get_line(size))

    # Recursively print the lines of the Rangoli
    def print_result(n):
        line = get_line(size - n + 1).center(length, '-')
        print(line)
        if n != 1:
            print_result(n - 1)
            print(line)

    print_result(size)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
