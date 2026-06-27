Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
type(a)
<class 'int'>
>>> b=5.6
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="python"
>>> type(d)
<class 'str'>
>>> e='''codegnan'''
>>> type(e)
<class 'str'>
>>> f=5+9j
>>> type(f)
<class 'complex'>
>>> g=4j=7
SyntaxError: cannot assign to literal
>>> g=4j+7
>>> type(g)
<class 'complex'>
>>> h=3j
>>> type(h)
<class 'complex'>
>>> a=3+7i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c=true
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> d="true"
>>> type(d)
<class 'str'>
