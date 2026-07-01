Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="code"
b="gnan"
print(a=b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a=b)
TypeError: print() got an unexpected keyword argument 'a'
print(a+b)
codegnan
a="python"
b="course"
print(a+" "+b)
python course
fname="yasmin"
lname="s"
print(fname+lname)
yasmins
print(fname+" "+lname)
yasmin s
print(fname.title()+" "lname.title())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(fname.title()+" "+lname.title())
Yasmin S
print((fname+" "+lname).title())
Yasmin S
#formatting
a=2
b=4
print(a+b)
6
print("the sum is",a+b)
the sum is 6
city="vja"
print("the city is",city)
the city is vja
a="motu"
b="pathlu"
print("hello",a+b)
hello motupathlu
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello {} hello {}".format(a,b))
hello motu hello pathlu
#fstringmethod
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
print(f"hello {a} hello {b}")
hello sita hello ram
a="motu"
b="chotu"
print(hello",a*b)
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello"a*b)
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("hello",a*b)
      
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print("hello",a*b)
TypeError: can't multiply sequence by non-int of type 'str'
a=4
      
b=5
      
print(a*b)
      
20
c=a*b
      
print("the product is {}".format(C))
      
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("the product is {}".format(C))
NameError: name 'C' is not defined. Did you mean: 'c'?
print(the product is {}".format(c))
      
SyntaxError: unterminated string literal (detected at line 1)
print("the product is {}".format(c))
      
the product is 20
print(f"the product is {c}")
      
the product is 20
print("the product is{}".format(a*b))
      
the product is20
print(f"the product is {a*b}")
      
the product is 20
#list[]
      
a=[3,5.6,"python",9+7j,True,False]
      
print(a)
      
[3, 5.6, 'python', (9+7j), True, False]
type(a)
      
<class 'list'>
b=9
      
type(b)
      
<class 'int'>
c=[9]
      
type(c)
      
<class 'list'>
a=["python","java","c"]
      
a.append("c++")
      
a
      
['python', 'java', 'c', 'c++']
a.append("ml","ai")
      
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
      
a
      
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#extend()
      
a=["java","html","css"]
      
a.extend(["js","bs"])
      
a
      
['java', 'html', 'css', 'js', 'bs']
#insert()
      
b=["apple","banana","grapes"]
      
b.insert(1,"mango")
      
b
      
['apple', 'mango', 'banana', 'grapes']
#sort()
      
a=["kiwi","mango","apple","dragon","berry"]
      
a.sort()
      
a
      
['apple', 'berry', 'dragon', 'kiwi', 'mango']
b=[9,6,3,0,2,4,20]
      
b.sort()
      
b
      
[0, 2, 3, 4, 6, 9, 20]
#reverse
      
a=["c","java","html","css"]
      
a.reverse()
      
a
      
['css', 'html', 'java', 'c']
b=[9,10,12,14,15]
      
b.reverse()
      
b
      
[15, 14, 12, 10, 9]
#pop()
      
a=["black","white","red","blue","pink"]
      
a.pop()
      
'pink'
a
      
['black', 'white', 'red', 'blue']
a.pop(2)
      
'red'
a
      
['black', 'white', 'blue']
a.pop("white")
      
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.pop("white")
TypeError: 'str' object cannot be interpreted as an integer
a.remove("white")
      
a
      
['black', 'blue']
#copy&clear
      
a=["pooja","yasmin","ashru","abu"]
...       
>>> a.copy()
...       
['pooja', 'yasmin', 'ashru', 'abu']
>>> b=a.copy()
...       
>>> b
...       
['pooja', 'yasmin', 'ashru', 'abu']
>>> a.clear()
...       
>>> a
...       
[]
>>> b=[]
...       
>>> b.append("hi")
...       
>>> b
...       
['hi']
>>> a=["hi","hello","how"]
...       
>>> len(a)
...       
3
>>> b="hello"
...       
>>> len(b)
...       
5
>>> c=["hello"]
...       
>>> len(c)
...       
1
>>> a.count("hello")
...       
1
