"""
把日志输出到ES上
听说CMRESHandler挺好用的，还没用过暂时
"""

import logging

LOG_LEVEL_MAP = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
}

def init_logger():
    """
    初始化日志器
    :return:
    """
    # need to do
    