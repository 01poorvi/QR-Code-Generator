#day1:-
'''
a,b=input('Enter a number for a and b:-').split('@')
c=int(a)+int(b)
print(c)
'''
# how to exclude spaces in the given string using len function indexing.
'''
a=input("Enter a string:-")
print(len(a)-a.count(' '))
'''
#decision control methods
'''
if
else
elif
'''
'''
age=int(input('Enter your age:-'))
if age>0 and age<=4:
    print('Ticket Charges:- 0 rs')
elif age>4 and age<=14:
    print('Ticket Charges:- 30 rs')
elif age>14 and age<=45:
    print('Ticket Charges:- 50 rs')
elif age>45 and age<=59:
    print('Ticket Charges:- 70 rs')
else:
    print('Ticket Charges:- 0 rs')
'''
#day2:-
'''
name=input('Enter your name:-')
age=int(input('Enter your age:-'))
#if name=='Chetan' and age==31:
#if age==31 and (name.lower() or name.upper()):
if age==31 and (name[0]=="c" or name[0]=="C"):
    print("present")
else:
    print("not present")
'''
#STRING FORMATTING:-
'''
a,b=input("Enter the value of a and b:-").split(',')
c=int(a)+int(b)
#according to python 2 version
print('value of a is '+a+' and value of b is '+b+' then sum is '+str(c))

#according to python 3 version
print('value of a is {} and value of b is {} then sum is {}'.format(a,b,c))

#according to python 3.6 version
print(f'value of a is {a} and value of b is {b} then sum if {c}')
'''
#LOOPS:-
#while:- is used for infinite times
'''ctrl c is used to exit the infinite loops only in idle. it causes keyboard intruption'''
'''
i=0
while i<=9:
    print('Noopur')
    i+=1
'''
'''
i=1
sum=0
mul=1
while i<=10:
    print(i)
    sum=sum+i
    mul=mul*i
    avg=sum/10
    i+=1
print(avg)
print(sum)
print(mul)
'''
'''
n=int(input("Enter your range:-"))
i=1
sum=0
mul=1
while i<=n:
    print(i)
    sum=sum+i
    mul=mul*i
    avg=sum/n
    i+=1
print(avg)
print(sum)
print(mul)
'''
#for:- is used with range function
'''
for i in range(1,11):
    print(i)
'''
#print sum of even numbers
'''
sum=0
for i in range(1,11):
    if i%2==0:
        print(i)
        sum=sum+i
print("sum:-",sum)
'''
#game- Guess the number
'''
win_num=45
num=int(input("Enter your number:-"))
Game_over=False
while not Game_over:
    if num==win_num:
        print("You Won!!!!")
        Game_over=True
    else:
        if num<win_num:
            print("Too Low!!")
            num=int(input("Enter your number again:-"))
        else:
            print("Too High!!")
            num=int(input("Enter your number again:-"))
'''

#FUNCTIONS:-
'''
-->USER DEFINED:- Fumction with arguments
                  Function wothout arguments
'''
#without arguments
'''
def add():
    a=6
    b=8
    return a+b
print(add())


def add():
    a=6
    b=8
    print(a+b)
add()
'''
#with arguments
'''
def add(a,b):
    return a+b
num=2
num1=8
print(add(num,num1))
'''
#day3:-
'''
i=1
sum=0
while i<=10:
    if i%2==0:
        print(i)
        sum=sum+i
    i+=1
print("sum=",sum)
'''
#without argument
'''
def even():
    i=1
    sum=0
    while i<=10:
        if i%2==0:
            print(i)
            sum=sum+i
        i+=1
    print('sum=',sum)
even()
'''
#with argument
'''
def even(n):
    i=1
    sum=0
    while i<=n:
        if i%2==0:
            print(i)
            sum=sum+i
        i+=1
    print('sum=',sum)
even(n)
'''
#with user input
'''
n=int(input("Enter the range:-"))
def even(n):
    i=1
    sum=0
    while i<=n:
        if i%2==0:
            print(i)
            sum=sum+i
        i+=1
    print('sum=',sum)
even(n)
'''
#pallindrome
'''
n=input("Enter a Value:-")
def pallindrom(n):
    rev_str=n[::-1]
    if (n==rev_str):
        print("the number is pallindrome")
    else:
        print("the number is not pallindrome")
pallindrom(n)
'''
#even odd number
'''
n=int(input("Enter the value:-"))
def num(n):
    if n%2==0:
        print("The number is even")
    else:
        print("The number is odd")
num(n)
'''
#DATABASE TYPES:-
#-->List--> unordered database, all type of data store(str,int,mix), denotes with []
'''
fruits=['mango','kiwi','banana']
print(fruits,type(fruits))
'''
#how to add data to list
'''
1- append
2- insert
'''
'''
fruits.append('watermelon')
print(fruits)
'''
'''
fruits.insert(2,'apple')
print(fruits)
'''
#how to remove data from the list
'''
1- pop
2- remove
'''
'''
fruits.pop()
print(fruits)
'''
'''
fruits.remove('banana')
print(fruits)
'''
#use of extend command in list
'''
l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
'''
#day4:-

#use of list command in list itself-->use only with range function

'''
num=list(range(1,11))
print(num,type(num))
'''
'''
num=list(range(1,11))
print(num)
even=[]
for i in num:
    if i%2==0:
        even.append(i)
print(even)
'''
'''
num=list(range(1,11))
print(num)
neg=[]
for i in num:
    neg.append(-i)
print(neg)
'''
'''
num=list(range(1,11))
print(num)
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i**2)
    else:
      odd.append(-i)
print(even)
print(odd)
'''
'''
list=['chetan','Anuj','Mohit']
rev=list[::-1]
print(rev)
r=[]
for i in list:
    r.append(i[::-1])
print(r)
'''
#use of split command-->it is used to convert string into list.
'''
user=input('Enter your string:-').split(' ')
text=input('Enter your string:-').split(' ')
new=user+text
print(new)
'''
'''
name,age='chetan,31'.split(',')
print(name)
print(age)
'''
#use of join command--> used to convert list into string
'''
user=['chetan','31']
print(','.join(user))
'''
#-->Tuple-->used in data security bcoz it is im-mutable,denoted with ().
'''
num=(1,2,3,4,5,6,7,8,9,10)
print(num,type(num))

new=(1,)
print(new,type(new))

user='chetan','mohit','anuj'
print(user,type(user))

name1,name2,name3=user
print(name1)
print(name2)

name_info=('chetan','31',['book1','book2'])
name_info[2].append('book3')
print(name_info)

name_info[2].insert(2,'book4')
print(name_info)
'''
#-->Dictionary-->unordered database,all types of data can stored, data is stored in the form of keys and values pairs,it is denoted by {}.
#how to define a dictionary
'''
user={'name':'chetan','age':31}
print(user,type(user))

user1=dict(name='chetan',age=31)
print(user1,type(user1))

user_info={
    'name':'chetan',
    'age':31
    }
print(user_info,type(user_info))
'''
#how to add data to dictionary
'''
d={}
d['name']='chetan'
d['age']=31
print(d)
'''

#how to apply if and else in dictionary
'''
user1={'name':'chetan','age':31}
'''
#cheking the keys
'''
if 'name' in user1:
    print("present")
else:
    print("not present")
'''
#cheking the values-->use value method
'''
if 'chetan' in user1.values():
    print("present")
else:
    print("not present")
'''
#day5:-

#use of items method-->used for checking values and keys both.
'''
user={'name':'chetan','age':31}
print(user,type(user))
if('name','chetan')in user.items():
    print('present')
else:
    print('not present')
''' 
#suppose-
'''
user={'name':'chetan','age':31}
print(user,type(user))
if('chetan','name')in user.items(): #keys and values are interchanged so output will be not present.
    print('present')
else:
    print('not present')
'''
#how to apply loops in dictionaries
'''
user={'name':'chetan','age':31}
for i in user: #loops by default extract keys in dictionaries 
    print(i)
'''
#use of keys method
'''
user={'name':'chetan','age':31}
for i in user.keys(): #we can skip keys method bcoz it is accesed by default in dictionaries
    print(i)
'''

#use of values method
'''
user={'name':'chetan','age':31}
for i in user.values(): #used to access values in dictionaries
    print(i)
'''
#use of items method-->used to access keys and values both
'''
user={'name':'chetan','age':31}
for i,j in user.items():
    print(f'{i}:{j}')
'''
#suppose
'''
user={'name':'chetan','age':31}
for i in user.items(): #gives the output in tuple which means we cannot modify the data
    print(i)
'''
#how to apply function in dictionaries
'''
def to_square(l):
    d={}
    for i in range(1,l+1):
        d[i]=i**2
    return d
print(to_square(10))
'''
'''
def word_count(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_count('noopur'))
'''
# use of comprehension command-->list
'''
num=list(range(1,11))
print(num)
new=[]
for i in num:
    new.append(i**2)
print(new)
square=[i**2 for i in range(1,11)]
print(square)
'''
#for 1 condition
'''
num=list(range(1,11))
print(num)
new=[]
for i in num:
    if i%2==0:
        new.append(i**2)
print(new)
square=[i**2 for i in range(1,11) if i%2==0]
print(square)
'''
#for 2 conditions
'''
num=list(range(1,11))
print(num)
new=[]
for i in num:
    if i%2==0:
        new.append(i**2)
    else:
        new.append(-i)
print(new)
square=[i**2 if i%2==0 else -i for i in range(1,11)]
print(square)
'''
#comprehension command in dictionaries
'''
def to_square(l):
    d={}
    for i in range(1,l+1):
        d[i]=i**2
    return d
print(to_square(10))
square={n:n**2 for n in range(1,11)}
print(square)
'''
#args--> * operator
'''
def add(a,b):
    return a+b
print(add(2,3)) #what if we give 3 no.? it will show type error. Then we use args, they convert all the data in tuple.
'''
'''
def add(*args):
    return args
print(add(1,2,3,4,5,6,7,8,9))
'''
'''
def add(*args):
    print(args)
    total=0
    for i in args:
        total+=i
    return total
print(add(1,2,3,4,5,6,7,8,9))
'''
'''
def add(*args):
    print(args)
    total=0
    for i in args:
        total+=i
    return total
n=int(input('Enter your range:-'))
num=list(range(1,n+1))
print(add(*num)) # we cannot pass list without * operator
'''
#args with normal parameter
'''
def total(n,n1,*args):
    print(args)
    print(n)
    print(n1)
total(1,2,3,4,5,6)
'''
#kwargs--> ** operator, always returns data in the form of dictionary
'''
def fun(**kwargs):
    return kwargs
print(fun(name='noopur',age=21))
'''
#lambda function--> logic- lambda variable:operation
'''
add=lambda a,b:a+b
print(add)#it shows hex code of the memory location of the code
'''
'''
add=lambda a,b:a+b
print(add(1,4))
'''
'''
squares= lambda a:a**2
print(squares(5))
'''
#map function--> it is used to show mapping location of the data, syntax- map(funtion, input)
'''
num=[1,2,3,4,5,6]
def square(a):
    return a**2
print(list(map(square,num)))
'''
#using lambda function
'''
num=[1,2,3,4,5,6]
def square(a):
    return a**2
print(list(map(lambda a:a**2,num)))
'''

#day6:-

#filter function-->only used to filter the data-->gives filter location, we need to typecaste the data. this will only execute even odd function bco it is filtered function.
'''
n=[1,2,3,4,5]
def square(a):
    return a%2==0
print(filter(square,n))#gives filter location
print(list(filter(square,n)))#typecaste the data
print(list(filter(lambda a:a%2==0,n)))#use of lambda function in filter function
print(list(filter(lambda a:"Even" if a%2==0 else "Odd",n)))#this will only show the list, it will only perform filter function not any other task.
'''
#Zip function--> zips two or more than two data.
'''
l1=[1,2,3]
l2=[4,5,6]
print(zip(l1,l2))#gives zip location of the data, we need to typecast the data
print(list(zip(l1,l2)))
'''
'''
user=['user_id1','user_id2','user_id3']
name=['chetan','anuj','mohit']
print(list(zip(user,name)))
print(tuple(zip(user,name)))
print(dict(zip(user,name)))#dictionary will only work for keys and values, no third data is applicable in dictionary. in that condition dict function will fail.
'''
#question:- l1=[1,2,3] l2=[4,5,6] output=[(1+4)/2,(2+5)/2,(3+6)/2]
'''
l1=[1,2,3]
l2=[4,5,6]
def average(l1,l2):
    ave=[]
    for pair in zip(l1,l2):
        ave.append(sum(pair)/len(pair))
    return ave
print(average(l1,l2))
'''
#Break,continue,pass command-->
#break:-
'''
for i in range(1,11):
    if i==5:
        break #terminates the logic, stops the code when condition is satisfied.
    print(i)
'''
#continue:-
'''
for i in range(1,11):
    if i==5:
        continue #skips the condition and continuw the logic.
    print(i)
'''
#pass:-
'''
for i in range(1,11):
    if i==5:
        pass #to bypass any condition
    print(i)
'''
#Function returning Function:-
#without argument
'''
def outer():
    def inner():
        print("hello i am function 1")
    return inner()
outer()
'''
#with argument
'''
def outer(msg):
    def inner():
        print(f"hello i just wonna say that {msg}")
    return inner()
outer("hi")
'''
#decorator-->enhance the functionality of other function, decorators are usually called by @.
#original decorator
'''
def decorator(any):
    def wrapper():
        print("I'm calling main function")
        any()
    return wrapper
@decorator
def func1():
    print("This is function 1")
@decorator
def func2():
    print("This is function 2")
func1()
func2()
'''
#work as decorator
'''
def decorator(any):
    def wrapper(*args,**kwargs):
        print("I'm calling main function")
        return any(*args,**kwargs)
    return wrapper

def func1():
    print("This is function 1")

def func2():
    print("This is function 2")
var=decorator(func1)
var
var=decorator(func2)
var

@decorator
def add(a,b):
    return a+b
print(add(2,3))
'''
#day7:-

#OOPS:- Object Oriented Programming System,create class with __init__ method using self command

#-->How to create class and variables
'''
class person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.full_name=fname+" "+lname
    def fullname(self):
        return f'{self.fname} {self.lname}'
p1=person('noopur','verma',21) #p1 is an object
p2=person('priyanshi','maurya',21) #p2 is an object
print(p1.fullname())
print(p1.full_name)
print(p1.fname)
print(p1.lname)
print(p1.age)
print(person.fullname(p2))
'''
#program:-
'''
class laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def brand_name(self):
        return f'{self.brand} {self.model}'
    def discount(self,n):
        off_price=(n/100)*self.price
        return self.price - off_price
l1=laptop('HP','xtu456',56000)
l2=laptop('DELL','xut326',48000)
print(l1.brand_name())
print(l1.discount(10))
'''
#same program with user input
'''
class laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def brand_name(self):
        return f'{self.brand} {self.model}'
    def discount(self,n): #n works as local variable here
        off_price=(n/100)*self.price
        return self.price - off_price
n=int(input("Enter the discount percent:-"))
l1=laptop('HP','xtu456',56000)
l2=laptop('DELL','xut326',48000)
print(l1.brand_name())
print(l1.discount(n))
'''
#same program with class variable technique
'''
class laptop:
    #n=30 #class variable
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def brand_name(self):
        return f'{self.brand} {self.model}'
    def discount(self): #n works as local variable here
        off_price=(laptop.n/100)*self.price
        return self.price - off_price
n=int(input("Enter discount:-")) #global variable
l1=laptop('HP','xtu456',56000)
l2=laptop('DELL','xut326',48000)
print(l1.brand_name())
print(l1.discount())
'''
#instance count-->counts number of instances present in a class
'''
class laptop:
    count_instance=0
    #n=30---  class variable
    def __init__(self,brand,model,price):
        laptop.count_instance+=1
        self.brand=brand
        self.model=model
        self.price=price
    @classmethod #in case of decorators we can not pass self
    def instance_count(cls):
        return f' you have created {cls.count_instance} instance of laptop class'
l1=laptop('HP','xtu456',56000)
l2=laptop('DELL','xut326',48000)
l3=laptop('DELL','567',70000)
print(laptop.instance_count())
'''
#inheritance
'''
class phone: #base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
class smart_phone(phone): #child class
    def __init__(self,brand,model,price,ram,internal_memory):
        phone.__init__(self,brand,model,price)
        self.ram=ram
        self.internal_memory=internal_memory
p1=phone('nokia','1100',1000)
p2=smart_phone('oneplus','5',30000,'6GB','64GB')
print(p2.full_name())
'''
#day8:-
#super class method
'''
class phone: #base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
class smart_phone(phone): #child class
    def __init__(self,brand,model,price,ram,internal_memory):
        super().__init__(brand,model,price)
        #phone.__init__(self,brand,model,price)
        self.ram=ram
        self.internal_memory=internal_memory
p1=phone('nokia','1100',1000)
p2=smart_phone('oneplus','5',30000,'6GB','64GB')
print(p2.full_name())
'''
#multi inheritance
'''
class phone: #base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
class smart_phone(phone): #child class
    def __init__(self,brand,model,price,ram,internal_memory):
        super().__init__(brand,model,price)
        #phone.__init__(self,brand,model,price)
        self.ram=ram
        self.internal_memory=internal_memory
class super_smart_phone(smart_phone):
    def __init__(self,brand,model,price,ram,internal_memory,camera):
        smart_phone.__init__(self,brand,model,price,ram,internal_memory)
        self.camera=camera
p1=phone('nokia','1100',1000)
p2=smart_phone('oneplus','5',30000,'6GB','64GB')
p3=super_smart_phone('MI','11S',30000,'12GB','1TB','150MPX')
print(p3.full_name())
'''
#function overloading
'''
class phone: #base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
class smart_phone(phone): #child class
    def __init__(self,brand,model,price,ram,internal_memory):
        super().__init__(brand,model,price)
        #phone.__init__(self,brand,model,price)
        self.ram=ram
        self.internal_memory=internal_memory
    def full_name(self):
        return f'{self.brand} {self.model} {self.price}'
class super_smart_phone(smart_phone):
    def __init__(self,brand,model,price,ram,internal_memory,camera):
        smart_phone.__init__(self,brand,model,price,ram,internal_memory)
        self.camera=camera
p1=phone('nokia','1100',1000)
p2=smart_phone('oneplus','5',30000,'6GB','64GB')
p3=super_smart_phone('MI','11S',30000,'12GB','1TB','150MPX')
print(p1.full_name())
print(p2.full_name())
print(p3.full_name())
'''
#encapsulation
#name mangling-->use '_'
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self._price=price
        self.full_speci=brand+' '+model+' '+str(price)
    def full_name(self):
        return f'{self.brand} {self.model}'
p1=phone('nokia','1100',1000)
p1._price=500
print(p1.full_speci)
print(p1.brand)
print(p1.model)
print(p1._price)
'''
#use of '__'
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.__price=price
        #self.full_speci=brand+' '+model+' '+str(price)
    def full_name(self):
        return f'{self.brand} {self.model} and price {self.__price}'
p1=phone('nokia','1100',1000)
#p1.__price=500
print(p1.brand)
print(p1.model)
print(p1._phone__price)
print(p1.full_name())
print(p1.__dict__)
'''
#what if we update a negative value then the output will always be 0
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        if price>0:
            self.__price=price
        else:
            self.__price=0
        #self.full_speci=brand+' '+model+' '+str(price)
    def full_name(self):
        return f'{self.brand} {self.model} and price {self.__price}'
p1=phone('nokia','1100',-1000)
#p1.__price=500
print(p1.brand)
print(p1.model)
print(p1._phone__price)
print(p1.full_name())
print(p1.__dict__)
'''
#day9:-
#special magic method/dunder method
#__str__ method--> it picks by defalut str even if str nd repr are borth present-->string
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
    def __str__(self):
        return f'{self.brand} {self.model}'
p1=phone('nokia','1100',1000)
print(p1)
'''
#__repr__ method--> its original work is to return objectof the class-->representation
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
    def __repr__(self):
        return f'{self.brand} {self.model} and price is {self.price}'
p1=phone('nokia','1100',1000)
print(p1)
'''
#for both print
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
    def __str__(self):
        return f'{self.brand} {self.model}'
    def __repr__(self):
        return f'{self.brand} {self.model} and price is {self.price}'
p1=phone('nokia','1100',1000)
print(str(p1))
print(repr(p1))
'''
#how to create a object through __repr__
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.price}'
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'
    def __repr__(self):
        return f'phone({self.brand} {self.model} {self.price})'
p1=phone('nokia','1100',1000)
print(str(p1))
print(p1.__repr__())
'''
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.price}'
    def __str__(self):
        return f'phone({self.brand} {self.model} {self.price})'
    def __repr__(self):
        return f'phone(\'{self.brand}\',\'{self.model}\',{self.price})'
p1=phone('nokia','1100',1000)
print(str(p1))
print(p1.__repr__())
'''
#__len__ method
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.price}'
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'
    def __repr__(self):
        return f'phone(\'{self.brand}\',\'{self.model}\',{self.price})'
    def __len__(self):
        return len(self.__str__())
p1=phone('nokia','1100',1000)
print(str(p1))
print(p1.__repr__())
print(len(p1))
'''
#operator overloading
'''
class phone: 
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def full_name(self):
        return f'{self.brand} {self.model}'
    def __str__(self):
        return f'{self.brand} {self.model}'
    def __repr__(self):
        return f'{self.brand} {self.model} and price is {self.price}'
    def __add__(self,other):
        return self.price+other.price
p1=phone('nokia','1100',1000)
p2=phone('nokia','1100',1000)
print(str(p1))
print(p1.__repr__())
print(p1+p2)
'''
#day10:-

#error--> three types of errors. 1- built in error, 2- exception,how to handle them and 3- raise your own error.
#1- syntax error--> when we accidently make mistakes in code.
#2- indentation error--> when we make mistake in indentation(spaces) of code.
#3- name error--> when we make a variable which we have not defined.
#4- type error--> when we make mistake in datatypes. like: adding and string to integer.
#5- index error--> when we make mistake in indexing values.
#6- value error--> when we make mistake in calling or printing the datatype. like: print(int(s)) but s is an string.
#7- attribute error--> when we use a command which is not available for that object.
#8- key error--> mostly in dictionary, when we call a key which is not present in the dictionary.

#raise command--> we use raise command to create our own error
'''
def add(a,b):
    if(type(a) is int and type(b) is int):
        return a+b
    #return 'you have entered the wrong datatype'
    raise TypeError('you have entered the wrong datatype')
print(add(2,3))
print(add('2',7))
'''
#error handling:-
'''
age=int(input("enter your age:-"))
if age<18:
    print("you cannot play the game")
else:
    print("you can play the game")#what if we input string to age, to handle these errors we use try and except command and only satisfy when loop is infinite.
''' 
#try and except command:-
'''
while True:
    try:
        age=int(input("enter your age:-"))
        break
    except ValueError:
        print("try again")
if age<18:
    print("you cannot play the game")
else:
    print("you can play the game")
'''
#finally command:-
'''
while True:
    try:
        age=int(input("enter your age:-"))
        break
    except ValueError:
        print("try again")
    finally:
        print("you have entered the correct data")
if age<18:
    print("you cannot play the game")
else:
    print("you can play the game")
'''
'''
while True:
    try:
        age=int(input("enter your age:-"))
        break
    except:
        raise ValueError("try again") #if we raise error then it will end the infinite loop
    finally:
        print("you have entered the correct data")
if age<18:
    print("you cannot play the game")
else:
    print("you can play the game")
'''
#file handling:-
#text,excel,csv,pdf
#open()
#file read
#read()
#seek()
#tell()
#readline()
#readines()
#with open
#close()

#1st method-->when code and text file are in same location.
'''
f=open('test.txt')
print(f.read())
f.close()
'''
#2nd method--> when code and text file have diffrent location.
'''
f=open('python\\test.txt')
f=open(r'file loaction with '\' everywhere\test.txt') #if we want to read our file with single \ use r.
print(f.read())
f.close()
'''
#tell command-->reads the cursor position of the file
'''
f=open(r'python\test.txt')
print(f.tell())
print(f.read())
print(f.tell())
f.close()
'''

#day11:-

#seek command--> reset the cursor position
'''
f=open(r'python\test.txt')
print(f'cursor position befor:{f.tell()}')
print('\n')
print(f.read())
print('\n')
print(f'cursor position after:{f.tell()}')
f.seek(5) # the no. we give means the cursor will read the text from that index.
print(f.read())
f.close()
'''
'''
f=open(r'python\test.txt')
print(f'cursor position befor:{f.tell()}')
print('\n')
print(f.read())
print('\n')
print(f'cursor position after:{f.tell()}')
f.seek(5) # the no. we give means the cursor will read the text from that index.
print(f'cursor position befor:{f.tell()}')
print('\n')
print(f.read())
print('\n')
print(f'cursor position after:{f.tell()}')
f.close()
'''
#readline command--> reads the data line by line
'''
f=open('test.txt')
print(f.readline())
f.close()
'''
#readlines command-->reads all lines of data
'''
f=open('test.txt')
print(f.readlines()) # this will give data in a list form
data=f.readlines()
for line in data: #this will show data line by line
    print(line)
f.close()
'''
#with open-->'r'=read,'w'=write,'a'=append--> with open command automatically close the file after execution.
#'r' command
'''
with open('test.txt','r')as f:
    print(f.read())
print(f.read()) # this will show error bcoz the file is already closed.
'''
#'w' command--> it overwrites the data
'''
with open('test.txt','w')as f:
    f.write('hello priyanshi')
'''
#'a' command--> it appends the data
'''
with open('test.txt','a')as f:
    f.append('\n i am noopur verma')
'''
#to read a ',' seperated file we need to use csv module.
'''
x=[]
y=[]
with open('test1.txt','r')as f:
    data=f.readlines()
    for col in data:
        x.append(col[0])
        y.append(col[2])
print(x)
print(y)
'''
'''
import csv
#from csv import *
x=[]
y=[]
with open('test1.txt','r')as f:
    data=csv.reader(f)
    for col in data:
        x.append(col[0])
        y.append(col[1])
print(x)
print(y)
'''
#random module

#random-->gives a random value between the range {0,1}
'''
import random
print(random.random())
'''
#randrange-->gives a value in a range given by user
'''
import random
print(random.randrange(1,30,4))
'''
#randint--> gives integer value including stop value.
'''
import random
print(random.randint(1,100))
'''
#to find info about some command we can use help
'''
import random
print(help(random.uniform))
'''
#randomuniform
'''
import random
print(random.uniform(1,10))
'''
#game using randint
'''
import random
win_num=random.randint(1,100)
num=int(input("Enter your number between 1-100:-"))
Game_over=False
while not Game_over:
    if num==win_num:
        print("You Won!!!!")
        Game_over=True
    else:
        if num<win_num:
            print("Too Low!!")
            num=int(input("Enter your number again:-"))
        else:
            print("Too High!!")
            num=int(input("Enter your number again:-"))
'''
#game using randrange
'''
import random
win_num=random.randrange(1,30,2)
num=int(input("Enter your number between 1-30:-"))
Game_over=False
while not Game_over:
    if num==win_num:
        print("You Won!!!!")
        Game_over=True
    else:
        if num<win_num:
            print("Too Low!!")
            num=int(input("Enter your number again:-"))
        else:
            print("Too High!!")
            num=int(input("Enter your number again:-"))
'''

#day12:-

#NUMPY:- is a mathematical tool from where we pick mathematical concepts.
'''
import numpy as np
my_list=[1,2,3,4,5]
print(type(np.array(my_list))) #the type of list is converted into array. it will show np.ndarray(n dimensional array)

arr=np.array(my_list)
print(arr) #it will print an array
'''
#multiple matrix using numpy:-
'''
r=np.ones((5,5))
print(r) #automatically show float datatype of one matrix

s=np.zeros((5,5))
print(s) #shows zero matrix
'''
#single dimensional matrix:-
'''
r=np.ones(5)
print(r) #this will show a matrix of 5 columns and 1 row.

r=np.zeros(5)
print(r) #this will show a matrix of 5 columns and 1 row.
'''
'''
s=np.random.randint(1,10,(4,4)) #it will print a new matrix everytime between the range.
print(s)
'''
#arange:-
'''
d=np.arange(1,10) #this will print a matrix of fixed elements of the range
print(d)
'''
'''
s=np.random.randint(1,10,10) #it will print a new matrix everytime between the range in a single row.
print(s)
'''

#seed command-->used to fix the matrix after getting a random matrix
'''
np.random.seed(10) #this will show the same matrix everytime we run the code.
s=np.random.randint(1,10,10) 
print(s)
'''
'''
print('max=',s.max())
print('min=',s.min())
print('mean=',s.mean())
print('max index no.=',s.argmax())
print('min index no.=',s.argmin())
print(s.reshape(2,5)) #this will break the array in 2 rows and 5 columns.
'''
'''
mat=np.arange(1,101).reshape(10,10))
print(mat)
print('\n')
print(mat[2,0]) #this will show the element of 3rd row's 1st element.
print('\n')
print(mat[2])
print(mat[2:])
print(mat[:,0])
'''

#day13:-

#MATPLOTLIB--> it is a data visualization tool
#s= square, o=circle.
'''
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,30,20,50]
plt.plot(x,y,color='r',marker='s',label='square',markersize=12,linewidth=6) #r=red , s=square-->it will show square on values, labels will only show when every point is denoted by some value.
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('XY-Graph')
plt.grid() #enables the grid pattern in graph
plt.legend() #this will help show label, and only happen when label command is active.
plt.show() #to show the graph
'''
#how to use matplotlib with numpy-->
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11)
print(x)
y=np.random.randint(1,100,10)
print(y)
plt.plot(x,y)
plt.show()
'''
#as user input
'''
import numpy as np
import matplotlib.pyplot as plt
n=int(input('enter range:-'))
s=int(input('enter range:-'))
a=int(input('enter range:-'))
x=np.arange(1,n+1)
print(x)
y=np.random.randint(1,s,a)
print(y)
plt.plot(x,y)
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,2,0.01)
s=np.sin(2*np.pi*t) #2*pi*r
plt.plot(t,s)
plt.show()
'''
#bar graph
'''
import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,50,60]
tick_label=['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label,color=['red','green'])
plt.show()
'''
#to show multiple lines in same graph.
'''
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(13,6))
t=np.arange(0,2,0.01)
s=np.sin(2*np.pi*t) #2*pi*r
h=np.cos(2*np.pi*t)
plt.plot(t,s,label='sin')
plt.plot(t,h,label='cos')
plt.legend()
plt.show()
'''
#sub plots-->syntax-(r,c,sec)


'''import matplotlib.pyplot as plt
import numpy as np
t=np.arrange (0,2,0.01)
s=np.sin(2*np.pi*t)
h=np.cos(2*np.pi*t)
plt.subplot(2,1,1)
plt.plot(t,s)
plt.sunplot(2,1,2)
plt.plot(t,h)
plt.show()
'''

#histrogram graph
'''import matplotlib.pyplot as plt
import numpy as np
age=np.random.randint(1,101,67)
print(age)
range=(1,100)
bins=10 # gap \interval 10-20,20-30
plt.hist(age,bins,range,histtype='bar',rwidth=0.7)
plt.show()
'''
#scatter plot

'''import matplotlib.pyplot as plt
import numpy as np
x=np.arrange(1,68)
print(x)
age=np.random.randint(1,101,67)
print(age)
plt.scatter(x,age)
plt.show()
'''


#pie plot
'''import matplotlib.pyplot as plt
activity =['eat','sleep','work','play']
slices=[2,3,5,7]
plt.pie(slices,labels=activity)
plt.show()'''


'''
import matplotlib.pyplot as plt
activity =['eat','sleep','work','play']
slices=[2,3,5,7]
plt.pie(slices,labels=activity ,startangle=90, shadow='true',
        explode=(0,0.1,0.2,0))
plt.show()
'''


'''import matplotlib.pyplot as plt
activity =['eat','sleep','work','play']
slices=[2,3,5,7]
plt.pie(slices,labels=activity ,startangle=90, shadow='true',
        explode=(0,0,0,0),autopct='%1.2f%%')
plt.show()
'''

# data plot from csv data file

'''
import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open ('data.csv','r') as f:
    data1=csv.reader(f)
    for col in data1:
        x.append(col[0])
        y.append(col[1])
print(x)
print(y)
plt.plot(x,y)
plt.show()

'''
#animation graph -- live graph

import matplotlib.animation as animation 
from matplotlib import style
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight') #fivethirtyeight is the style
fig1=plt.figure()
ax1=fig1.add_subplot(1,1,1)
def animate(p):
    plot_data=open('file.txt').read()
    line_data=pot_data.split('\n')
    x1=[]
    y1=[]
    for line in line_data:
        if len(line)>1:
            x,y=line.split(',')
            x1.append(x)
            y1.append(y)

        ax1.clear()
        ax1.plot(x1,y1)
animate_data=animation .FuncAnimation(fig1,animate,interval=500)#500 mili sec
plt.show()
























































































































































































