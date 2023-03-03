from xml.dom import minidom


def print_xml():
    with minidom.parse('input/template.xml') as file:
        count = 1

        for line in file.getElementsByTagName('line'):
            print('C{0:2d}  '.format(count), end='')

            for part in line.getElementsByTagName('part'):
                print_part(part, part.getElementsByTagName('q'))

            print()
            count += 1


def print_part(part, q):
    if q:
        print(' ' * int(q[0].childNodes[0].data), end='')
    else:
        print(part.childNodes[0].data, end='')


if __name__ == '__main__':
    print_xml()
