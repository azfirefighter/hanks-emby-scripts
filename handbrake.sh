#!/bin/bash

SRC=/home/henry/handbrake/to_process
DEST=/home/henry/handbrake/processed
DEST_EXT=mp4
HANDBRAKE_CLI=HandBrakeCLI

python3 rename.py

for FILE in `ls $SRC`
do
        filename=$(basename $FILE)
        extension=${filename##*.}
        filename=${filename%.*}

        $HANDBRAKE_CLI -i "$SRC/$FILE" -o "$DEST/$filename.$DEST_EXT" -e x264 -q 20 -O
	
	rm $SRC/$FILE
done

python3 rename_and_ship.py