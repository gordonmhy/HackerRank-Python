# Alphabet Rangoli
# Input: 0 < size < 27
# Output: A Rangoli of the inputted size

def print_rangoli(size):
    alphabets = '.abcdefghijklmnopqrstuvwxyz'

    # Recursively generate one line of the Rangoli
    def get_line(line_num, i=0):
        if line_num == i + 1:
            return alphabets[size - i]
        return alphabets[size - i] + '-' + get_line(line_num, i + 1) + '-' + alphabets[size - i]

    length = len(get_line(size))

    # Pad each line of the Rangoli with '-'
    def pad(line):
        result = line
        while len(result) < length:
            result = '-' + result + '-'
        return result

    # Recursively print the lines of the Rangoli
    def print_result(n):
        if n == 1:
            print(pad(get_line(size - n + 1)))
        else:
            print(pad(get_line(size - n + 1)))
            print_result(n - 1)
            print(pad(get_line(size - n + 1)))

    print_result(size)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
