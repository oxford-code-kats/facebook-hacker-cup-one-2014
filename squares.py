from collections import namedtuple


Bounds = namedtuple('Bounds', ['xmin', 'ymin', 'xmax', 'ymax'])

def translate(input):
    chars = {'.': 0, '#': 1}
    return [chars[char] for char in input]

def parse_inputs(data):
    return [translate(line) for line in data]

def get_bounds(data):
    min_x_index = get_bound(data, row_min, min)
    max_x_index = get_bound(data, row_max, max)
    min_y_index = get_bound(zip(*data), row_min, min)
    max_y_index = get_bound(zip(*data), row_max, max)
    return Bounds(xmin=min_x_index, xmax=max_x_index, ymin=min_y_index, ymax=max_y_index)

def get_bound(data, row_min_max, min_max):
    indexes = (row_min_max(row) for row in data)
    filtered = (index for index in indexes if index is not None)
    return min_max(filtered, default=None)

def is_square(bounds):
    if bounds.xmin is None:
        return False
    return bounds.xmax - bounds.xmin == bounds.ymax - bounds.ymin

def row_min(row):
    try:
        return row.index(1)
    except ValueError:
        return None

def row_max(row):
    max_index = None
    for index, elem in enumerate(row):
        if elem == 1:
            max_index = index
    return max_index

def is_filled(data, bounds):
    for row in data[bounds.ymin:bounds.ymax + 1]:
        if not all(row[bounds.xmin:bounds.xmax + 1]):
            return False
    return True