### The `while` syntax

The `while` syntax is used as a more basic method for iteration compared to the `for` syntax. With the

```python
while EXPRESSION:
    command_1
    command_2
    ...
    command_n
```
    
We declare that all the commands "below" `while` (`command_1`, ... `command_n`) will run until the `<EXPRESSION>` becomes `False`.



```python
# Print all numbers from 0 to 9 (9 is included) 
a=0
while a<10:
    print (a)
    a += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



Print all **odd** numbers from 1 to 50



```python
a=1

while a<50:
    if a%2 == 1:
        print (a)
    a+=1
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    23
    25
    27
    29
    31
    33
    35
    37
    39
    41
    43
    45
    47
    49



print the multiplication table of 8



```python
a = 1
while a<=10:
    print (a*8)
    a+=1

```

    8
    16
    24
    32
    40
    48
    56
    64
    72
    80



A little bit better:



```python
a = 1
while a<=10:
    print (a, 'times 8 is', a*8)
    a+=1
```

    1 times 8 is 8
    2 times 8 is 16
    3 times 8 is 24
    4 times 8 is 32
    5 times 8 is 40
    6 times 8 is 48
    7 times 8 is 56
    8 times 8 is 64
    9 times 8 is 72
    10 times 8 is 80



Print the multiplication table of all numbers from 1 to 10



```python
a = 1
while a<=10:
    b=1
    while b<=10:
        print (a, 'times ', b, ' is', a*b)
        b+=1
    a+=1
```

    1 times  1  is 1
    1 times  2  is 2
    1 times  3  is 3
    1 times  4  is 4
    1 times  5  is 5
    1 times  6  is 6
    1 times  7  is 7
    1 times  8  is 8
    1 times  9  is 9
    1 times  10  is 10
    2 times  1  is 2
    2 times  2  is 4
    2 times  3  is 6
    2 times  4  is 8
    2 times  5  is 10
    2 times  6  is 12
    2 times  7  is 14
    2 times  8  is 16
    2 times  9  is 18
    2 times  10  is 20
    3 times  1  is 3
    3 times  2  is 6
    3 times  3  is 9
    3 times  4  is 12
    3 times  5  is 15
    3 times  6  is 18
    3 times  7  is 21
    3 times  8  is 24
    3 times  9  is 27
    3 times  10  is 30
    4 times  1  is 4
    4 times  2  is 8
    4 times  3  is 12
    4 times  4  is 16
    4 times  5  is 20
    4 times  6  is 24
    4 times  7  is 28
    4 times  8  is 32
    4 times  9  is 36
    4 times  10  is 40
    5 times  1  is 5
    5 times  2  is 10
    5 times  3  is 15
    5 times  4  is 20
    5 times  5  is 25
    5 times  6  is 30
    5 times  7  is 35
    5 times  8  is 40
    5 times  9  is 45
    5 times  10  is 50
    6 times  1  is 6
    6 times  2  is 12
    6 times  3  is 18
    6 times  4  is 24
    6 times  5  is 30
    6 times  6  is 36
    6 times  7  is 42
    6 times  8  is 48
    6 times  9  is 54
    6 times  10  is 60
    7 times  1  is 7
    7 times  2  is 14
    7 times  3  is 21
    7 times  4  is 28
    7 times  5  is 35
    7 times  6  is 42
    7 times  7  is 49
    7 times  8  is 56
    7 times  9  is 63
    7 times  10  is 70
    8 times  1  is 8
    8 times  2  is 16
    8 times  3  is 24
    8 times  4  is 32
    8 times  5  is 40
    8 times  6  is 48
    8 times  7  is 56
    8 times  8  is 64
    8 times  9  is 72
    8 times  10  is 80
    9 times  1  is 9
    9 times  2  is 18
    9 times  3  is 27
    9 times  4  is 36
    9 times  5  is 45
    9 times  6  is 54
    9 times  7  is 63
    9 times  8  is 72
    9 times  9  is 81
    9 times  10  is 90
    10 times  1  is 10
    10 times  2  is 20
    10 times  3  is 30
    10 times  4  is 40
    10 times  5  is 50
    10 times  6  is 60
    10 times  7  is 70
    10 times  8  is 80
    10 times  9  is 90
    10 times  10  is 100



Find how many digits a number has:



```python
a=51234123
# 1st method (fast and better)
len(str(a))
```




    8




```python
# 2nd method
# Notice that the integer division with 10 removes the last digit from a number!
# 51234123 // 10 --> 5123412

a=51234123
c=0
remainder = a
while remainder != 0:
    remainder = remainder // 10
    c += 1
print (c)
```

    8



How many times does ```a``` occurs in a string?



```python
# 1st method (better / faster)
a = 'zabarakatranemia'
a.count('a')
```




    6




```python
# 2nd method
index = 0
c = 0
while index < len(a):
    if a[index] == 'a':
        c += 1
    index += 1
print (c)
```

    6



Invert a string.



```python
# 1st method (better / faster)
a = 'zabarakatranemia'
a[::-1]
```




    'aimenartakarabaz'




```python
# 2nd method
index = len(a)-1
anapodo = ''
while index >= 0:
    anapodo = anapodo + a[index]
    index -= 1
print (anapodo)
```

    aimenartakarabaz



The sum of all numbers from 1 to 20



```python
s = 0
c = 0
while c < 20:
    c += 1
    s += c
print (s)
```

    210



```python
s = 0
c = 1
while c <= 20:
    s += c
    c += 1
print (s)
```

    210



```python
sum(range(1,21))
```




    210




As with `for` we are allowed to use `break` and `continue`. With `break` we exit the `while` syntax completely, whereas with `continue` we move execution to the beginning of the while where the estimation of the logical expression takes place.



```python
a=0
while a<10:
    a += 1
    if a== 5:
        continue
        
    print (a)
```

    1
    2
    3
    4
    6
    7
    8
    9
    10



Note that 5 does not exist.



```python
a=0
while a<10:
    a += 1
    if a== 5:
        break
        
    print (a)
```

    1
    2
    3
    4



And here when a becomes 5 then it comes out completely from while.



Something that is rarely used but is especially useful is ```else``` after ```while```. It enters the ```else``` syntax only if a ```break``` has **not** occurred in the while.



```python
a=0
while a<10:
    a += 1
    if a== 5:
        break
        
    print (a)
else:
    print ('No break happened')
```

    1
    2
    3
    4



```python
a=0
while a<10:
    a += 1
    #if a== 5:
    #    break
        
    print (a)
else:
    print ('No break happened')
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    No break happened



The `while` syntax is commonly used when we want to do an iteration but we do not know how many times this interation should be done. For example: let a ball fall from 1 meter. Each time it bounces it reaches 90% of its initial height. After 5 bounces to what height will it have reached? Here we know how many iteration we have to do, so we will use the ```for``` syntax:



```python
height=1
for i in range(5):
    height -= 0.1*height
print (height)
```

    0.5904900000000001



Let us now look at another problem: After how many bounces will the ball reach a height of less than 0.5 meters? Now we do not know the number of repetitions (exactly this is what is required), so it is "convenient" to use the ```while``` syntax:



```python
height = 1
bounces = 0
while height > 0.5:
    bounces += 1
    height -= 0.1*height
print (bounces)
```

    7



Another example: The following function checks whether a number is prime or not:



```python
def is_prime(n):
    for x in range(2, int(n**0.5)+1):
        if n%x==0:
            return False
    
    return True
```


If we start suming up all prime numbers starting from 1, to which priment number will this sum exceed 1,000,000?



```python
s = 0
c = 1
while s < 1_000_000:
    if is_prime(c):
        s += c
    c += 1
print (c-1)
```

    3943



# Tuples

Tuples are data structures that are similar to lists. The difference is that in tuples we can not change a value. Or else tuples are immutable data types. To define a tuple, instead of brackets ( `[1,2,3]` ) we use parentheses ( `(1,2,3)` )



```python
a = (1,2,3)
type(a)
```




    tuple




```python
a[2] = 7 #This is an error. We cannot modofy the valuea of a tuple
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-20-21aa96e85905> in <module>
    ----> 1 a[2] = 7 #This is an error. We cannot modofy the valuea of a tuple
    

    TypeError: 'tuple' object does not support item assignment



```python
b = [1,2,3]
b[2] = 7 # This is fine. A is a list
```


Although in tuples we can not add or remove an item, we can change items in lists or dictionaries that they may contain:



```python
a = (1,[4,5],10)
a[1].append(6)
print (a)
```

    (1, [4, 5, 6], 10)



Except from modifying their elements, we can use tuples just as we use lists. For example we can iterate on tuples and apply the functions `min`, `max`, `sort`, ...



```python
for x in (1,2,3):
    print (x)
```

    1
    2
    3



```python
sum((5,6,7))
```




    18




### Functions that return more than 1 value

 In python a function can return more than one value:



```python
def f():
    return 1,2
```


```python
a,b = f()
print (a)
print (b)
```

    1
    2



If we store in a single variable the result of a function that returns more than one value then the type of the returned value is a tuple.



```python
a = f()
```


```python
print (a)
```

    (1, 2)



```python
type(a)
```




    tuple




# Dictionaries

 So far we have seen the following types of variables:



```python
a=0 # integer
a=True # boolean
a="324234" # strings
a=5.6 # floats
a=[2,4,4] # lists
a=None # None
```


Dictionaries are a new type of variable. Dictionaries have data in the form of key -&gt; value. Each key is unique. For example:



```python
a = {"mitsos": 50, "anna": 40}
```


```python
print(a)
```

    {'mitsos': 50, 'anna': 40}



```python
a['mitsos']
```




    50




```python
a['anna']
```




    40




The `keys` method returns a list of all dictionary keys



```python
a.keys()
```




    dict_keys(['mitsos', 'anna'])




The `values` method returns a list of all dictionary values



```python
a.values()
```




    dict_values([50, 40])




We can insert a new pair of KEY, VALUE, as follows:



```python
a["kitsos"] = 100
```


```python
print (a)
```

    {'mitsos': 50, 'anna': 40, 'kitsos': 100}



We can also remove a KEY, VALUE pair with the command del:



```python
del a['kitsos']
print (a)
```

    {'mitsos': 50, 'anna': 40}



The key can be number, string and boolean and tuple. The value can be anything.



```python
a[123] = 0.1
a[3.14] = "hello"
a[False] = [1,2,3]
a[(4,7)] = 4
```


```python
print (a)
```

    {'mitsos': 50, 'anna': 40, 123: 0.1, 3.14: 'hello', False: [1, 2, 3], (4, 7): 4}



```python
# Attention ! False == 0 !
a[0]
```




    [1, 2, 3]




The key can NOT be a list:



```python
a[[1,2,3]] = 0
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-141-6cebb9942dfe> in <module>
    ----> 1 a[[1,2,3]] = 0
    

    TypeError: unhashable type: 'list'



The key can NOT be a dictionary either:



```python
a[{}] = 0
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-142-b372ccb1b9be> in <module>
    ----> 1 a[{}] = 0
    

    TypeError: unhashable type: 'dict'



In python we can have dictionaries in lists and lists in dictionaries without any restrictions



```python
d = {"a": {2:"a"}, 3: ["hello", False, []], 3.1: True}
print (d)
```

    {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True}



We can compose lists and dictionaries from other lists and dictionaries:



```python
[d, d, d["a"]]
```




    [{'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     {2: 'a'}]




```python
{"a": d, "b": d[3]}
```




    {'a': {'a': {2: 'a'}, 3: ['hello', False, []], 3.1: True},
     'b': ['hello', False, []]}




There is also the empty dictionary



```python
a = {}
```


`len` returns the number of records of a dictionary:



```python
person = {"name": "alex", "age": 50, "occupation": "master"}
```


```python
len(person)
```




    3




```python
len({})
```




    0




We can check if a key exists in a dictionary



```python
"name" in person # Very fast..
```




    True




```python
"alex" in person # Very fast..
```




    False




We can check if a value exists in a dictionary:



```python
"alex" in person.values() # Attention! this is slow!
```




    True




We can iterate in all the elements of a dictionary:



```python
for i in person:
    print (i)
```

    name
    age
    occupation



```python
for i in person:
    print ("key: {}  Value: {}".format(i, person[i]))
```

    key: name  Value: alex
    key: age  Value: 50
    key: occupation  Value: master



We can convert a list (or tuple) into a dictionary with the dict function. However, the list must consist of sublists, where each sublist has 2 items. In these sublists the first item will become the key and the second the value:



```python
a = [("mitsos", 1), ('maria', 2), ('elenh', 4) ]
dict(a)
```




    {'mitsos': 1, 'maria': 2, 'elenh': 4}




The opposite can also be done with the ```items``` method:



```python
a = {'mitsos': 1, 'maria': 2, 'elenh': 4}
print(list(a.items()))
```

    [('mitsos', 1), ('maria', 2), ('elenh', 4)]



### Accessing data in dictionary

 We can use `[][]` more than once to access an item:



```python
person = {"name": "alex", "age": 50, "occupation": "master", "exper": ["python", "karate"]}
```


```python
print (person)
```

    {'name': 'alex', 'age': 50, 'occupation': 'master', 'exper': ['python', 'karate']}



```python
print (person['exper'][0])
```

    python



```python
print (person['exper'][1])
```

    karate



```python
print (person['exper'])
```

    ['python', 'karate']



```python
a = ["a", "b", {"name": "mitsos", "surnmae": "sdfsdfsdf"}]
```


```python
a[0]
```




    'a'




```python
a[1]
```




    'b'




```python
a[2]
```




    {'name': 'mitsos', 'surnmae': 'sdfsdfsdf'}




```python
a[2]['name']
```




    'mitsos'




The function `a.get(b,c)` checks if `b` exists in the dictionary `a`. If it exists then it returns the value: `a[b]`, otherwise it returns `c`:



```python
a = {"a": 1, "b": 2, "c": 3}
```


```python
a.get("mitsos", 50)
```




    50




```python
a.get("a", 50)
```




    1




### Iteration in a dictionary

Suppose that a is a list and b is a dictionary:



```python
a = [1,2,3]
b = {"a":1, "b":2, "c":3}
```


We can iterate a list as follows:



```python
for x in a:
    print (x)
```

    1
    2
    3



The same can be done in a dictionary:



```python
for x in b:
    print (x, b[x])
```

    a 1
    b 2
    c 3



We can get the key-value pairs of the dictionary as a list by using the `items()` method:



```python
list(b.items())
```




    [('a', 1), ('b', 2), ('c', 3)]




So as we have seen before, we can iterate a dictionary and assign the key-value pairs of each record of the dictionary into two variables:



```python
for x,y in b.items():
    print (x,y)
```

    a 1
    b 2
    c 3



### Examples with dictionary



Count the number of occurences of each item in a list:



```python
a = [3,2,3,2,4,5,4,3,6,5,7,9,1,2,8,9,9]
d = {}

for x in a:
    if not x in d:
        d[x] = 0
    d[x] += 1

print (d)
```

    {3: 3, 2: 3, 4: 2, 5: 2, 6: 1, 7: 1, 9: 3, 1: 1, 8: 1}



Find the value that has the largest key:



```python
a = {1:3, 5:2, 3:1} # Maximum key is 5. The value of 5 is 2.

max_key = max(a.keys())
print(a[max_key])
```

    2



Find the key that has the highest value



```python
a = {1:3, 5:2, 3:1} #  Maximum value is 3 belonging to key 1
max( (v,k)  for k,v in a.items())[1]
```




    1




Let's break the above in smaller steps:



```python
b = list(a.items()) # Convert the list
print (b)

c = [(v,k) for k,v in b] # Swat key/value pairs
print(c)

d = max(c) # Get the tuple that has the maximum value
print(d)

e = d[1] # Get the second element of the maximum tuple. This happens to be the key
print (e)
```

    [(1, 3), (5, 2), (3, 1)]
    [(3, 1), (2, 5), (1, 3)]
    (3, 1)
    1



### Dictionary Comprehension

 In a previous lecture we introduced list comprehensions



```python
# List comprehension
[x for x in [1,2,3,4] if x>2]
```




    [3, 4]




As a reminder, we talked about how the above is equivalent to:



```python
a = []
for x in [1,2,3,4]:
    if x>2:
        a.append(x)
print (a)
```

    [3, 4]



The same can be done with dictionaries:



```python
{ x:x*10 for x in range(1,10)}
```




    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}




This is equivalent to:



```python
a={}
for x in range(1,10):
    a[x] = x*10
print (a)
```

    {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}



Another example:



```python
{ x:'hello {}'.format(x*10) for x in range(1,10)}
```




    {1: 'hello 10',
     2: 'hello 20',
     3: 'hello 30',
     4: 'hello 40',
     5: 'hello 50',
     6: 'hello 60',
     7: 'hello 70',
     8: 'hello 80',
     9: 'hello 90'}




### Sets

 A `set` is a data structure that models a set. Each item in a set can **only** exist once:



```python
set([1,2,3])
```




    {1, 2, 3}




```python
set([1,2,3,2])
```




    {1, 2, 3}




```python
a = set(['a','b', 'a'])
a
```




    {'a', 'b'}




```python
'b' in a
```




    True




```python
set("Hello World!")
```




    {' ', '!', 'H', 'W', 'd', 'e', 'l', 'o', 'r'}




The operation `&` between two sets returns the intersection of the sets:



```python
a = set([1,2,3,4])
b = set([3,4,5,6])
a & b
```




    {3, 4}




The same can be done with the intersection function:



```python
a.intersection(b)
```




    {3, 4}




The operation `|` between two sets returns the union of the sets:



```python
a | b
```




    {1, 2, 3, 4, 5, 6}




The same can be done with the union function:



```python
a.union(b)
```




    {1, 2, 3, 4, 5, 6}




The operation `-` between two sets `α` and `β` returns the elements of `α` that do not exist in `β` :



```python
a - b
```




    {1, 2}




```python
b - a
```




    {5, 6}




```python
(a - b) & (b-a)
```




    set()




We can add an element to a set with the add function:



```python
a = {1,2,3}
a.add(10)
print (a)
```

    {10, 1, 2, 3}



Another way to add an element is to use the ```|``` operator :



```python
a = {1,2,3}
a = a | {10}
print (a)
```

    {10, 1, 2, 3}



We can not add a list to a set. This is because we can only add items that do NOT change:



```python
a.add([7,8,9])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-79-1706898a2cfb> in <module>
    ----> 1 a.add([7,8,9])
    

    TypeError: unhashable type: 'list'



Sets are an additional type of data:



```python
type(set([1,2,3]))
```




    set




```python
a = set([1,2,3])
type(a) is set
```




    True




### set comprehension

 Just like with lists and dictionaries, we can have comprehensions with sets:



```python
{x%4 for x in range(10)}
```




    {0, 1, 2, 3}


