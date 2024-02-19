from bombyx import bombyx1, bombyx2
import sys

args = sys.argv[1:]

if __name__ == '__main__':
    try:
        if (len(args) == 2 and bombyx1(args[0], args[1]) == 0):
            exit(0)
        if (len(args) == 3 and bombyx2(args[0], args[1], args[2]) == 0):
            exit(0)
        exit(84)
    except Exception as e:
        exit(84)


