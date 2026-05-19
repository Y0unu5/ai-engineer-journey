
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('ArithmeticApp')

def add(a,b):
    logger.info('Addition of %s and %s',a,b)
    return a+b

def subtract(a,b):
    logger.info('Subtraction of %s and %s',a,b)
    return a-b

def multiply(a,b):
    logger.info('Multiplication of %s and %s',a,b)
    return a*b

def divide(a,b):
    try:
        logger.info('Division of %s and %s',a,b)
        return a/b
    except ZeroDivisionError:
        logger.error('Cannot divide by zero')

add(5,20)
subtract(10,5)
multiply(5,5)
divide(10,0)
