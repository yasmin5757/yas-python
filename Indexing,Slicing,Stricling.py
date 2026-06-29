Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a="simple is better than complex"
a[11]+a[12]+a[13]+a[14]+a[15]+a[16]
'etter '
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'imple '
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'tter tha'
'complex'
'complex'
b="codegnan it solution"
a[12]+a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'tter tha'
b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'solution'
b[9]+b[10]
'it'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
'codegnan'
#negative indexing
a="i am learning python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]
'learni'
a[-18]+a[-17]
'am'
a[-19]
' '
b="python fullstack"
b[-5]+b[-4]+b[-3]+b[-2]+b[1]
'stacy'
b[-5]+b[-4]+b[-3]+b[-2]+b[1]
'stacy'
b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'stack'
b[-9]+b[-8]+b[-7]+b[-6]
'full'
b[-16]+b[-15]+b[-14]+b[-13]+b[-12]+b[-11]
'python'
#slicing
a="time is very precious"
a[13:21]
'precious'
a[0:4]
'time'
a[8:12]
'very'
b="work until you succed"
b[15:23]
'succed'
'succed'
'succed'
b="work until you succeed"
b[15:23]
'succeed'
b[0:4]
'work'
b[5:10]
'until'
#negative slicing
a="vizag is city of destiny"
a[-15:-12]
'cit'
a[-15:-11]
'city'
a[-7:-1]
'destin'
a[-7:]
'destiny'
a[-24:-19]
'vizag'
b="hi hello how are you"
b[-17:-12]
'hello'
b[-11:-8]
'how'
b[-20:-18]
'hi'
b[-7:-4]
'are'
b[-3:-1]
'yo'
b[-3:]
'you'
>>> #stricling
>>> a="data science"
>>> a[0:0]
''
>>> a[::2]
'dt cec'
>>> a[::5]
'dsc'
>>> b="machine learning"
>>> b[::5]
'mnag'
>>> b[::7]
'm n'
>>> a[::2]
'dt cec'
>>> b[::2]
'mcielann'
>>> b[3:11]
'hine lea'
>>> b[:8]
'machine '
>>> b[9:]
'earning'
>>> b[::4]
'miln'
>>> b[::10]
'ma'
>>> a="cloud computing"
>>> a[1:9:2]
'lu o'
>>> a[2:13:3]
'o mt'
>>> a[6:14:4]
'cu'
>>> a[5:12:2]
' opt'
>>> a[3:9:5]
'um'
