#!/bin/bash
for i in {1..100}
do
	if [ ! -d "p$i" ]; then
		# Control will enter here if $DIRECTORY exists.
		mkdir "p$i"
	fi

	if [ ! -e "./p$i/__init__.py" ]; then
                touch "p$i/__init__.py"
        fi

	if [ ! -e "./p$i/p$i.py" ]; then
		touch "p$i/p$i.py"
	fi
done
