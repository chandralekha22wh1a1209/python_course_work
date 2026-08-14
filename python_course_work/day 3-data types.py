Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
count = 10
>>> price
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    price
NameError: name 'price' is not defined. Did you mean: 'print'?
>>> price = 99.99
>>> price
99.99
>>> type(price)
<class 'float'>
>>> c = 3+8j
>>> c
(3+8j)
>>> type(c)
<class 'complex'>
>>> s = 'codegnan'
>>> type(s)
<class 'str'>
>>> l = list[]
SyntaxError: invalid syntax
>>> l = list()
>>> l = [1, 2, 3. 'code', [1,2,3]]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> l =  [1, 2, 3, 'code', [1,2,3]]
>>> print(l)
[1, 2, 3, 'code', [1, 2, 3]]
>>> type(l)
<class 'list'>
>>> type(s)
<class 'str'>
>>> s={'name':'chandra','batch':63,'course':'PFS'}
>>> s
{'name': 'chandra', 'batch': 63, 'course': 'PFS'}
>>> status = True
>>> type(status)
<class 'bool'>
>>> status = None
>>> types(status)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    types(status)
NameError: name 'types' is not defined. Did you mean: 'type'? Or did you forget to import 'types'?
>>> type(status)
<class 'NoneType'>
>>> s.add(6)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.add(6)
AttributeError: 'dict' object has no attribute 'add'
>>> s =[1,2,3,4,5]
>>> s.add(6)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.add(6)
AttributeError: 'list' object has no attribute 'add'
>>> s = {1,2,3,4,5}
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.remove(2)
>>> s
{1, 3, 4, 5, 6}
>>> s = frozenset([1,2,3,4})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s = frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
