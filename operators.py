Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
#assignment
a=3
b=5
a+b
8
a+=b
a
8
a
8
a-=2
a
6
a+=b
b
5
b
5
b-=2
b
3
a**=4
a
14641
a**=4
a
45949729863572161
45949729863572161
45949729863572161
#comparision
a=4
b=8
a<b
True
a>b
False
b>a
True
b<a
False
a!=b
True
a==b
False
a<=b
True
True
True
#logical
a=5
b=7
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or a<=b
True
a>=b or a<=b
True
a!=b or a==b
True
True
True
a<b or b>a
True
a>=b or a<=b
True
#identify
a=4
type(a) is int
True
type(a) is not int
False
a=5.6
type(a) is float
True
type(a) is not float
False
type(a) is str
False
type(a) is not str
True
a="python"
type(a) is str
True
a=5
b=3
type(a=b) is bool
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    type(a=b) is bool
TypeError: type() takes 1 or 3 arguments
a=4
type(a) is bool
False
#membership
a=3,4,5,6,7,8,9,10
8 in a
True
20 in a
False
20 not in a
True
#bitwise
#bitwise
a=2
b=4
a&b
0
a=5
b=7
a&b
5
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
bin(7)
'0b111'
a=3
b=5
a|b
7
a=4
b=8
a|b
12
>>> a=2
>>> -(a+1)
-3
>>> ~a
-3
>>> a=5
>>> ~a
-6
>>> a=9
>>> ~a
-10
>>> b=-11
>>> ~b
10
>>> c=-15
>>> ~c
14
>>> a=6
>>> b=9
>>> a^b
15
>>> a=5
>>> b=7
>>> a^b
2
>>> 2
2
>>> a=3
>>> a<<2
12
>>> a=5
>>> a<<3
40
>>> a=4
>>> a>>2
1
>>> a=9
>>> a>>3
1
