from xml.dom import minidom


def print_xml():
    line_parts = []
    with minidom.parse('input/template.xml') as file:
        line_length = int(file.getElementsByTagName('line_length')[0].childNodes[0].data)
        column_width = int(file.getElementsByTagName('column_width')[0].childNodes[0].data)
        count = 1

        for line in file.getElementsByTagName('line'):
            line_parts.append('C{0:2d}  '.format(count))

            for part in line.getElementsByTagName('part'):
                line_parts.append(get_data_to_append(column_width, line_parts, part))

            print("".join(line_parts).ljust(line_length))
            count += 1
            line_parts.clear()


def get_data_to_append(column_width, line_parts, part):
    if part.getAttribute("type") == 'c':
        to_append = (line_parts.pop() + part.childNodes[0].data).ljust(column_width)
    else:
        to_append = part.childNodes[0].data
    return to_append


def get_attr():
    with minidom.parse('input/template.xml') as file:
        line = file.getElementsByTagName('line')[0]
        part = line.getElementsByTagName('part')[0]
        print(part.getAttribute("type"))


if __name__ == '__main__':
    print_xml()
    # get_attr()

