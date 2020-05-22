#!/usr/bin/env python3

from pathlib import Path
import sys


def main():
    if len(sys.argv) != 3:
        print('usage: %s <sources path> <<priority class name>,>')
        sys.exit(1)
    classes = {}
    from_imports = {}
    imports = {}
    priority_class_names = sys.argv[2].split('|')
    for path in Path(sys.argv[1]).glob('**/*.py'):
        if str(path).endswith('/__init__.py'):
            continue
        state = None
        class_name = None
        class_lines = []
        with open('./%s' % path, 'r') as f:
            for line in f:
                line = line.rstrip()
                if not line and state != 'class':
                    continue
                if line.startswith('# internal imports'):
                    state = 'internal imports'
                elif line.startswith('from'):
                    if state != 'internal imports':
                        from_imports[line] = True
                elif line.startswith('import'):
                    if state != 'internal imports':
                        imports[line] = True
                elif line.startswith('class'):
                    state = 'class'
                    class_name = line
                    class_lines.append(line)
                else:
                    class_lines.append(line)
        classes[class_name] = class_lines
    tmp = list(from_imports.keys())
    tmp.sort()
    print('\n'.join([key for key in tmp]))
    print('')
    tmp = list(imports.keys())
    tmp.sort()
    print('\n'.join([key for key in tmp]))
    tmp = list(classes.keys())
    tmp.sort()
    for priority_class_name in priority_class_names:
        print('\n')
        print('\n'.join(classes[priority_class_name]))
        tmp.remove(priority_class_name)
    for class_name in tmp:
        print('\n')
        print('\n'.join(classes[class_name]))


if __name__ == '__main__':
    main()
