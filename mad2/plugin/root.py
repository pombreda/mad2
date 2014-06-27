from __future__ import print_function

import logging
import leip
import os
import re

from mad2.util import get_all_mad_files

lg = logging.getLogger(__name__)


@leip.hook("madfile_post_save", 100)
def root(app, madfile):



    filename = madfile['inputfile']
    madname = madfile['madname']

    #change SHA1SUM file
    dirname = madfile['dirname']
    sha1name = os.path.join(dirname, 'SHA1SUMS')
    qdname = os.path.join(dirname, 'QDSUMS')
    dstats = os.stat(dirname)

    #attempt to set  permissions as non root
    try:
        if os.path.exists(madname):
            fstats = os.stat(filename)
            os.chmod(madname, fstats.st_mode)
    except:
        pass

    try:
        if os.path.exists(sha1name):
            os.chmod(sha1name, 0o664)
        if os.path.exists(qdname):
            os.chmod(qdname, 0o664)
    except:
        pass

    if os.geteuid() != 0:
        #only do something when root
        return


    if os.path.exists(madname):
        fstats = os.stat(filename)
        os.chown(madname, fstats.st_uid, fstats.st_gid)

    if os.path.exists(sha1name):
        os.chown(sha1name, dstats.st_uid, dstats.st_gid)

    if os.path.exists(qdname):
        os.chown(qdname, dstats.st_uid, dstats.st_gid)

