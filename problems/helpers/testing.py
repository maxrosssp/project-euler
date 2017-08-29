import time

def get_timed_function(func):
    def timedFunction(*args):
        start = time.time()
        result = func(*args)
        end = time.time()

        return (result, end - start)

    return timedFunction