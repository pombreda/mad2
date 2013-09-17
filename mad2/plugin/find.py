from __future__ import print_function

import logging
import sys

import os
import leip

lg = logging.getLogger(__name__)

@leip.arg('-n', '--no_recurse', action='store_true', help='no recursive search')
@leip.command
def find(app, args):
    """
    (recursively) find and print files already mad annotated
    """
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath == '.' and args.no_recurse:
            break
        for f in filenames:
            if f[0] == '.' and f[-4:] == '.mad':
                print(os.path.join(dirpath, f[1:-4]))