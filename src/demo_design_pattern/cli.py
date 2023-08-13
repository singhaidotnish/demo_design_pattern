import argparse
from . import concept as concept


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--add', help="requires name phone address ", action='store_true')
    parser.add_argument('-n', '--name', help="name type string all characters")
    parser.add_argument('-p', '--phone', help="phone type string all digits only")
    parser.add_argument('-ad', '--address', help="address type string all characters and special characters")
    parser.add_argument(
        '-di', '--display', help="display on terminal", action='store_true')
    parser.add_argument(
        '-ft', '--filetype', help="yaml or json")

    parser.add_argument(
        '-c', '--convert', help="Take input format and show in another format. "
                                "requires filetype and filetype_to", action='store_true')
    parser.add_argument(
        '-fto', '--filetype_to', help="File type options yaml or json")
    parser.add_argument(
        '-fl', '--filter', help="Requires parameter like Joe*")
    parser.add_argument(
        '-at', '--all_types', help='List all file types', action='store_true')

    args = parser.parse_args()

    if args.filter and not args.filetype:
        parser.error('The -Filter argument requires --filetype')
    # not permissible
    if args.convert and not (args.filetype and args.filetype_to):
        parser.error('The -Convert argument requires --filetype and --filetype_to')
        return
    if args.display and not args.filetype:
        parser.error('The -Display argument requires --filetype')
        return
    if args.add and not (args.name and args.phone and args.address):
        parser.error('The -Add argument requires -Name and -Phone and -Address ')
        return
    if args.add and not args.filetype:
        parser.error('The -Add argument requires filetype too')
        return
    if args.add and (args.display or args.convert or args.filter):
        parser.error('The -Add argument does not require the -Display or -Convert or -Filter')
        return

    # permissible
    if args.display and args.filetype:
        filetype = args.filetype
        ui = concept.Ui(filetype)
        ui.call_display()
        return

    if args.filter and args.filetype:
        _filter = args.filter
        _filetype = args.filetype
        ui = concept.Ui(_filetype)
        ui.call_filter(_filter)
        return

    if args.convert and args.filetype and args.filetype_to:
        _filetype = args.filetype
        _filetype_to = args.filetype_to
        ui = concept.Ui(_filetype)
        ui.call_convert(_filetype_to)
        return

    if args.add and args.filetype and (args.name and args.phone and args.address):
        _filetype = args.filetype
        _name = args.name
        _phone = args.phone
        _address = args.address
        item = {'name': _name, 'phone': _phone, 'address': _address}
        ui = concept.Ui(_filetype)
        ui.call_add(item)
        return

    if args.all_types:
        _filetype = 'Json'
        ui = concept.Ui(_filetype)
        ui.call_list_of_all_types()


if __name__ == '__main__':
    main()
