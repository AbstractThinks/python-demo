def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# now = log(now)
@log
def now():
    print('2017-06-01')


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# now = log('execute')(now)
@log2('execute')
def now2():
    print('2015-3-25')

if __name__ == '__main__':
    now()
    now2()
