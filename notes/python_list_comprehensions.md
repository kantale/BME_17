### The `split` and `join`

 If we want to "break" a string into a list of many strings then we can use the `split` command:



```python
"a+b+c".split('+')
```




    ['a', 'b', 'c']




```python
"hello world".split(' ')
```




    ['hello', 'world']




```python
"I like to move it move it".split('move')
```




    ['I like to ', ' it ', ' it']




```python
a = '''
ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.
ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·
αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,
νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο
ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.
'''
a.split('\n')
```




    ['',
     'ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ',
     'πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·',
     'πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,',
     'πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,',
     'ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.',
     'ἀλλ᾽ οὐδ᾽ ὣς ἑτάρους ἐρρύσατο, ἱέμενός περ·',
     'αὐτῶν γὰρ σφετέρῃσιν ἀτασθαλίῃσιν ὄλοντο,',
     'νήπιοι, οἳ κατὰ βοῦς Ὑπερίονος Ἠελίοιο',
     'ἤσθιον· αὐτὰρ ὁ τοῖσιν ἀφείλετο νόστιμον ἦμαρ.',
     '']




A call to `split` without any argument removes all types of spaces (space, tabs and new lines) between the words in a string:



```python
"hello                 world".split()
```




    ['hello', 'world']




The `join` method does the opposite. Takes a list of strings and joins them into a string:



```python
'+'.join(['a','b','c'])
```




    'a+b+c'




```python
' '.join(['hello', 'world'])
```




    'hello world'




```python
print ('\n'.join(['line 1', 'line 2']))
```

    line 1
    line 2



### Functions ```all``` and ```any``` 



`all` returns `True` if **all** the items in a list are `True`



```python
all([True, True, True])
```




    True




```python
all([True, False, True])
```




    False




```python
all([3,4,5,4,5])
```




    True




```python
all([3,4,5,'',4,5])
```




    False




`any` returns `True` if any of the items (even one) in the list is `True` :



```python
any([False, False, False])
```




    False




```python
any([False, False, False, "mitsos"])
```




    True




**Attention!**:
* The `all` value of the empty list is `True`
* The `any` value of the empty list is `False`



```python
all([])
```




    True




```python
any([])
```




    False




### The ```range``` function



The `range` function creates something (*) that represents a numeric sequence.

(\*) This "something" is called a generator and we will talk more about it in the next lecture



```python
range(1,10) 
```




    range(1, 10)




If we apply the `list` function in the object returned from range then we can generate a list of sequential elements:



```python
list(range(10)) # From 0 to 10 (without 10)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(5,10)) # From 5 to 10 (without 10)
```




    [5, 6, 7, 8, 9]




```python
list(range(1,11,2)) # From 1 to 11 (without 11) with step 2
```




    [1, 3, 5, 7, 9]




This [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression) can also be in a descending order:



```python
list(range(11,1,-2))
```




    [11, 9, 7, 5, 3]




```python
list(range(10,1,-1))
```




    [10, 9, 8, 7, 6, 5, 4, 3, 2]




The `list(range(...))` returns a list with which we can perform operations normally as we have seen:



```python
a = list(range(100, 120, 5)) + ["mitsos"]
print (a)
```

    [100, 105, 110, 115, 'mitsos']



Why whenever we see `"ΧΥΖ"[a:b]` , `[1,2,3][a:b]` , `range(a,b)`  this means from `a` to `b` **WITHOUT `b`**? This story goes [back a long way](https://en.wikipedia.org/wiki/Zero-based_numbering). Generally, in computing when we want N elements, then based on an old contract, the first element has index 0, the second 1, etc. So when we say `range(10)` the python generates a list from 0 to 9. When we type range(5,7) then in essence we ask python  for a list of 2 items (7-5). The first according to the same convention will be "where the numbering starts" ie 5. Since the list must have 2 items then the second will be the next one ie 6. This numbering is very convenient for [some mathematical calculations](https://www.johndcook.com/blog/2008/06/26/why-computer-scientists-count-from-zero/) as well. Some additional examples:



```python
list(range(3,10,2))
```




    [3, 5, 7, 9]




```python
list(range(3,11,2))
```




    [3, 5, 7, 9]




```python
list(range(3,12,2))
```




    [3, 5, 7, 9, 11]




```python
list(range(10)) # list(range(0,10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
list(range(5,7)) # list(range(a,b)) # b-a
```




    [5, 6]




### The `zip` function

 With `zip` we can &#39;join&#39; two lists into one list of sublists:



```python
list(zip([1,2,3], ['a', 'b', 'c']))
```




    [(1, 'a'), (2, 'b'), (3, 'c')]




### The `enumerate` function

The `enumerate` function takes as an argument a list and creates another list which contains both the indexes and the elements of the first list:



```python
a = ["python", "mitsos", "Crete"]
print (list(enumerate(a)))
```

    [(0, 'python'), (1, 'mitsos'), (2, 'Crete')]



The `enumerate` functions does exactly the same as this combination of `range` and `zip`:



```python
a = ["python", "mitsos", "Crete"]
print (list(zip(range(len(a)),a)))
```

    [(0, 'python'), (1, 'mitsos'), (2, 'Crete')]



### The `for` syntax

 With the `for` syntax we can repeat commands for each element in a list



```python
for x in [1,4,6]: 
    print (x)
```

    1
    4
    6



```python
for x in [1,4,6]: 
    print ("The number is:", x)
```

    The number is: 1
    The number is: 4
    The number is: 6



```python
for x in range(1,10): 
    print ("The number is:", x)
```

    The number is: 1
    The number is: 2
    The number is: 3
    The number is: 4
    The number is: 5
    The number is: 6
    The number is: 7
    The number is: 8
    The number is: 9



```python
for i in range(1,10,3): 
    print ("Hello:", i)
```

    Hello: 1
    Hello: 4
    Hello: 7



If the commands we want to repeat are more than 1 then it is **MANDATORY** to put them on the next line and further inside. This is called mandatory [indentation](https://en.wikipedia.org/wiki/Indentation_style) or [off-side rule](https://en.wikipedia.org/wiki/Off-side_rule) !



```python
for i in range(1,10,3):
    print ("command A:", i)
    print ("command B:", i)
```

    command A: 1
    command B: 1
    command A: 4
    command B: 4
    command A: 7
    command B: 7



If there is a `for` inside another `for` then the following lines must be entered even further:



```python
for i in range(1,5):
    for j in range(1,5):
        print (i,j)
```

    1 1
    1 2
    1 3
    1 4
    2 1
    2 2
    2 3
    2 4
    3 1
    3 2
    3 3
    3 4
    4 1
    4 2
    4 3
    4 4



Example: The multiplication table:



```python
for i in range(1,11):
    for j in range(1,11):
        print ("{} X {} = {}".format(i,j,i*j))
    print ("=" * 10)
```

    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    1 X 10 = 10
    ==========
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    2 X 10 = 20
    ==========
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    ==========
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    ==========
    5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    5 X 8 = 40
    5 X 9 = 45
    5 X 10 = 50
    ==========
    6 X 1 = 6
    6 X 2 = 12
    6 X 3 = 18
    6 X 4 = 24
    6 X 5 = 30
    6 X 6 = 36
    6 X 7 = 42
    6 X 8 = 48
    6 X 9 = 54
    6 X 10 = 60
    ==========
    7 X 1 = 7
    7 X 2 = 14
    7 X 3 = 21
    7 X 4 = 28
    7 X 5 = 35
    7 X 6 = 42
    7 X 7 = 49
    7 X 8 = 56
    7 X 9 = 63
    7 X 10 = 70
    ==========
    8 X 1 = 8
    8 X 2 = 16
    8 X 3 = 24
    8 X 4 = 32
    8 X 5 = 40
    8 X 6 = 48
    8 X 7 = 56
    8 X 8 = 64
    8 X 9 = 72
    8 X 10 = 80
    ==========
    9 X 1 = 9
    9 X 2 = 18
    9 X 3 = 27
    9 X 4 = 36
    9 X 5 = 45
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    9 X 10 = 90
    ==========
    10 X 1 = 10
    10 X 2 = 20
    10 X 3 = 30
    10 X 4 = 40
    10 X 5 = 50
    10 X 6 = 60
    10 X 7 = 70
    10 X 8 = 80
    10 X 9 = 90
    10 X 10 = 100
    ==========



We can also repeat using a string instead of a list:



```python
for letter in "python":
    print (letter)
```

    p
    y
    t
    h
    o
    n



If a list has sub-lists with more than 1 item then we can use more than 1 variable in `for` :



```python
a = [[2, "Crete"], [3, "Cyprus"], [4, "Majiorca"]]
for x, y in a:
    print ("Number: {} Island: {}".format(x,y))
```

    Number: 2 Island: Crete
    Number: 3 Island: Cyprus
    Number: 4 Island: Majiorca



Of course the same can be done if it has sub-lists with 3 items etc ..



```python
a = [[1,2,3], ["a", "b", "c"]]
for x,y,z in a:
    print ("{} {} {}".format(x,y,z))
```

    1 2 3
    a b c



The `if` syntax (and any other python syntax) can be inside a `for`:



```python
for i in range(1,10):
    if i>5:
        print (i)
```

    6
    7
    8
    9



```python
for i in range(1,10):
    if i>=5:
        print (i)
```


### break and continue



With the `break` command we can "stop" the iteration inside a for. When the computer "sees" `break` then it directly exits `for` :



```python
for i in range(1,10):
    print (i)
    if i>5:
        break # Get out from for !!!
```

    1
    2
    3
    4
    5
    6



With the `continue` command we can ignore all the resr of the commands in an iteration and move on to the next item in the iteration. Or else, we can move on, or.. continue to the next item in the iteration.




```python
for i in range(1,10):
    if i == 5: # ΔΕΝ ΤΥΠΩΝΕΙ ΤΟ 5
        continue
    print (i) # TO PRINT **DEN** EINAI MESA STHN IF! (einai mesa sth for)
```

    1
    2
    3
    4
    6
    7
    8
    9



**Caution!** anything that is below (and in the same indentation) with `continue` and `break` is ignored!



```python
for i in range(1,10):
    if i == 5:
        continue
        print (i) #  This command is ignored
```

Also having as a last command in an iteration the ```continue``` command, is redundant and does not make any difference. Python does this automatically..


```python
# Please don't do this!
for x in [1,2,3]:
    print (x)
    continue # <-- This is redundant
```

    1
    2
    3



# List Comprehensions

List Comprehension is a new syntax for creating a list from another list. The [official description is here](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) . The general form is:

```python
a = [expression for variable in LIST]
```

Which is equivalent to:

```python
a = []
for variable in LIST:
    a.append(expression)
```

For example:



```python
a = [1,2,3]
```


```python
b = [x+1 for x in a]
print (b)
```

    [2, 3, 4]



The above is equivalent to:



```python
a = [1,2,3]
b = []
for x in a:
    b.append(x+1)
print (b)
```

    [2, 3, 4]



Some other examples:



```python
a = ["a", "b", "c"]
["hello: " + x for x in a]
```




    ['hello: a', 'hello: b', 'hello: c']




```python
a = ["a", "b", "c"]
b  = [x * 3 for x in a]
print (b)
```

    ['aaa', 'bbb', 'ccc']



```python
a = [1,2,3,4,5,6]
[x/2 for x in a]
```




    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]



We can also use the `if` syntax in a list comprehensions. The general form is:

```python
a = [expression_1 for variable in LIST if expression_2]
```

Which is equivalent to:

```python
a = []
for variable in LIST:
    if expression_2:
        a.append(expression_1)
```

Examples:



```python
a = [1,2,3,4,5,6]
[x/2 for x in a if x>4]
```




    [2.5, 3.0]




This is equivalent to:



```python
a = [1,2,3,4,5,6]
b = []
for x in a:
    if x>4:
        b.append(x/2)
print (b)
```

    [2.5, 3.0]



Another example. Let the list be:



```python
a = [1,2,3,4,5,4,3,5,6,7,8,7,6,5,5,4]
```


What are all the items that have a value of 4?

First method:



```python
[i for i, x in enumerate(a) if x==4]
```




    [3, 5, 15]




Second method:



```python
a = [1,2,3,4,5,4,3,5,6,7,8,7,6,5,5,4]
[x for x in range(len(a)) if a[x] == 4]
```




    [3, 5, 15]




```python
list(range(len(a)))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]




Also a list comprehension can have more than 1 `for` :



```python
a = [1,2,3]
b = ["a", "b", "c"]
["{}{}".format(x,y) for x in a for y in b]
```




    ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']




This is equivalent to:



```python
c = []
for x in a:
    for y in b:
        c.append("{}{}".format(x,y))
print (c)
```

    ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']



By using list comprehension we can produce a string that contains the whole [multiplication table](https://en.wikipedia.org/wiki/Multiplication_table):



```python
print ('\n'.join(["{} X {} = {}".format(x,y,x*y) for x in range(1,11) for y in range(1,11)]))
```

    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    1 X 10 = 10
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    2 X 10 = 20
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    5 X 8 = 40
    5 X 9 = 45
    5 X 10 = 50
    6 X 1 = 6
    6 X 2 = 12
    6 X 3 = 18
    6 X 4 = 24
    6 X 5 = 30
    6 X 6 = 36
    6 X 7 = 42
    6 X 8 = 48
    6 X 9 = 54
    6 X 10 = 60
    7 X 1 = 7
    7 X 2 = 14
    7 X 3 = 21
    7 X 4 = 28
    7 X 5 = 35
    7 X 6 = 42
    7 X 7 = 49
    7 X 8 = 56
    7 X 9 = 63
    7 X 10 = 70
    8 X 1 = 8
    8 X 2 = 16
    8 X 3 = 24
    8 X 4 = 32
    8 X 5 = 40
    8 X 6 = 48
    8 X 7 = 56
    8 X 8 = 64
    8 X 9 = 72
    8 X 10 = 80
    9 X 1 = 9
    9 X 2 = 18
    9 X 3 = 27
    9 X 4 = 36
    9 X 5 = 45
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    9 X 10 = 90
    10 X 1 = 10
    10 X 2 = 20
    10 X 3 = 30
    10 X 4 = 40
    10 X 5 = 50
    10 X 6 = 60
    10 X 7 = 70
    10 X 8 = 80
    10 X 9 = 90
    10 X 10 = 100



# Some examples of use of the above



## 1. From a list take only those that have a specific property

e.g. Take only odd numbers from a list



```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x%2==1

```


```python
# 1st method
b = list(filter(f,a))
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 2nd method
b = []
for x in a:
    if f(x):
        b.append(x)
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 2rd method
b = []
for x in a:
    if not f(x):
        continue
        
    b.append(x)
print (b)
```

    [1, 3, 5, 7, 9]



```python
# 4th method
b = [x for x in a if f(x)]
print (b)
```

    [1, 3, 5, 7, 9]



## 2. Count the number that has a specific property in a list

How many are odd numbers?



```python
# 1st method
c = len(list(filter(f,a)))
print(c)
```

    5



```python
# 2nd method
c = sum(map(f,a))
print (c)
```

    5



```python
# 3rd method
c = 0
for x in a:
    if f(x):
        c += 1
print (c)
```

    5



```python
# 4th method
c = 0
for x in a:
    if not f(x):
        continue
    c += 1
print (c)
```

    5



```python
# 5th method
c = len([None for x in a if f(x)])
print (c)
```

    5



```python
# 6th method
c = sum(f(x) for x in a)
print (c)
```

    5



## 3. Apply a function to all elements of a list

eg multiply with 10 all elements in a list



```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x*10
```


```python
# 1st method
b = list(map(f,a))
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



```python
# 2nd method
b = []
for x in a:
    b.append(f(x))
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



```python
# 3rd method
b = [f(x) for x in a]
print (b)
```

    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



## 4. A combination of all of the above

Find the sum of the multiplication with 10 of all the odd numbers in a list.



```python
a = [1,2,3,4,5,6,7,8,9,10]
def f(x):
    return x%2==1
def g(x):
    return x*10
```


```python
# 1st method
c = sum(map(g, filter(f, a)))
print (c)
```

    250



```python
# 2nd method
c = 0
for x in a:
    if f(x):
        c += g(x)
print (c)
```

    250



```python
# 3rd method
c = 0
for x in a:
    if not f(x):
        continue
    c += g(x)
print (c)
```

    250



```python
# 4th method
c = sum(g(x) for x in a if f(x))
print (c)
```

    250



## 5. Combining more than one list

We have two lists of the same size a, b. In each element in these lists we have one abservation. Each observation has 2 "values". For example:

Suppose we have this list of cities:



```python
cities = ['Heraklion', 'Athens', 'Thessaloniki']
```


and their **respective** populations:



```python
pop = [200_000, 4_000_000, 500_000]
```


Get the cities with a population of less than 1,000,000:



```python
# 1st method
solution = []
for city, p in zip(cities, pop):
    if p < 1_000_000:
        solution.append(city)
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 2nd method
solution = []
for i, p in enumerate(pop):
    if p < 1_000_000:
        solution.append(cities[i])
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 3rd method
solution = [city for city, p in zip(cities, pop) if p<1_000_000]
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 4th method
solution = [cities[i] for i,p in enumerate(pop) if p<1_000_000]
print (solution)
```

    ['Heraklion', 'Thessaloniki']



```python
# 5th method (a bit ugly..)
def f(x):
    return x[1]<1_000_000

def g(x):
    return x[0]

def h(x):
    return cities[x]

solution = list(map(h, map(g, filter(f, enumerate(pop)))))
print (solution)
```

    ['Heraklion', 'Thessaloniki']



## 6. Convert a list of lists, a flat list

Suppose that we have the following list:



```python
a = [ [1,2], ["a", "b"], [True, False] ]
```


Make a list that has all the elements of ```a``` in one level (without sublists)



```python
# 1st method
b = []
for x in a:
    b.extend(x)
print (b)
```

    [1, 2, 'a', 'b', True, False]



```python
# 2nd method
b = []
for x in a:
    for y in x:
        b.append(y)
print (b)
```

    [1, 2, 'a', 'b', True, False]



```python
# 3rd method (more pythonic!)
b = [y for x in a for y in x]
print (b)
```

    [1, 2, 'a', 'b', True, False]



## 7. Un-zipping!

Suppose that we have the following list:



```python
a = [ [1, "a"], [2, "b"], [3, "c"]]
```


Create two lists k, l which will have the first and second elements of each list respectively.



```python
# 1st method
k = []
l = []
for x in a:
    k.append(x[0])
    l.append(x[1])
print (k)
print (l)
```

    [1, 'a', True]
    [2, 'b', False]



```python
# 2nd method
k = []
l = []
for x,y in a:
    k.append(x)
    l.append(y)
print (k)
print (l)
```

    [1, 'a', True]
    [2, 'b', False]



```python
# 3rd method
k = [x[0] for x in a]
l = [x[1] for x in a]
print (k)
print (l)
```

    [1, 'a', True]
    [2, 'b', False]



## 8. Check if there is a specific item in a list.

Is ```3``` in the list: `a = [1,2,3,4,5,6,7,8,9,10]` ?



```python
a = [1,2,3,4,5,6,7,8,9,10]

```


```python
# 1st method
b = 3 in a
print (b)
```

    True



```python
# 2nd method
b = False
for x in a:
    if x==3:
        b = True
        break
print (b)
```

    True



```python
# 3rd method
b = True
for x in a:
    if x==3:
        break
else:
    b = False
print (b)
```

    True

