from xml.dom import minidom


def print_xml():
    line_parts = []
    with minidom.parse('input/template.xml') as file:
        total_width = int(file.getElementsByTagName('total_width')[0].childNodes[0].data)
        left_width = int(file.getElementsByTagName('left_width')[0].childNodes[0].data)

        count = 1

        for line in file.getElementsByTagName('line'):
            line_parts.append('C{0:2d}  '.format(count))

            for part in line.getElementsByTagName('part'):
                line_parts.append(get_data_to_append(line_parts, part, left_width))

            print("".join(line_parts).ljust(total_width))
            count += 1
            line_parts.clear()


def get_data_to_append(line_parts, part, left_width):
    if part.hasAttribute("info"):
        return ''
    elif part.getAttribute("column") == "left":
        return ' ' * (left_width - sum(map(len, line_parts)))
    else:
        return part.childNodes[0].data


def test():
    with minidom.parse('input/template.xml') as file:
        line = file.getElementsByTagName('line')[0]
        print(len(line.childNodes))


if __name__ == '__main__':
    print_xml()
    # test()
