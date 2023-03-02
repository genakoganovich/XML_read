from xml.dom import minidom

# parse a xml file by name
with minidom.parse('input/template.xml') as file:
    count = 1

    for line in file.getElementsByTagName('line'):
        print('C{0:2d}  '.format(count), end='')

        for part in line.getElementsByTagName('text'):
            print(part.childNodes[0].data, end='')

        print()
        count += 1
