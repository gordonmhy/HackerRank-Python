# String Formatting
# Input: 1 <= n <= 99
# Output: From 1 to n, print their respective
# decimal, octal, hexadecimal and binary.

def print_formatted(number):
    # Convert some hex digits to characters
    def display(num, radix):
        if radix != 16 or int(num) < 10:
            return num
        num = int(num) - 10
        return 'ABCDEF'[num]

    # Recursively build the resulting string from decimal
    def convert(decimal, radix=2):
        if decimal < radix:
            return display(str(decimal), radix)
        return convert(decimal // radix, radix) + display(str(decimal % radix), radix)

    # 'length' is the length of the longest binary number in result
    def pad(num, length):
        return ' ' * (length - len(str(num)))

    # Generate resulting lines one after another
    def obtain_resulting_lines(n, length):
        for i in range(1, n + 1):
            result = ''
            result += pad(i, length) + str(i) + ' '
            octal = convert(i, 8)
            result += pad(octal, length) + str(octal) + ' '
            hexadecimal = convert(i, 16)
            result += pad(hexadecimal, length) + str(hexadecimal) + ' '
            binary = convert(i, 2)
            result += pad(binary, length) + str(binary)
            yield result

    for line in obtain_resulting_lines(number, len(convert(number, 2))):
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)