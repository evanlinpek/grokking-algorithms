import logging

class LogConfigurator:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def add_console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.logger.level)
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

    def add_file_handler(self, filename):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(self.logger.level)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

# 使用日志类
log_config = LogConfigurator('my_logger', logging.DEBUG)
log_config.add_console_handler()  # 将日志输出到控制台
log_config.add_file_handler('my_log.log')  # 将日志输出到文件



if __name__ == '__main__':
    # 获取logger并使用
    logger = log_config.logger
    logger.debug('这是一个debug级别的日志')
    logger.info('这是一个info级别的日志')
    logger.warning('这是一个warning级别的日志')
    logger.error('这是一个error级别的日志')
    logger.critical('这是一个critical级别的日志')