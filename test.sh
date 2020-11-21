#!/bin/bash

blender --background test.blend \
        --python-use-system-env \
        --python ./test.py 
        # --engine CYCLES \
        # --render-output //test-##.png \
        # --render-format PNG \
        # --threads 0 \
        # --render-frame 1
