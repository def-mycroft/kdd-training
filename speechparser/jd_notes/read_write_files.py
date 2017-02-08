from __future__ import print_function
import sys

def write_file(filename):
    with open(filename, 'w') as f:
        for i in range(10):
            print(i, file=f)

        print('some line', file=f)


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.rstrip())
    except IOError as e:
        print(e)


# read_file('test1.txt')

x = input('Give me a number: ')

def test():
    with open('test.txt', 'w') as f:
        i = 0
        for line in sys.stdin:
            if i < 10:
                print(line.rstrip(), file=f)
                i += 1
            else:
                return
