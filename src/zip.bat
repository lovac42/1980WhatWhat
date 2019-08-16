@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=nineteen80ww
set NAME=1980WhatWhat
set VERSION=0.0.1

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

quick_manifest.exe "1980 What What" "%REPO%" >%REPO%/manifest.json

echo %VERSION% >%REPO%/VERSION

%ZIP% %NAME%_v%VERSION%_Anki20.zip *.py %REPO%/*

cd %REPO%
%ZIP% ../%NAME%_v%VERSION%_Anki21.ankiaddon *

%ZIP% ../%NAME%_v%VERSION%_CCBC.adze *
