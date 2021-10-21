def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'before {type(args)} {type(kwargs)}')
        result = func(*args, **kwargs)
        print('after')
        return result

    return wrapper


def decorator_without_args(func):
    def wrapper():
        print('before')
        result = func()
        print('after')
        return result

    return wrapper


@decorator
def decorated_without_args():
    print('inside')
    return 'result'


@decorator
def decorated_with_args(arg1, arg2):
    print('inside')
    return f'result {arg1} {arg2}'


@decorator
def decorated_with_default_args(arg1='default1', arg2='default2'):
    print('inside')
    return f'result {arg1} {arg2}'


@decorator
def decorated_with_mixed_args(arg1, arg2, arg3='default3', arg4='default4'):
    print('inside')
    return f'result {arg1} {arg2} {arg3} {arg4}'


@decorator_without_args
def decorated_without_args2():
    print('inside')
    return 'result'


# @decorator_without_args # this would not work
def decorated_with_args2(arg1, arg2):
    print('inside')
    return f'result {arg1} {arg2}'


print(decorated_without_args())
print(decorated_with_args('one', 'two'))
print(decorated_with_default_args())
print(decorated_with_default_args(arg1='one'))
print(decorated_with_default_args(arg1='one', arg2='two'))
print(decorated_with_mixed_args('one', 'two'))
print(decorated_with_mixed_args('one', 'two', arg3='three', arg4='four'))

print(decorated_without_args2())
print(decorated_with_args2('one', 'two'))
