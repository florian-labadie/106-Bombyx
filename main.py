from bombyx import grown_rate, init_and_end_generation
import sys

args = sys.argv[1:]

if __name__ == '__main__':
    try:
        if (len(args) == 2 and grown_rate(args[0], args[1]) == 0):
            exit(0)
        if (len(args) == 3 and init_and_end_generation(args[0], args[1], args[2]) == 0):
            exit(0)
        exit(84)
    except Exception as e:
        exit(84)


