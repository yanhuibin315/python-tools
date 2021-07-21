"""
使用按时间分割日志文件的Handler，
调用时直接调用logger即可
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
    logfile = log_conf["config"]["file"]  # 日志文件
    fmt = log_conf["config"]["fmt"]  # 输出格式
    level = log_conf["config"]["level"]  # 日志级别
    seg = log_conf["config"]["segment"]  # 分割时间
    backCount = int(log_conf["config"]["max_counts"])  # 最多文件数
    logger = logging.getLogger(__name__)
    logger.setLevel(LOG_LEVEL_MAP[level])
    th = handlers.TimedRotatingFileHandler(filename=logfile, when=seg, backupCount=backCount, encoding='utf-8')
    th.setFormatter(logging.Formatter(fmt))
    logger.addHandler(th)
    return logger

logger = init_logger()