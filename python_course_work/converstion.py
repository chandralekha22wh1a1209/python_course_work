Python 3.14.6 (v3.14.6:c63aec69bd5, Jun 10 2026, 08:07:54) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> float(a)
10.0
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> bool(0)
False
