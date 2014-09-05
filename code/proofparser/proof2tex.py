# Bismillahi-r-Rahmani-r-Rahim

import sys
import re


def convert_line(line):
    # Get the line number
    split = line.split()
    line = ' '.join(split[1:])
    number = int(split[0])

    # Remove the end comments
    end_split = line.split('.')
    line = end_split[0]
    method = end_split[-2].strip()
    assert method.startswith('[')
    assert method.endswith(']')
    method = method[1:][:-1]

    # Find label, if it exists
    label = None
    try:
        label_split = line.split('#')
        label = label_split[1].strip()
        if label.startswith('label('):
            label = label[len('label('):][:-1]
        else:
            label = None
        line = label_split[0].strip()
    except IndexError:
        pass

    return number, line, label, method


def preprocess(lines):
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('%'):
            continue
        yield convert_line(line)


def interpret(lines):
    labels = {}
    new_number = 1
    for number, line, label, method in lines:
        if label:
            labels[number] = label
        if not label:
            labels[number] = new_number
            line_number = new_number
            new_number += 1
            if line.count('P') == 1 and line.startswith('P('):
                assert line.endswith(')')
                line = line[2:][:-1]
            if method == 'assumption':
                yield line_number, line, ['assumption']
            elif method.startswith('ur('):
                uses_labels = [labels[int(use)] for use in
                               re.findall('\d+', method)]
                yield line_number, line, uses_labels
            elif line.startswith('$F'):
                pass
            else:
                raise ValueError("Unknown line format: %s" % line)
                

def to_latex(interpretation):
    var_map = {
        'a': r'\alpha',
        'b': r'\beta',
        'x': r'\phi',
        'y': r'\psi',
        'z': r'\chi',
        'u': r'\omega',
        'v': r'\lor',
        }
    for number, line, uses_labels in interpretation:
        new_line = ''
        i = 0
        while i < len(line):
            if line[i:i+2] == '=>':
                new_line += r'\rightarrow'
                i += 2
            else:
                try:
                    mapped = var_map[line[i]]
                    new_line += mapped
                except KeyError:
                    new_line += line[i]
                i += 1
        tag = "\\tag{%d}" % number
        uses_labels = map(str, uses_labels)
        uses = '\\text{(%s)}' % ', '.join(uses_labels)
        result = tag + ' & ' + new_line + ' & ' + uses + r'\\'
        yield result

if __name__ == "__main__":
    f = open(sys.argv[1])
    p = preprocess(f)
    interp = interpret(p)
    for line in to_latex(interp):
        print line

