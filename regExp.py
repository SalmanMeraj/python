import re
from re import match

file=open('communicate.txt')

for line in file:
    if re.search( '(communicate|emot)ions', line):
        print (line)
print()       
## find out where we can get only emotion 

file=open('communicate.txt')

for line in file:
    if re.search( 'conscious', line):
        print(line)
print()
file=open('communicate.txt')

for line in file:
    if re.search('email', line):
        print(line)
        
## if we want to match any string then we need to write code like following 
pattern = r"Bangla"

result = re.match(pattern, "Bangladesh")

if result:
    print("Match Found!")
else:
    print("No match")
## match example

passion='python'

developer=re.match(passion, "pythonProgramming")

if developer:
    print("Python is easy")
else:
    print("Java is better")
    
##match 

android="Java"
dataScience="Python"

appdev=re.match(android, "Android-app-development-Java")
analytics=re.match(dataScience, 'Python-data-analysis')

if appdev:
    print("Java is best for mobile app development")
else:
    print('none')
    
if analytics:
    print('Python is getting popular for data mining')
else:
    print("none")
## python search option 
# we wwould like to find a single word inside our written text instead of file 

love=r"Country"

find=re.search(love, "I love my Country")

if find:
    print("Yes!")
else:
    print("Oh! no")
    
## search example
nation='Bangla'

country=re.search(nation, "My country name is Bangladesh. It is near India")

if country:
    print("I love my country")
else:
    print('none')
# we can do it in a shorter way like below
win='Schumachar'

if re.search(win, "In 1994 & 95 Schumachar won the F1 world championship"):
    print('He was the Champ')

else:
    print('none')
##search 

language="bangla"

differ='There is a difference between Bangladeshi people speaks in bangla & wets bengal people talk bangla'
if re.search(language, differ):
    print('Bangla is mathced')
    
else:
    print('none')
    
print(re.findall(language, differ,))

## returen method caracter 

nice="bin"

find=re.search(nice, "combination")

if find:
    print(find.group())
    print(find.start())
    print(find.end())
    print(find.span())
else:
    print('none')
    
## meta character 

g='gr.|.y'

if re.match(g, "gravy"):
    print("It's gravy")
if re.match(g, "gray"):
    print("Thi si gray")  
if re.match(g, "grey"):
    print('thi is grey')
if re.match(g, "Gray"):
    print("Match")
## meta character to find out the start & end of the character 

t="^wr.te$"

if re.match(t, "written"):
    print("written")
if re.match(t, "write"):
    print("write")
if re.match(t, "wrote"):
    print('wrote')
    
if re.match(t, "Write"):
    print('Write')

# tr agin
u='^To.|.to$'
if re.match(u, "Tomato"):
    print("Thi is Tomato")
if re.match(u, "Zomato"):
    print("Zomato")

## try again 
u='^To.to$'
if re.search(u, "Tomato"):
    print("Thi is Tomato")
if re.search(u, "Zomato"):
    print("Zomato")
    
## character class

# checking the vowel

v='[aeiou]'

if re.search(v, "UMbrella"):
    print("There is vowel in this word")
else:
    print("No vowel matched")

if re.search(v, "Ortega"):
    print("We found the vowel")

if re.match(v, "Tomato"):
    print("Vowel iside Tomato")
else:
    print("No vowel in tomato")

if re.search(v, "rhythm sngs"):
    print('vowel in rhythm')
else: 
    print('Rhythm')

## range in character 

rnge="[A-Z]"

if re.search(rnge,"you can put XBOX over here"):
    print("iOK")
if re.search(rnge, "XB is here"):
    print("it's ok to be matched")
if re.search(rnge, "we dont have it"):
    print("ok")
else:
    print('not ok')

rhge="[a-z][A-Z][0-9]"

if re.search(rhge, "this is it"):
    print("lower case")
if re.search(rhge, "NS1 is not"):
    print('we found uper & lower case & number')
else:
    print('not ok')

tango="[A-Z][A-Z][A-Z][a-z][0-9]"
if re.search(tango, "DHLf1 is the official sponsor"):
    print("DHL services")
if re.search(tango, "DHL is the official sopnsor"):
    print("DHL")
else:
    print("Fedex")
    
## uses of ^ inside the character classes

tmz="[^A-Z]"

if re.search(tmz, "A handful flowers"):
    print("FLOWERS")
else:
    print("Not match")
if re.search(tmz, "FLOWERS"):
    print("ROSE")
else:
    print("rose")
if re.search(tmz, "HAND OF GOD"):
    print("Maradona")
else:
    print("Argentina")
    
##v group Character 

grp=r"MD(Hassan)*"

if re.match(grp, "MD Meraj Ul Hassan"):
    print("First & Last name")
if re.match(grp, "MDHassan"):
    print("Yes!")
if re.match(grp, "MD Hassan"):
    print("Match 2")
if re.match(grp, "md hassan"):
    print("md hassan")
else:
    print('none')
#findall
if re.findall(grp, "MD Meraj Ul Hassan"):
    print('Match 1')

if re.findall(grp, "MD Hassan"):
    print('Match 2x')
    
if re.findall(grp, "md hassan"):
    print('Mathc 3')
else:
    print('no match')
## search
if re.search(grp, "MD Meraj Ul Hassan"):
    print('MD Meraj Ul Hassan')

## accessing the index by using group()

grp1="a(b)(cd)(e(f)g)h" 

mat=re.match(grp1, "abcdefghijkl")

if mat:
    print(mat.group())
    print(mat.group(0))
    print(mat.group(1))
    print(mat.group(2))
    print(mat.group(3))
    print(mat.group(4))
    
    print(mat.groups())
    
## Or | meta character 

bypass=r"Ma|exx"

if re.match(bypass, 'Massachessete'):
    print("It's ok")
if re.match(bypass, 'exxgf'):
    print('ok')
else:
    print('not ok')

wrd='wr(i|o)te'

if re.match(wrd, "write"):
    print('He write')
if re.match(wrd, "wrote"):
    print('He wrote')
if re.match(wrd, "written"):
    print('written')
else: 
    print('she wrote')

wrd='wr.|.te'

if re.match(wrd, 'write'):
    print('write')
if re.match(wrd, 'wrmte'):
    print('wrmte')
else:
    print('wrd wrong')

# special sequence

spsq=r"(.+) \1"

seq=re.match(spsq, "md md")

if seq:
    print('md')
else:
    print('not md')

sp=r'(.+) \1'

if re.match(sp, "1st 1st"):
    print('first')
if re.match(sp, "by by"):
    print('byby')
if re.match(sp, 'cow cat'):
    print('cow & cat')
else: 
    print('cow')
    
    
## check digit 

digit=r'(\d)'

if re.match(digit, "12th"):
    print('12th')
else:
    print('not digit')
if re.match(digit, "1456"):
    print('number')
if re.match(digit, "th5"):
    print('alphaneumeric')
else:
    print('none')
    
## space 

space=r'(\s)'

if re.search(space, "Md Meraj Ul Hassan"):
    print('there is space')
if re.search(space, "merajhassan"):
    print('no space')
else:
    print('space 02')

## inverse spciale character 

Dd=r'(\D+\d)'

if re.match(Dd, "F 16"):
    print("F-16 get plane")
if re.match(Dd, 'f16'):
    print('f16 get')
if re.match(Dd, 'Hyper 22x'):
    print('HYper 22x')
if re.match(Dd, '1, 23, 25600'):
    print('only number')
else: 

## checking the bundary of any string 
    def Hola(firstname):
        print('Hello '+firstname)
first_name=input("What is your First Name? ")
Hola(first_name)