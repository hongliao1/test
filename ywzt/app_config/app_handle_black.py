import logging


def app_handle_black(func):
    def hendle_1(*args, **kwargs):
        logging.info('run\t' + func.__name__ + '\n 定位方法:' + repr(args[1:][0]) + '\n 值:' + repr(args[1:][1]) + '\n' + repr(kwargs))
        element = func(*args, **kwargs)
        return element

    return hendle_1
