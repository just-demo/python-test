def test(param):
    print(param + ' __name__ is ' + __name__)


if __name__ == '__main__':
    test('imported')

test('imported')
print('imported __name__ is ' + __name__)
