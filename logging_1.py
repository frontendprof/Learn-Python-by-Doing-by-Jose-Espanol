# B_R_R
# M_S_A_W



"""
First two levels is not reflected in regular mode, unless you configure it to be reflected

Logging levels:

DEBUG
INFO
WARNING
ERROR
CRITICAL



"""

import logging
#logging.basicConfig(level=logging.DEBUG) #Configuring it to be reflected
#logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s') #Configuring time elements too
logging.basicConfig(format='%(asctime)s %(levelname)-16s [%(filename)s:%(lineno)d] %(message)s') #Configuring extra configs

logger=logging.getLogger('test_logger')

logger.info("This will not show up in ordinary scenario")
logger.warning("This will  show up all the time")
logger.critical("YOur critical message")

