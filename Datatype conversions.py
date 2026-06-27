Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatype conversions
>>> #int()
>>> int(9)
9
>>> int(8.9)
8
>>> int("yasmin")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("yasmin")
ValueError: invalid literal for int() with base 10: 'yasmin'
>>> int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(3.9)
3.9
>>> float("yasmin")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    float("yasmin")
ValueError: could not convert string to float: 'yasmin'
>>> float(9.8)
9.8
>>> str('python")
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> str("python")
...     
'python'
>>> str('python)
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> str('python')
...     
'python'
str('''codegnan''')
    
'codegnan'
float(True)
    
1.0
float(False)
    
0.0
str(True)
    
'True'
str(False)
    
'False'
str("hi")
    
'hi'
str(5.6)
    
'5.6'
str(6+9j)
    
'(6+9j)'
#complex
    
complex(7)
    
(7+0j)
complex(7.8)
    
(7.8+0j)
complex("hello")
    
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
#bool
    
bool(5)
    
True
bool(8.9)
    
True
bool("java")
    
True
bool(5+9j)
    
True
bool(True)
    
True
bool(False)
    
False
