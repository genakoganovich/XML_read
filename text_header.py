from xml.dom import minidom
import struct


class Sgy:
    TEXT_HEADER_SIZE = 3200
    S_I = 17
    S_N = 21

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        self.full_name = path + file_name
        self.attributes = dict()
        self.attributes['line'] = file_name[0:str(file_name).find('_')]
        self.attributes['sample_interval'] = str(Sgy.get_s_interval(self.full_name)) + ' MS'
        self.attributes['trace_length'] = str(Sgy.get_s_len(self.full_name)) + ' MS'
        self.attributes['datum'] = str(100) + ' M'

    def __repr__(self):
        rep = 'Sgy(' + self.path + ', ' \
              + self.file_name + ', ' \
              + str(self.s_interval) + ', ' \
              + str(self.s_len) + ')'
        return rep

    def get_attribute(self, key):
        return self.attributes[key]

    @staticmethod
    def get_value(file_name, position, format_character, size):
        with open(file_name, 'rb') as f:
            f.seek(position)
            return int(struct.unpack(format_character, f.read(size))[0])

    @staticmethod
    def get_s_interval(file_name):
        return int(Sgy.get_value(file_name, Sgy.TEXT_HEADER_SIZE + Sgy.S_I, 'h', 2) / 1000)

    @staticmethod
    def get_s_number(file_name):
        return Sgy.get_value(file_name, Sgy.TEXT_HEADER_SIZE + Sgy.S_N, 'h', 2)

    @staticmethod
    def get_s_len(file_name):
        return Sgy.get_s_interval(file_name) * (Sgy.get_s_number(file_name) - 1)


def print_xml(sgy_file):
    line_parts = []
    with minidom.parse('input/template.xml') as file:
        total_width = int(file.getElementsByTagName('total_width')[0].childNodes[0].data)
        left_width = int(file.getElementsByTagName('left_width')[0].childNodes[0].data)

        count = 1

        for line in file.getElementsByTagName('line'):
            line_parts.append('C{0:2d}  '.format(count))

            for part in line.getElementsByTagName('part'):
                line_parts.append(get_data_to_append(line_parts, part, left_width, sgy_file))

            print("".join(line_parts).ljust(total_width))
            count += 1
            line_parts.clear()


def get_data_to_append(line_parts, part, left_width, sgy_file):
    if part.getAttribute("info").startswith('xml'):
        with minidom.parse('input/Dombey2D_info.xml') as file:
            info_value = file.getElementsByTagName(part.getAttribute("info").split()[1])[0].childNodes[0].data
        return info_value

    elif part.getAttribute("info").startswith('sgy'):
        return sgy_file.get_attribute(part.getAttribute("info").split()[1])

    elif part.getAttribute("column") == "left":
        return ' ' * (left_width - sum(map(len, line_parts)))

    else:
        return part.childNodes[0].data


def test():
    with minidom.parse('input/template.xml') as file:
        line = file.getElementsByTagName('line')[0]
        print(len(line.childNodes))


if __name__ == '__main__':
    print_xml(Sgy('./input/', 'URH-618_MF_PSTM_Stack__20230304.sgy'))
    # test()
