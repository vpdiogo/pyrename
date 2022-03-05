import sys
from .lib.rename import rename_file


def main():
    old_file = str(sys.argv[1])
    new_file = str(sys.argv[2])

    rename_file(old_file, new_file)

    return


if __name__ == '__main__':
    main()
