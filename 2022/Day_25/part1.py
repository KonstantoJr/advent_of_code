with open('input.txt', 'r') as f:
    data = f.read().splitlines()


def Decimal2SNAFU(decimal):
    SNAFU = ''
    while decimal > 0:
        remainder = decimal % 5
        if remainder == 0:
            SNAFU += '0'
        elif remainder == 1:
            SNAFU += '1'
        elif remainder == 2:
            SNAFU += '2'
        elif remainder == 3:
            SNAFU += '='
            decimal += 5
        elif remainder == 4:
            SNAFU += '-'
            decimal += 5
        decimal = decimal // 5
    return SNAFU[::-1]


def SNAFU2Decimal(SNAFU):
    SNAFU = list(SNAFU)
    SNAFU.reverse()
    decimal = 0
    for i in range(len(SNAFU)):
        if SNAFU[i].isdigit():
            decimal += int(SNAFU[i]) * (5 ** i)
        elif SNAFU[i] == '-':
            decimal += - 1 * (5 ** i)
        elif SNAFU[i] == '=':
            decimal += - 2 * (5 ** i)
    return decimal


decimals = [SNAFU2Decimal(i) for i in data]
totalFuel = sum(decimals)
print(totalFuel, Decimal2SNAFU(totalFuel),
      SNAFU2Decimal(Decimal2SNAFU(totalFuel)))
