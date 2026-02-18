

def after(seconds, func, *args):
    import time
    time.sleep(seconds)
    # print(len(args))
    func(args)


def greeting(a):
    print(a)
    for i in a:
        print(f'Hello Guido, {i}')

after(2, greeting,*range(5), 'you old asshole!') # unpacking the range

