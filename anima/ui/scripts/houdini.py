# -*- coding: utf-8 -*-
# Copyright (c) 2012-2017, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

import hou

from anima import logger


if hou.applicationVersion() <= (16, 0, 557):
    from anima.ui import SET_PYSIDE
    from anima.utils import do_db_setup
    SET_PYSIDE()
else:
    from anima.ui import SET_PYSIDE2
    from anima.utils import do_db_setup
    SET_PYSIDE2()


class Executor(object):
    """Executor that binds the UI element to Houdini event loop
    """

    def __init__(self):
        self.application = None
        from anima.ui.lib import QtCore
        self.event_loop = QtCore.QEventLoop()

    def exec_(self, app, dialog):
        self.application = app
        if hou.applicationVersion()[0] <= 15:
            self.application.setStyle('CleanLooks')
        else:
            self.application.setStyle('Fusion')

        hou.ui.addEventLoopCallback(self.processEvents)
        dialog.exec_()

    def processEvents(self):
        self.event_loop.processEvents()
        self.application.sendPostedEvents(None, 0)


def version_creator():
    """Helper function for version_creator UI for Houdini
    """
    # connect to db
    do_db_setup()

    import logging
    from stalker import log
    log.logging_level = logging.WARNING

    from anima.ui import version_creator
    from anima.env import houdini
    reload(houdini)
    reload(version_creator)

    h = houdini.Houdini()

    logger.setLevel(logging.WARNING)

    if hou.applicationVersion()[0] <= 13:
        version_creator.UI(
            environment=h
        )
    else:
        version_creator.UI(
            environment=h,
            executor=Executor()
        )
