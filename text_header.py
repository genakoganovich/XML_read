from xml.dom import minidom

# parse a xml file by name
file = minidom.parse('input/template.xml')

for line in file.getElementsByTagName('line'):
    for part in line.getElementsByTagName('text'):
        print(part.childNodes[0].data, end='')

    print()
