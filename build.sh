#!/usr/bin/env bash

WORKING_DIR=$(dirname "${BASH_SOURCE[0]}")
WORKING_DIR=$(cd "$WORKING_DIR" && pwd)

[ ! -d "$WORKING_DIR/bin" ] && mkdir "$WORKING_DIR/bin"

for dir in python js bash; do
    if [ -d "$dir" ]; then
        for file in "$dir"/*; do
            filename=$(basename -- "$file")
            filename="${filename%.*}"
            cp "$file" "$WORKING_DIR/bin/$filename"
            chmod a+x "$WORKING_DIR/bin/$filename"
        done
    fi
done

echo "Add below line to your .bash_profile all other loaded shell profiles if you want to use these scripts globally:"
echo "export PATH=\"$WORKING_DIR/bin:\$PATH\""
