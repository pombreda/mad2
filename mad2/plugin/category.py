from __future__ import print_function

import logging
import sys

import leip
from mad2.util import get_all_mad_files

lg = logging.getLogger(__name__)


@leip.arg('file', nargs='*')
@leip.arg('category', help='category to assign to these files')
@leip.commandName('=')
def apply_category(app, args):
    """
    apply a predefined category to a (set of) file(s)
    """
    catinfo = app.conf.get_branch('template.{}'.format(args.category))
    if not catinfo:
        print("Invalid category: {0}".format(args.category))
        print("Choose from:")
        tempinfo = app.conf.get_branch('template')
        for cat in app.conf.find_branch('template'):
            print(" - {0}".format(cat))
        sys.exit()

    for madfile in get_all_mad_files(app, args):
        madfile.mad.update(catinfo)
        madfile.save()
