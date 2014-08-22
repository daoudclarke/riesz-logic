# Bismillahi-r-Rahmani-r-Rahim

import sys



def convert_line(line):
    # Get the line number
    split = line.split()
    line = ' '.join(split[1:])
    number = int(split[0])

    # Remove the end comments
    end_split = line.split('.')
    line = end_split[0]
    method = end_split[-2]

    # Remove hash comments
    label = None
    try:
        label_split = line.split('#')
        label = label_split[1].strip()
        line = label_split[0].strip()
    except IndexError:
        pass

    return number, line, label, method




def convert(lines):
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('%'):
            continue
        yield convert_line(line)


if __name__ == "__main__":
    f = open(sys.argv[1])
    for line in convert(f):
        print line

