#!/usr/bin/env python3
import sys


def is_armstrong_number(number: int) -> bool:
    """
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    For example:
    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    ref [ https://exercism.org/tracks/python/exercises/armstrong-numbers ]
    """

    num_str = str(number)
    power   = len(num_str)
    gen_num = sum(int(ch) ** power for ch in num_str)
    return gen_num == number


def main() -> int:
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <number>', file=sys.stderr)
        return 1
    try:
        number = int(sys.argv[1])
    except ValueError:
        print(f'Argument [{sys.argv[1]}] must be an integer.', file=sys.stderr)
        return 2
    print(is_armstrong_number(number))
    return 0


if __name__ == '__main__':
    main()
