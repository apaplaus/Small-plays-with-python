#!/usr/bin/env python3


class TooManyCallsError(Exception):
    """ Exception class for big amout of function calles"""

    pass


def limit_calls(max_calls=2, error_message_tail='called too often'):
    """ Decorator generator function"""

    calls = 0

    def decorator(func):
        """ Decorator that will be applyed to function to restrict it's calls"""

        def wrapper(*args, **kwargs):
            """ Wrapper that checks function calls and limits it"""

            nonlocal calls
            calls += 1
            if calls > max_calls:
                specific_error_message = "function \"{}\" - ".format(func.__name__) + error_message_tail
                raise TooManyCallsError(specific_error_message)
            func(*args, **kwargs)

        return wrapper
    return decorator


def ordered_merge(*args, selector={}):
    """ Generator function that construct itarable from other iterables"""

    temp_args = []
    for item in args:
        temp_args.append(list(item))
    for pos, select in enumerate(selector):
        yield temp_args[select].pop(0)


class Log:
    """ Class for logging into file and deal with exceptions"""

    def __enter__(self):
        """ Called befor 'with' block"""

        self.file = open(self.file_name, "w")
        self.file.write('Begin\n')
        return self

    def __init__(self, file: str):
        """ Construct class object"""

        self.file_name = file

    def logging(self, output: str):
        """ Log message into file"""

        self.file.write(output + "\n")

    def __exit__(self, type, value, traceback):
        """ Called at the end of 'with' block"""

        self.file.write('End\n')
        self.file.close()
        return True


def test():
    """Test functionality of implemented fucntions"""

    assert list(ordered_merge('abcde', [1, 2, 3], (3.0, 3.14, 3.141), range(11, 44, 11), selector = [2,3,0,1,3,1])) == [3.0, 11, 'a', 1, 22, 2]
    with Log('mylog.txt') as logfile:
        logfile.logging('Test1')
        logfile.logging('Test2')
        a = 1 / 0
        logfile.logging('Test3')


if __name__ == '__main__':
    test()
