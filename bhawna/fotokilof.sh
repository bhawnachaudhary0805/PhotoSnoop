#!/bin/sh

# MYPATH - path to bhawna python source
MAIN=__main__.py
MYPATH="${0%/*}"
cd $MYPATH

# compile MO files, usable for testing tanslations
NAME=bhawna
cd locale/
for I in ??; do
    cd $I/LC_MESSAGES
    if [ -e $NAME.po ]; then
        msgfmt $NAME.po -o $NAME.mo
    fi
    cd ../../
done
cd ..

# run bhawna
python3 $MAIN &

