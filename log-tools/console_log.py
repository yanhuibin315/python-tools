"""
把日志输出到控制台
"""

import logging
from logging import handlers
import yaml

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
    with open("log.yaml", "r") as f:
        log_conf = yaml.load(f, Loader=yaml.BaseLoader)
    fmt = log_conf["config"]["fmt"]  # 输出格式
    level = log_conf["config"]["level"]  # 日志级别
    sh = logging.StreamHandler()#往屏幕上输出
    sh.setFormatter(fmt) #设置屏幕上显示的格式
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL_MAP[level])
    logger.addHandler(sh)
    return logger

logger = init_logger()