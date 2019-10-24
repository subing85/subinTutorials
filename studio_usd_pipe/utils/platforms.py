'''
platforms.py 0.0.1 
Date: January 15, 2019
Last modified: January 26, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import platform

from studio_usd_pipe.utils import config


def get_tool_version():
    return config.get_tool_kit()[2]


def get_tool_name():
    return config.get_tool_kit()[0]


def get_tool_prity_name():
    return config.get_tool_kit()[1]


def get_child(*args):
    tools = {
        'publish': 'Publish'
        }    
    if args[0] not in tools:
        return None    
    return tools[args[0]]







def has_valid():
    tool_oss, tool_app, tool_ver, tool_py = config.get_conig()
    operating_system, application, version, python = get_maya_platform()
    result = {True, 'Support to your maya version'}
    # to block os validation if tool_os != operating_system:
    # to block os validation   result = {False: 'Only support \"%s\" operating system' % tool_os}
    # to block os validation  return result
    if tool_app not in application:
        result = {False: 'Only support \"%s %s\"' %
                  (tool_app, tool_ver)}
        return result
    if tool_ver not in version:
        result = {False: 'Only support \"%s %s\"' %
                  (tool_app, tool_ver)}
        return result
    return result


def get_maya_platform():
    from maya import cmds
    operating_system = platform.system()
    application = cmds.about(q=True, a=True)
    version = cmds.about(q=True, v=True)
    python = platform.python_version()
    return operating_system, application, version, python



def get_tool_kit():
    return config.get_tool_kit()


def get_qwidget():
    import shiboken
    from maya import OpenMayaUI
    from PySide import QtGui
    qwidget = OpenMayaUI.MQtUtil.mainWindow()
    main_window = shiboken.wrapInstance(long(qwidget), QtGui.QWidget)
    return main_window


def get_main_window():
    from maya import cmds
    maya_windows = [each_win for each_win in cmds.lsUI(
        wnd=True) if cmds.window(each_win, q=True, mw=True)]
    return maya_windows[0]
