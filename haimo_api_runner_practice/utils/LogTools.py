import logging
from loguru import logger
from datetime import date, datetime

class Logger():
    def __init__(self, need_log=True):
        self.my_logger = logger
        
        if need_log is True:
            log_file = "./report/{}/log.txt".format(datetime.now().strftime('%Y%m%d%H%M'))
        self.my_logger.add(log_file, encoding='utf-8')

    def info(self, content):
        self.my_logger.info(content)
    
    def debug(self, content):
        self.my_logger.debug(content)

    def error(self, content):
        self.my_logger.error(content)

    def warning(self, content):
        self.my_logger.warning(content)

my_logger = Logger()

if __name__ == "__main__":
    Logger().info("玩玩")
    Logger().debug("玩玩")
    Logger().warning("玩玩")
    Logger().error("玩玩")


