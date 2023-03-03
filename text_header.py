from xml.dom import minidom


def print_xml():
    with minidom.parse('input/template.xml') as file:
        count = 1

        for line in file.getElementsByTagName('line'):
            print('C{0:2d}  '.format(count), end='')

            for part in line.getElementsByTagName('part'):
                print(select_part(part, part.getElementsByTagName('q')), end='')

            print()
            count += 1


def select_part(part, q):
    if q:
        return ' ' * int(q[0].childNodes[0].data)
    else:
        return part.childNodes[0].data


if __name__ == '__main__':
    print_xml()
