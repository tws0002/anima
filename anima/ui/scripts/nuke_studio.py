# -*- coding: utf-8 -*-
# Copyright (c) 2012-2013, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#import nuke

import nuke
from nukescripts import *

def set_qt_lib():
    if nuke.NUKE_VERSION_MAJOR < 10 or (nuke.NUKE_VERSION_MAJOR == 11):
        from anima.ui import SET_PYSIDE2
        SET_PYSIDE2()
    else:
        from anima.ui import SET_PYSIDE
        SET_PYSIDE()

from anima.utils import do_db_setup

def version_creator():
    """Helper function for version_creator UI for Nuke
    """
    # connect to db
    do_db_setup()

    # set PySide or PySide2
    set_qt_lib()

    from anima.ui import version_creator
    from anima.env import nuke_studioEnv
    ns = nuke_studioEnv.NukeStudio()
    ns.name = "NukeStudio"

    # display only warning messages
    import logging
    logging.getLogger(version_creator.__name__).setLevel(logging.WARNING)
    logging.getLogger("anima.ui").setLevel(logging.WARNING)
    logging.getLogger("anima.ui.models").setLevel(logging.WARNING)
    logging.getLogger("anima.env.nuke_studioEnv").setLevel(logging.WARNING)
    logging.getLogger("stalker.db").setLevel(logging.WARNING)

    version_creator.UI(environment=ns)
