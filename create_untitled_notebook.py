"""Write the old terminal path as target_path into the new Untitled notebook."""

import sys

terminal_path = sys.argv[1]
print('supplied path:', terminal_path)

with open('import_statements.ipynb', 'r') as f:
    txt = f.read()

untitled = txt.replace('#os.chdir()', 'os.chdir(\\"{}\\")'.format(terminal_path))

with open('Untitled.ipynb', 'w') as f:
    f.write(untitled)
