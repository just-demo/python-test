from one_three import Three
from two import two

try:
    raise Three('one')
except Three as e:
    print(e)

try:
    two()
except Three as e:
    print(e)
