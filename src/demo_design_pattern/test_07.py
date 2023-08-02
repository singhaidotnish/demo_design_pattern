import argparse
from .test_04 import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--add', help="requires name phone address ")
    parser.add_argument('-n', '--name', help="name type string all characters")
    parser.add_argument('-p', '--phone', help="phone type string all digits only")
    parser.add_argument('-ad', '--address', help="address type string all characters and special characters")
    parser.add_argument(
        '-di', '--display', help="filter is optional", action='store_true')
    # TODO if display then filter is optional
    parser.add_argument(
        '-c', '--convert', help="requires filetype_from and filetype_to", action='store_true')
    parser.add_argument(
        '-s', '--filetype_from', help="File type options yaml or json", action='store_true')
    parser.add_argument(
        '-de', '--filetype_to', help="File type options yaml or json", action='store_true')
    parser.add_argument(
        '-f', '--filter', help="requires name=Joe*")
    parser.add_argument(
        '-f', '--filetype', help="yaml or json")

    args = parser.parse_args()
    if args.add and (args.display or args.convert):
        print('+++ Only one of {} {} above possible'.format('display', 'convert'))
        return
    if args.convert and not (args.filetype_from and args.filetype_to):
        print('+++ requires filetype_from and filetype_to ')
        return
    if args.display:
        print('+++ filter is optional')
        return
    if args.add and not (args.name and args.phone and args.address):
        print('+++ add name phone address mandatory')
        return
    if args.display and args.filter and args.filetype:
        print('+++ call test_04 ui.filter')
        return


if __name__ == '__main__':
    main()
