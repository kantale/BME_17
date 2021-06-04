# Lists

 [Lists](https://el.wikipedia.org/wiki/%CE%9B%CE%AF%CF%83%CF%84%CE%B1_%28%CE%B1%CF%86%CE%B7%CF%81%CE%B7%CE%BC%CE%AD%CE%BD%CE%BF%CF%82_%CF%84%CF%8D%CF%80%CE%BF%CF%82_%CE%B4%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD%29) are a basic concept in computer science.

 It is essentially an ordered set of data. Ordered = each element has its place (1st, 2nd, ...)



```python
a = [1,2,3,4]
print (a)
```

    [1, 2, 3, 4]



A list can have values and variables of different types (numbers, decimals, strings, ...)



```python
a = [1,2,3,"mitsos", 5, 7.77777778]
print (a)
```

    [1, 2, 3, 'mitsos', 5, 7.77777778]



The elements of a list are accessed just like the letters in strings:



```python
a[0] # First element
```




    1




```python
a[0:3] # All elements from first until the 4th without the 4th. 
```




    [1, 2, 3]




```python
a[-1] # The last element
```




    7.77777778




```python
a[-2:] # One but the last element
```




    [5, 7.77777778]




Similarly, we can use steps. Suppose the following list:



```python
b = [1,2,3,4,5,6]
```


```python
b[2:5:2] # From the 3rd until the 6th element (without taking 6th) with step 2
```




    [3, 5]




```python
b[::2] # From start until the end with step 2
```




    [1, 3, 5]




```python
b[:3] # From the start unitl the 4th element (without taking the 4th element)
```




    [1, 2, 3]




```python
# All below are equal
print (b)
print (b[:])
print (b[::])
print (b[::1])
print (b[0:])
print (b[0::])
print (b[0::1])
print (b[:len(b)])
print (b[:len(b):])
print (b[0:len(b)])
print (b[0:len(b):1])
```

    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]



```python
b[-1:0:-1] # From the end until the first (without taking the first) 
```




    [6, 5, 4, 3, 2]




```python
b[-1::-1] # From the end until the first (we also take the first)
```




    [6, 5, 4, 3, 2, 1]




```python
b[::-1] # This is equivalent with the above
```




    [6, 5, 4, 3, 2, 1]




Like strings, we can apply `len` , `count` , `index` to lists.



```python
a = [1,2,3,"mitsos", 5, 7.77777778]
```


```python
len(a) # Number of all elements in the list
```




    6




```python
a.count(1) # How many times does exist in the list?
```




    1




```python
a.count(55) # How many times does 55 exist in the list?
```




    0




```python
a.index("mitsos") # What is the index of "mitsos" in the list?
```




    3




```python
a.index(4) # What is the index of 4 in the list?
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-19-79f48df914e9> in <module>
    ----> 1 a.index(4) # What is the index of 4 in the list?
    

    ValueError: 4 is not in list



A list may contain other lists!



```python
a = [1,2, [3,4,5], 6, 7]
```


```python
len(a)
```




    5




```python
a[2]
```




    [3, 4, 5]




```python
a[1]
```




    2




```python
a[2][1]
```




    4




We can change the contents of any item in a list:



```python
a = [1,2,3,4,5]
a[2] = 8
print (a)
```

    [1, 2, 8, 4, 5]



```python
a[3] = ['Mitsos', 'Kwstas']
print (a)
```

    [1, 2, 8, ['Mitsos', 'Kwstas'], 5]



**Caution!** this is not allowed in strings:



```python
a = 'Mitsos'
a[2] = 'k'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-134-2320b677b6ef> in <module>
          1 a = 'Mitsos'
    ----> 2 a[2] = 'k'
    

    TypeError: 'str' object does not support item assignment



If you want to read more about why this is the case then google: "Why are Python Strings Immutable?"



There is also the empty list: `[]`



```python
a = []
print (len(a))
```

    0



We can write lists in many ways:



```python
# The following 2 are equal:
a = [1,2,3] 

a = [
    1,
    2,
    3,
]
```


**Caution!** It is absolutely ok to add a comma right after the last element in a list!



```python
# These two are equal:
print ([1,2,3]) 
print ([1,2,3,])
```

    [1, 2, 3]
    [1, 2, 3]



So it is fine to add a comma after the last element. But is **not fine** if we do NOT put a comma in between the elements:



```python
a = [
    'aaaa',
    'bbbb' # CAUTION! This string is merged with the one below!
    'cccc'
]
print (len(a))
```

    2



```python
print (a)
```

    ['aaaa', 'bbbbcccc']



A list can have a list, which has a list that has ..



```python
a = [[]]
print (len(a))
```

    1



```python
a = [[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]
print (len(a))
```

    1



```python
a = [1,2,3,[],4]
```


```python
len(a)
```




    5




```python
a=3
b = [a,a,a+1, a/2]
print (b)
```

    [3, 3, 4, 1.5]



We can concatenate two lists:



```python
[1,2,3] + ["mitsos", "a"]
```




    [1, 2, 3, 'mitsos', 'a']




We can multiply a list by a number:



```python
[1,2,3] *4
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




We can not multiply or subtract two lists!



```python
[1,2,3] * [5,6]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-50-4f81883a1dc4> in <module>
    ----> 1 [1,2,3] * [5,6]
    

    TypeError: can't multiply sequence by non-int of type 'list'



```python
[1,2,3] - ["mitsos", "a"]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-51-d5954fea0119> in <module>
    ----> 1 [1,2,3] - ["mitsos", "a"]
    

    TypeError: unsupported operand type(s) for -: 'list' and 'list'



The `list` function converts various data types into lists:



```python
list("mitsos")
```




    ['m', 'i', 't', 's', 'o', 's']




```python
list([1,2,3]) # This does nothing..
```




    [1, 2, 3]




Not everything can be turned into a list:



```python
list(5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-54-0c7f5cd48ec1> in <module>
    ----> 1 list(5)
    

    TypeError: 'int' object is not iterable



A list is always True, unless it is empty:



```python
if [1,2,3]:
    print ("not empty")
```

    not empty



```python
if []:
    print ("not empty")
else:
    print ("is empty!")
```

    is empty!



### Comparing strings



When the comparison operators (`<`, `>`, `<=`, `>=`) are applied to strings, then we compare them [alphabetically](https://en.wikipedia.org/wiki/Alphabetical_order). String ```a``` is "lower" than ```b``` if ```a``` is placed in a lower index than ```b``` if we sort ```a``` and ```b```. 


```python
'ab' < 'fg'
```




    True




```python
'ab' < 'b'
```




    True




```python
'ab' < 'ac'
```




    True




```python
'ab' < 'a'
```




    False




The empty string has the lowest possible value



```python
'' < '0'
```




    True




```python
"A" < "a"
```




    True




```python
"05456745674" < "5"
```




    True




```python
'8' < '09'
```




    False




### The ```in``` operator

 This operator checks if there is "something" "somewhere"



```python
'rak' in 'Heraklion'
```




    True




```python
'raki' in 'Heraklion'
```




    False




```python
'h' in 'Heraklion'
```




    False




```python
'H' in 'Heraklion'
```




    True




```python
1 in [1,2,3]
```




    True




```python
[1,2] in [1,2,3]
```




    False




```python
[1,2] in [1, [1,2], 3]
```




    True




```python
False in [1, True-True]
```




    True




```python
None in [3, None, 4]
```




    True




```python
'ra' in ['Heraklion']
```




    False




```python
[] in [1, [], 2]
```




    True




### map and filter



We can apply a function to all elements of a list with the `map` function:



```python
def f(x):
    return x+1

a = [4,5,6]

list(map(f,a))
```




    [5, 6, 7]




We can get a subset of a list of elements that have a property with the `filter` function. The filter must return something that can be valued as `True` or `False` .



```python
def is_even(x):
    # Return True / False depending in whether x is even or not
    return x%2==0

a = [1,2,3,4,5,6,7,8,9]
list(filter(is_even,a))
```




    [2, 4, 6, 8]




```python
def is_first_vowel(x):
    # Return True or False depending to whether x starts with a vowel
    return x[0].lower() in 'aeiouy'

a = ['Ioannina', 'Thessalonikh', 'Athena']
list(filter(is_first_vowel,a))
```




    ['Ioannina', 'Athena']




### Operations on lists

Some of the operations that we can do on lists are:



```python
sum([2,3,4]) # The sum of all elements
```




    9




**Attention** `sum` must be applied to lists containing only `int` or `float` values



```python
sum(['a', 'b'])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-68-0ca1e4efb8fe> in <module>
    ----> 1 sum(['a', 'b'])
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
min([3,5,4]) # minimum element
```




    3




```python
max(['heraklion', 'patras', 'athens']) # Maximum element
```




    'patras'




```python
max(['heraklion', 'patras', 't'])
```




    't'



`max` and `min` have a very interesting property. When applied to lists that contain other lists, then it tries to compare these elements with the following logic: Compare first element of both lists, if they are the same then move to the second element, if both second elements are the same then move to the third etc. 



```python
min([5, "b"], [6, "a"]) # 5 is lower than 5 so the second element is not checked 
```




    [5, 'b']




```python
# 5 is equal to 5 so the second elements ("b" and "a") are alse checked:
min([[5, "b"], [5, 'a']])

```




    [5, 'a']




```python
# Another example:
min([[5, "b"], [7, "t"], [6, 'r'], [5, 'a']])
```




    [5, 'a']




And that&#39;s because:



```python
[5, 'a'] < [5, 'b']
```




    True




### Insert and remove items to a list

 Remember that we can concatenate two lists:



```python
[1,2,3] + ['Μίτσος', 7.8]
```




    [1, 2, 3, 'Μίτσος', 7.8]




We can use this property to add any item to a list anywhere:



```python
# Insert at the end:
a = [1,2,3]
a = a + ['Μήτσος']
print (a)
```

    [1, 2, 3, 'Μήτσος']



Remember that `a = a + b` is equivalent to `a += b` :



```python
# Insert at the end:
a = [1,2,3]
a += ['Μήτσος']
print (a)
```

    [1, 2, 3, 'Μήτσος']



```python
# Insert at the beginning:
a = [1,2,3]
a = ['Μήτσος'] + a
print (a)
```

    ['Μήτσος', 1, 2, 3]



```python
# Insert at any index (we use the slicing trick)
a = [1,2,3]
a = a[:2] + ['Μήτσος'] + a[2:]
print (a)
```

    [1, 2, 'Μήτσος', 3]



We can use the append, extend and insert functions instead:



```python
a = [1,2,3]
a.append('Mitsos') # equivalent to: a += ['Mitsos']
print (a)
```

    [1, 2, 3, 'Mitsos']



```python
a = [1,2,3]
a.extend(['Mitsos', 7.8]) # equivalent to: a += ['Mitsos', 7.8]
print (a)
```

    [1, 2, 3, 'Mitsos', 7.8]



```python
a = [1,2,3]
a.insert(2, 'Mitsos') # equivalent to: a = a[:2] + ['Mitsos'] + a[2:]
print (a)
```

    [1, 2, 'Mitsos', 3]



To remove an item we can use slicing again:



```python
a = [1, 2, 'Mitsos', 3]
a = a[:2] + a[3:]
print(a)
```

    [1, 2, 3]



But we can also use `del` :



```python
a = [1, 2, 'Mitsos', 3]
del a[2]
print (a)
```

    [1, 2, 3]



Another way is to just use `filter`:



```python
a = [1, 2, 'Mitsos', 3]

def remove_mitsos(x):
    return x != 'Mitsos'

a=list(filter(remove_mitsos, a))
print(a)
```

    [1, 2, 3]



### Sorting

 With the command `sorted` we can sort a list:



```python
a = [3,4,5,3,2,1]
```


```python
sorted(a)
```




    [1, 2, 3, 3, 4, 5]




**Caution!** `sorted` does NOT change the list. Instead it returns the result to another variable:



```python
a
```




    [3, 4, 5, 3, 2, 1]




```python
b = sorted(a)
```


```python
b
```




    [1, 2, 3, 3, 4, 5]




if we want to change our list (sorting in place) we should use the `sort` function:



```python
a = [3, 4, 5, 3, 2, 1]
a.sort()
print (a) # a changed!
```

    [1, 2, 3, 3, 4, 5]



We can only sort lists that have elements that can be compared:



```python
sorted(["b", "a", "c"])
```




    ['a', 'b', 'c']




```python
sorted(["b", "a", 100, "c"])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-81-b245b7eeb5df> in <module>
    ----> 1 sorted(["b", "a", 100, "c"])
    

    TypeError: '<' not supported between instances of 'int' and 'str'



We can sort from largest to smallest:



```python
sorted([3,4,5,2,3,4,5,2,1], reverse=True)
```




    [5, 5, 4, 4, 3, 3, 2, 2, 1]




As with `min` and `max` , if sort a list of lists (or tuple), then it first checks the first element of the list. If it is equal, then check the second etc:



```python
a = [
    ["mitsos", 50],
    ['gianni', 40],
    ['gianni', 30]
]
sorted(a)
```




    [['gianni', 30], ['gianni', 40], ['mitsos', 50]]




In the example above ```['gianni', 30]``` is less than ```'gianni', 40]```:



```python
['gianni', 30] < ['gianni', 40]
```




    True



Sometimes we may want to sort a list that contains sublists but we want the sorting to be done not based on the first element but on our own function. E.g. Given the list:



```python
a = [["gianni", 30, 20000], ["mitsos", 50, 4000], ["anna", 60, 100000]]
```


Suppose we want to sort the list items based on their third item (20000, 4000, 100000). Be careful that if we apply the `sorted` command then it will not return what we want:



```python
sorted(a)
```




    [['anna', 60, 100000], ['gianni', 30, 20000], ['mitsos', 50, 4000]]




We want the list whose third element is 4000 to come out first. Then the list whose third element is 20000 to come out second and finally the list whose third element is 100000 to come out last.

In this case we can create a function which takes as an argument an element of a list and returns the value through which the sorting will be done:



```python
def sort_according_to_this(x):
    return x[2]
```

I can test this function by calling it with various elements of my list. It should return the value for which I want the sorting to be based on:


```python
sort_according_to_this(a[0])
```




    20000




```python
sort_according_to_this(a[1])
```




    4000




```python
sort_according_to_this(a[2])
```




    100000




Now I can pass `sort_according_to_this` to `sorted` as an argument to the sorting function and sort list `a` according to the third element of each of its elements:



```python
sorted(a, key=sort_according_to_this)
```




    [['mitsos', 50, 4000], ['gianni', 30, 20000], ['anna', 60, 100000]]




Another example. Let the list be:



```python
a = ["heraklion", "patras", "thessaloniki", "athens"]
```


The following command sorts the list according to the length of the strings:



```python
sorted(a, key=len)
```




    ['patras', 'athens', 'heraklion', 'thessaloniki']




The `max` and `len` functions also support key = ...:



```python
min(a,key=len) # H polh me to mikrotero onoma
```




    'patras'




```python
max(a,key=len) # H polh me to megalutero onoma
```




    'thessaloniki'



### A thought experiment

Perhaps a function that sorts according to a sorting function might be difficult to understand. This is a thought experiment that could make this a bit more clear. Suppose that someone hands you the task to "sort all countries of Europe". What would be the immediate qeustion after this from you? "Sort according to what?". A sorting of a list of numbers or a list of strings is straightforward. What we usually want is an ordering from lower to greater or an alphabetical ordering. But what if a list refers to a real world entity (countries of Europe) or contains a complex item like list of lists... ?

So let's return to the countries of Europe:



```python
# A random list of european countries
countries = ['France', 'Germany', 'Italy', 'Greece', 'Spain', 'Belgium', 'The Netherlands']
```

How can we order them? The default alphabetical sorting is of no interest:


```python
sorted(countries)
```




    ['Belgium', 'France', 'Germany', 'Greece', 'Italy', 'Spain', 'The Netherlands']



Now suppose that we have a function the returns the GDP of each country:



```python
def get_GDP(country):
    return ... # Magic commands tha return the GDP of a country
```

Now we can sort the list of countries according to their GDP:


```python
sorted(countries, key=get_GDP)
```


```python

```
