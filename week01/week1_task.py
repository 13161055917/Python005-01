import logging
import os
from datetime import datetime
from pathlib import Path

def log_name():
    nowtime = datetime.strftime(datetime.today(), '%Y-%m-%d')
    filename = f'学习资料/极客时间/python进阶训练营/Python005-01/week01/python-{nowtime}'
    if not Path(filename).exists():
        os.mkdir(filename)

    logging.basicConfig(filename=filename+'/name.log',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')

    logging.info("func log_test running")

if __name__ == '__main__':
    log_name()