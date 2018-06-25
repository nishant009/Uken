import ast
import optparse
import pydash as py

from intervaltree import Interval, IntervalTree

def find_diff(list_a, list_b):
    interval_tree = IntervalTree()
    
    for interval in list_a:
        interval_tree.add(Interval(interval[0], interval[1]))

    for interval in list_b:
        interval_tree.chop(interval[0], interval[1])

    result = []
    for item in interval_tree.items():
        result.append((item.begin, item.end))
    
    return result

def main():
    """Example invocation:
    python solution.py
        --lista='[(900, 1100), (1300, 1500)]' \
        --listb='[(900, 915), (1000, 1015), (1230, 1600)]'
    """
    parser = optparse.OptionParser()
    parser.add_option(
        '-a',
        '--lista',
        action='store',
        dest='list_a',
        help='First list',
        default=None
    )
    parser.add_option(
        '-b',
        '--listb',
        action='store',
        dest='list_b',
        help='Second List',
        default=None
    )
    options, _ = parser.parse_args()

    if py.is_empty(options.list_a) or py.is_empty(options.list_b):
        return

    result = find_diff(
        ast.literal_eval(options.list_a),
        ast.literal_eval(options.list_b)
    )

    print('Result of listA - listB: ')
    print(result)

if __name__ == "__main__":
    main()