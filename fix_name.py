import os
import sys
import getopt


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi", ["file"])
    except getopt.GetoptError:
        print('test.py -i <file>')
        sys.exit(2)



if __name__ == "__main__":
    main(sys.argv)

