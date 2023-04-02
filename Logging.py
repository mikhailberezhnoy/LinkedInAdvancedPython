import logging


fmtstring ="%(asctime)s: %(levelname)s %(funcName)s Line :%(lineno)d %(message)s"
def mb1():
    logging.info('Here')


#logging.basicConfig(filename='c:\mb\pyoutlog.out', level=logging.DEBUG, filemode='w', format =fmtstring)
logging.basicConfig(level=logging.DEBUG, filemode='w', format =fmtstring)
logging.warning ("It's a warning")
logging.info ("It's a info")
mb1()
