# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/1980WhatWhat


from anki import version
from anki.hooks import wrap
from anki.exporting import AnkiPackageExporter

from .main import touch_media

try:
    from ccbc.media import ExtMediaManager as MediaManager
except ImportError:
    from anki.media import MediaManager


#Export apkgs
if version.startswith("2.1"):
    AnkiPackageExporter._exportMedia = wrap(
        AnkiPackageExporter._exportMedia,touch_media,"before"
    )
else:
    AnkiPackageExporter.exportFiltered = wrap(
        AnkiPackageExporter.exportFiltered,touch_media,"before"
    )


#Sync
MediaManager.mediaChangesZip = wrap(
    MediaManager.mediaChangesZip,touch_media,"before"
)


#MenuTools:Check Media
MediaManager.check = wrap(
    MediaManager.check,touch_media,"before"
)
