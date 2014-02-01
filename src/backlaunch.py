# -*- coding: utf-8 -*-
"""
This file is run by VMProxy

(I could run also backend.py directly, but I want to have clean global scope 
in __main__ module (because that's where user scripts run), but backend's global scope 
is far from clean. 
I could also do python -c "from backend import VM: VM().mainloop()", but looks like this 
gives relative __file__-s on imported modules.) 
"""

import logging
import os.path
import sys
from backend import VM

# set up logging
logger = logging.getLogger("thonny.backend")

file_handler = logging.FileHandler(os.path.expanduser(os.path.join("~",".thonny","backend.log")), encoding="UTF-8");
file_handler.setLevel(logging.WARNING);
logger.addHandler(file_handler)

# TODO: sending log records to original stdout could be better (reading from stderr may introduce sync problems)
stream_handler = logging.StreamHandler(stream=sys.stderr)
logger.addHandler(stream_handler)

# create and run VM
VM().mainloop()