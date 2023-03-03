from xml.dom import minidom


def print_xml():
    line_parts = []
    with minidom.parse('input/template.xml') as file:
        line_length = int(file.getElementsByTagName('line_length')[0].childNodes[0].data)
        count = 1

        for line in file.getElementsByTagName('line'):
            line_parts.append('C{0:2d}  '.format(count))

            for part in line.getElementsByTagName('part'):
                line_parts.append(select_part(part, part.getElementsByTagName('q')))

            print("".join(line_parts).ljust(line_length))
            count += 1
            line_parts.clear()


def select_part(part, q):
    if q:
        return ' ' * int(q[0].childNodes[0].data)
    else:
        return part.childNodes[0].data


if __name__ == '__main__':
    print_xml()
