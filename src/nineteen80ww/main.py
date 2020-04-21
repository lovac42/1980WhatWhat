# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/1980WhatWhat


import os, time
from os.path import isfile, join
from anki.hooks import wrap
from aqt.utils import showText
from aqt import mw


DOS_EPOCH_TIME=315550800

def touch_media(self, *args, **kwargs):
    media = []
    m=mw.col.media.dir()
    for f in os.listdir(m):
        fpath=join(m,f)
        if isfile(fpath):

            #TEST: set to 1979
            # os.utime(fpath,(315550000,315550000))

            if os.stat(fpath).st_mtime<DOS_EPOCH_TIME:
                t=time.time()
                os.utime(fpath,(t,t))
                media.append(f)

    if media:
        lst="\n".join(media)
        showText("Incorrect mod time before 1980, auto updated:\n\n%s"%lst)


##### WRAPS #################

from anki import version
from anki.exporting import AnkiPackageExporter

if version.endswith("ccbc"):
    from ccbc.media import ExtMediaManager as MediaManager
else:
    from anki.media import MediaManager

#Export apkgs
if version.startswith("2.1"):
    AnkiPackageExporter._exportMedia=wrap(AnkiPackageExporter._exportMedia,touch_media,"before")
else:
    AnkiPackageExporter.exportFiltered=wrap(AnkiPackageExporter.exportFiltered,touch_media,"before")

#Sync
MediaManager.mediaChangesZip=wrap(MediaManager.mediaChangesZip,touch_media,"before")

#MenuTools:Check Media
MediaManager.check=wrap(MediaManager.check,touch_media,"before")
