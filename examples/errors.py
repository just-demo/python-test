class CustomError1(Exception):
    pass


class CustomError2(Exception):
    pass


def check(num):
    print('checking', num)
    if num == 0:
        raise AssertionError('Zero!')
    elif num == 1:
        raise CustomError1('One!')
    elif num == 2:
        raise CustomError2('Two!')
    elif num == 3:
        raise Exception('Three!')


def checkTryCatch(num):
    try:
        check(num)
    except AssertionError as e:
        print('Assertion error', e)
    except (CustomError1, CustomError2) as e:
        print('Custom error', e)
    except:
        print('Other error')
    else:
        print('Success')
    finally:
        print('Finally')


for i in range(5):
    checkTryCatch(i)
