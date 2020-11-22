import sys


def get_all_lines_from_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    return lines


class Point:
    def __init__(self, coordinates_in_string):
        self.X = float(coordinates_in_string.split(' ')[0])
        self.Y = float(coordinates_in_string.split(' ')[1])


def length(first_point, second_point):
    return ((first_point.X - second_point.X) ** 2 + (first_point.Y - second_point.Y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.l1 = length(p1, p2)
        self.l2 = length(p2, p3)
        self.l3 = length(p3, p1)

def is_this_triangle_isosceles(self):
    if self.l1 == self.l2 or self.l2 == self.l3 or self.l3 == self.l1:
        return True
    else:
        return False

def is_this_triangle_exists(self):
    lengths = [self.l1, self.l2, self.l3]
    lengths = sorted(lengths)
    if lengths[2] < lengths[0] + lengths[1]:
        return True
    else:
        return False

def square(self):
    p = (self.l1 + self.l2 + self.l3) / 2
    s = (p * (p - self.l2) * (p - self.l2) * (p - self.l3)) ** 0.5
    return s


def create_triangle(line):
    line = line.rstrip('\n')
    p1 = Point(line)
    line = ' '.join(line.split(' ')[2:])
    p2 = Point(line)
    line = ' '.join(line.split(' ')[2:])
    p3 = Point(line)
    return Triangle(p1, p2, p3)


def write_to_file(destination, coordinates):
    file = open(destination, "w")
    file.write(coordinates)
    file.close()


def main(source, destination):
    lines = get_all_lines_from_file(source)
    max_square = 0
    for i in range(len(lines)):
        triangle = create_triangle(lines[i])
    if triangle.is_this_triangle_exists() is True and triangle.is_this_triangle_isosceles() is True:
        square = triangle.square()
    else:
        square = -1
    max_square = max(square, max_square)
    if square == max_square:
        write_to_file(destination, lines[i])


    if __name__ == '__main__':
        main(sys.argv[1], sys.argv[2])