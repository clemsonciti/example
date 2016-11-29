import argparse
import sys
import os
import shutil
import textwrap
import string

# this parser will default to printing the help text on error:
class GetExampleParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def list_examples(args):
    print('')
    print('Available examples:')
    for i, d in enumerate(os.listdir(args.examples_dir)):
        if d.startswith('.'):
            continue
        print('    {0}. {1}'.format(i+1, d))

def get_example(args):
    print('')
    print("Getting example {0}".format(args.name))

    example_dir = os.path.join(args.examples_dir, args.name)
    if args.dest:
        dest_dir = args.dest
    else:
        dest_dir = './{0}'.format(args.name)

    if not os.path.isdir(example_dir):
        print('*** Error: no example named {0} ***'.format(args.name))
        sys.exit(1)

    try:
        shutil.copytree(example_dir, dest_dir)
    except OSError:
        print("*** Error in copying to {0}; perhaps a folder called {0} already exists? ***".format(dest_dir))
        sys.exit(1)

    print('Example {0} copied into {1}.'.format(args.name, os.path.abspath(dest_dir)))

def get_example_info(args):
    print('')
    print("Description for example \"{0}\":".format(args.name))

    example_dir = os.path.join(args.examples_dir, args.name)
    if not os.path.isdir(example_dir):
        print('*** Error: no example named {0} ***'.format(args.name))
        sys.exit(1)

    with open(os.path.join(args.examples_dir, args.name, 'README.md')) as f:
        print(reindent(f.read()))

def reindent(s, numSpaces=4):
    s = s.split('\n')
    s = [(numSpaces * ' ') + line.lstrip() for line in s]
    s = string.join(s, '\n')
    return s
