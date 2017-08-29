#!/bin/bash
for i in {1..100}
do
	if [ -e "./p$i/p$i.py" ]; then
                mv "./p$i/p$i.py" "./p$i.py"
        fi
done
