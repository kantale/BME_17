# Introduction to programming with python

###  [Alexandros Kanterakis](mailto:kantale@ics.forth.gr) kantale@ics.forth.gr

###  Introduction

All lectures will be available in the form of [jupyter notebooks](http://jupyter.org/) . Jupyter is an environment that allows us to write python and inspect the results of commands directly in your browser. You can save your experiments in a file and share it by mail, etc.

A jupyter notebook consists of cells. Each cell can contain either python code (other languages are also allowed) or [markdown](https://en.wikipedia.org/wiki/Markdown) . Markdown is a collection of conventions to import formatting into a text file. E.g. if in markdown we write a word between 2 asterisks (eg: `**Alexandros**` ) then it will appear as bold, that is: **Alexander** . [Complete list of all markdown contracts](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) .

You can also load a notebook in your browser, the same way that you open word document. Even better you can save a notebook on the Internet for free! As a [gist](https://gist.github.com/) .



## A first taste

###  print



```python
print ('something')
```

    something



We can use single ('), double quotes (") or triple quotes (''') or ("""), to denote the start and the end of a string.



```python
print ("hello")
```

    hello



```python
print ("""hello""")
```

    hello



```python
print ('''hello''')
```

    hello



We can have an "Enter" inside a string with the special character: "\n". ```n``` stands for "new line".



```python
print ("hello\nworld")
```

    hello
    world



Similarly we can use single or double quotes in a string. Depending on what we use to declare a string (single or double quotes) we should use ```'``` or ```''```:



```python
print ("his master's voice")
```

    his master's voice



```python
print ('his master\'s voice')
```

    his master's voice



```python
print (" I am \"fear\"  ")
```

     I am "fear"  



```python
print ('i am "fear"')
```

    i am "fear"



If we use triple quotes we can have many lines in one string (multiline strings):



```python
print ("""ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.""")
```

    ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ
    πλάγχθη, ἐπεὶ Τροίης ἱερὸν πτολίεθρον ἔπερσεν·
    πολλῶν δ᾽ ἀνθρώπων ἴδεν ἄστεα καὶ νόον ἔγνω,
    πολλὰ δ᾽ ὅ γ᾽ ἐν πόντῳ πάθεν ἄλγεα ὃν κατὰ θυμόν,
    ἀρνύμενος ἥν τε ψυχὴν καὶ νόστον ἑταίρων.



(we will come back later)



### Comments

 In any line, anything that follows the character `#` is considered a comment and is ignored:



```python
# This is a comment
print ('This is not a comment') # But this is!
```

    This is not a comment



### Mathematical operations and expressions:



Python can do operations with integers with any number of digits:



```python
24328470239847502934672098347520349867 * 234573458729835619384756398456
```




    5706813409766902302233897564852365380972748955782671565995978605352




We have the classic operations: addition, subtraction, multiplication and division:



```python
3+2
```




    5




```python
3-2
```




    1




```python
3*2
```




    6




Decimal division:



```python
3/2
```




    1.5




Integer division:



```python
3//2
```




    1




**Caution!**



```python
1/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-18-9e1622b385b6> in <module>()
    ----> 1 1/0
    

    ZeroDivisionError: division by zero



We also have some additional operations:

 The remainder of the division:



```python
15 % 4 
```




    3




That is 15 = 3 * 4 + **3**



The exponential:



```python
4**2
```




    16




**Attention** : The exponential is NOT ```^```:



```python
4 ^ 2
```




    6




```^``` Is another operation called [XOR](https://en.wikipedia.org/wiki/Exclusive_or) and will not concern us in this lesson.

 In python every operation has a priority. For example, multiplications and divisions are performed **before** additions and subtractions:



```python
10+6/2
```




    13.0




**Note:** It is better not to rely on the priority of actions since it might not be that obvious. To clearly set the priority of an operation we use parenthesis:



```python
10+(6/2)
```




    13.0




```python
(10+6)/2
```




    8.0




If an operation anywhere has a division **or** a decimal number, the result is decimal, otherwise it is an integer:



```python
2/2
```




    1.0




```python
2*2
```




    4




```python
2 + 2.0
```




    4.0




```python
2+2
```




    4




Python has one:
-  Synonym for 1: `True`
-  Synonym for 0: `False`



```python
True + 1
```




    2




```python
False + 1
```




    1




We will see more about `False` and `True` a bit later!



Although integers can have an unlimited number of digits, decimal numbers have a certain accuracy:



```python
5.123456789012345678901234567
```




    5.123456789012345




Why is this happening? An integer, no matter how large, can be represented in memory without losing accuracy. But for some decimals it is simply impossible to have infinite accuracy. For example:



```python
1/3
```




    0.3333333333333333




`1/3` has infinite decimal places! How do we store this in memory? The solution is to store a certain number of decimal places. Fortunately, there is an international [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754) standard that defines how we store decimal numbers. However, you can [instruct python](https://docs.python.org/3/library/decimal.html) not to use this template and handle decimals as accurately as you want (sacrificing memory and computing speed a bit).



### Alphanumeric (or otherwise: strings)



```python
"mitsos"
```




    'mitsos'




We can add two strings:



```python
'a' + 'b'
```




    'ab'




We can multiply a string by an integer:



```python
'a' * 10
```




    'aaaaaaaaaa'




There is also the empty string



```python
''
```




    ''




`len` returns the size of a string



```python
len("abcdefg")
```




    7




```python
len('')
```




    0




```Count``` returns how many times there is a string inside another string.



```python
"zabarakatranemia".count('a')
```




    6




```python
"zabarakatranemia".count('ra')
```




    2




```python
"zabarakatranemia".count('c')
```




    0




```index``` returns the index of the first occurence of a sub-string in a string.



```python
"zabarakatranemia".index('anemia')
```




    10




```python
# "ra" exists twice but index always returns the index
# of the first occurence.
"zabarakatranemia".index('ra') 
```




    4




If it does not exist then it raises an error!



```python
"zabarakatranemia".index('c')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-237-1515cc1d7dbe> in <module>()
    ----> 1 "zabarakatranemia".index('c')
    

    ValueError: substring not found



**Caution!** Two strings declared next to each other are considered one!



```python
"Hello" "world"
```




    'Helloworld'




A string can have characters in any language!



```python
a = "σε οποιαδίποτε γλώσσα ذا كيور (بالإنجليزية: The Cure) هي فرقة روك إنجليزية، تم تكوينها في كرولي، غرب ساسكس عام 1976. واجهت الفرقة عِدة تغيرات؛ مع "
print (a)
```

    σε οποιαδίποτε γλώσσα ذا كيور (بالإنجليزية: The Cure) هي فرقة روك إنجليزية، تم تكوينها في كرولي، غرب ساسكس عام 1976. واجهت الفرقة عِدة تغيرات؛ مع 



Yes, [emoji are](https://unicode.org/emoji/charts/full-emoji-list.html) included:



```python
print ("\U0001F621")
```

    😡



After this very brief introduction in python, we can talk in a more theoretical perspective:

#  Operators

 Operators are symbols or reserved words with which we apply basic operations to various expressions. For more you can read here: [https://en.wikipedia.org/wiki/Operator_(computer_programming](https://en.wikipedia.org/wiki/Operator_(computer_programming) )

 Some of the most basic operators that python supports are:
-  +
-  -
-  /
-  //
-  *
-  %
-  **
-  &lt;
-  &gt;
-  &lt;=
-  &gt; =
-  ! =
-  ==
-  and
-  or
-  not
-  in
-  is



### The + operator

The expressions that can include the ```+``` operator are:



```python
3+2
```




    5




```python
3+2.0
```




    5.0




```python
3+0.0
```




    3.0




```python
'ab' + 'cde' 
```




    'abcde'




```python
True + True + False
```




    2




```python
True + 2
```




    3




```python
True + 0.0
```




    1.0




```python
[1,2,3] + [4,5,6] # Lists, we will talk later about them!
```




    [1, 2, 3, 4, 5, 6]




### The operator -

 The operations allowed by the &#39;-&#39; operator are:



```python
3-2
```




    1




```python
3-7
```




    -4




```python
4-6.0
```




    -2.0




```python
True - True
```




    0




```python
True - 6.6
```




    -5.6




### The operator *

 The operations allowed with the &#39;*&#39; operator are:



```python
6*7
```




    42




```python
6.6*2
```




    13.2




```python
True * 2
```




    2




```python
True * False
```




    0




```python
True * 2.3
```




    2.3




```python
6 * 'hello'
```




    'hellohellohellohellohellohello'




```python
[1,2,3] * 5  # Λίστες, θα τα δούμε αργότερα..
```




    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]




### The &#39;/&#39; operator


Οι πράξεις που επιτρέπονται με τον τελεστή '/' είναι:


```python
4/5
```




    0.8




**CAUTION!!**



```python
5/0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-57-0106664d39e8> in <module>()
    ----> 1 5/0
    

    ZeroDivisionError: division by zero



```python
True/True
```




    1.0




```python
6/3
```




    2.0




```python
6.5/3
```




    2.1666666666666665




### The operator &#39;//&#39;

 This operator gives us the result of integer division



```python
5//2
```




    2




```python
11//3
```




    3




```python
6.5 // 2.1
```




    3.0




```python
True // 2
```




    0




### The ```%``` operator

 This operator gives us the remainder of the integer division



```python
5%2
```




    1




```python
5.2 % 2
```




    1.2000000000000002




```python
True % 2
```




    1




The ```%``` operator is used (not so often) to insert strings inside strings



```python
'my name is %s nice to meet you' % "mitsos"
```




    'my name is mitsos nice to meet you'




You can find [here](https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html) how you can use this operator for strings with more examples



### The operator **

 This operator returns the exponential $ a ^ b $



```python
3**2
```




    9




```python
3.2**2.3
```




    14.515932837559118




```python
True ** 2
```




    1




## Logical Operators

 We saw before the constants `True` and `False` . What is their purpose? So far we have seen operators who can generate numbers. For example the `+` operator can produce any number. But there is a group of operators that can only produce 2 different values. These values are `True` and `False`. These operators are:
-  The comparison operators ```<```,```>```, ```<=```,```>=```
-  The equality operators ```==```, ```!=```
-  The operators ```and```, ```or```, ```not```
-  The ```in```, ```is``` operators (we will talk about them later)

 These operators **always** return True or False to **whatever** we apply them!

  a < β checks if α is less than β:



```python
2<3 
```




    True




```python
3<2
```




    False




```python
3<3
```




    False




α <= β checks if α is less than or equal to β:



```python
2<=3
```




    True




```python
3<=2
```




    False




```python
3<=3
```




    True




α > β checks if α is greater than β:



```python
3 > 2
```




    True




```python
2 > 3
```




    False




```python
3 > 3
```




    False




α >= β checks if α is greater than or equal to β:



```python
3 >= 2
```




    True




```python
2 >= 3
```




    False




```python
3 >= 3
```




    True




The operator α == β checks if α is equal to β



```python
3==2
```




    False




```python
3==3
```




    True




```python
3==3.0
```




    True




```python
"3" == 3
```




    False




```python
16**0.5 == 4
```




    True




```python
'mitsos' == 'mits' + 'os'
```




    True




```python
3 == 6/2
```




    True




```python
True == True or False
```




    True




```python
3 == True + True + True + False
```




    True




```python
3 == 'mits' + 'os'
```




    False




```python
[1,2,3] == [1,2,3] # Λίστες, θα τα δούμε αργότερα
```




    True




```python
[1,2,3] == [2,1,3]
```




    False




The operator α != β if α is **not** equal to β



```python
3 != 2
```




    True




```python
2 != 2
```




    False




```python
2 != 2.0
```




    False




```python
1 != True
```




    False




```python
'hello' != ' hello '
```




    True




```python
'' != ''
```




    False




```python
'' != ' '
```




    True




We can also use the same operators ```<```, ```>```, ```<=```, ```>=``` more than once:



```python
2<3<4
```




    True




```python
2<3<3
```




    False



When we apply these operators to strings, then we compare them [alhabetical](https://en.wikipedia.org/wiki/Alphabetical_order). "Smaller" is considered the one that ib an alphabetical ordering has the lower index. 

Your phone uses exactly this method to sort your contacts! 


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




Sometimes we want to make a decision depending on whether 2 or more reasonable values are true. For example:

 I will go out if the weather is good **and** I have free time.

 I will go out if the weather is good **or** I have free time.

 So we have two additional logical operators: ```and``` , ```or``` .

Α and β are `True` if α and β are `True` , if one of α, β is `False` (or both), then the result is `False` :



```python
True and True
```




    True




```python
True and False
```




    False




```python
False and True
```




    False




```python
False and False
```




    False




```python
(1==1) and (2==3-1)
```




    True




```python
(1==1) and (2==3)
```




    False




```python
(1>=1) and (2<=2)
```




    True




Similarly the result of the operation α or β is `True` if one of α, β (or both) is `True` , otherwise it is `False` :



```python
True or True
```




    True




```python
True or False
```




    True




```python
False or True
```




    True




```python
False or False
```




    False




```python
1==2 or 1<=1
```




    True




```python
1>2 or 2<1
```




    False




```python
0==1 or True
```




    True




Finally, there is the `not` operator. This operator has the peculiarity that it is applied to a single value. `not` a, results in `False` if a is `True` and `True` if a is `False` :



```python
not True
```




    False




```python
not False
```




    True




```python
not 0
```




    True




```python
not 0.0000000001
```




    False




```python
not ''
```




    True




```python
not 1
```




    False




```python
not ' '
```




    False




```python
not 3==4
```




    True




```python
not 3==3
```




    False




```python
not "mitsos"=="Mitsos"
```




    True




```python
not "mitsos" == "mitsos"
```




    False




**Fun fact:** Your computer which does all sort of incredible things, in reality it can actually do only one operation: `not (a and b)` . This operation is called NAND. For example when the computer does a mathematical operation (eg `14.2 * 51.1` ), it "breaks" that operation into NAND operations. That is, the processor has billions of circuits that do this and that alone. But they are organized so that when combined in the right way they do all the arithmetic operations! [More](https://en.wikipedia.org/wiki/NAND_logic) . Even when your computer does something more complex (streaming, playing a game, controlling a nuclear reactor, guiding a spaceship) it still breaks all the operations needed in NAND operations.



### Back to strings!



All capitals:



```python
"abcde".upper()
```




    'ABCDE'




All lower:



```python
"ABCDE".lower()
```




    'abcde'




Replace one piece of string with another:



```python
"hello world".replace('l', "QQQ")
```




    'heQQQQQQo worQQQd'




We can remove the empty strings from the end and from the start of a string:



```python
"    hello    ".strip()
```




    'hello'




```python
"+++hello+++".strip('+')
```




    'hello'




```python
not "     "
```




    False




```python
not "     ".strip()
```




    True




Check if one string starts with another string:



```python
"heraklio".startswith('her')
```




    True




Check if one string ends with another string:



```python
"alex".endswith("lex")
```




    True




### Indexing

From strings (as with lists as we will see later), we can extract a subset by using `[]` . This feature is called indexing.



```python
print ("hello")
```

    hello



**Caution!** The numbering starts from 0!



```python
"hello"[0]
```




    'h'




```python
"hello"[1]
```




    'e'




**Caution!** The numbering should not exceed the size of the string!



```python
"hello"[100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-197-e6ccf1afaf71> in <module>()
    ----> 1 "hello"[100]
    

    IndexError: string index out of range



The index (or "numbering") can get negative values! `-1` is the last element. The `-2` is one before the last etc ..



```python
"hello"[-1]
```




    'o'




```python
"hello"[-2]
```




    'l'




```python
"hello"[-100]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-201-552ff00ad524> in <module>()
    ----> 1 "hello"[-100]
    

    IndexError: string index out of range



### Indexing spaces

 We can get a subset of a string based on the intervals that we define in `[]`



```python
"hello"[1:3]
```




    'el'




When we write `[a:b]` we mean "start from the first element (the numbering starts from 0!) And stop at the second element, BUT WITHOUT TAKING THIS !!"



```python
"hello"[1:4]
```




    'ell'




If we want to get a subset starting from the beginning of the string then we can write either `[0:b]` or `[:b]`



```python
"hello"[0:2]
```




    'he'




```python
"hello"[:2]
```




    'he'




If we want a subset that ends at the end of the string then we can write `[a:]`



```python
"hello"[2:]
```




    'llo'




### Indexing spaces with steps

 We can use `[a:b:c]` for indexing. This means: go from ```a``` to ```b``` (without taking ```b```!) with step: ```c```.



```python
"abcdefgij"[1:7:2]
```




    'bdf'




```python
"abcdefgij"[1:7:3]
```




    'be'




If we omit the first element then by default it assumes the value 0 (the beginning)



```python
"abcdefgij"[:7:3]
```




    'adg'




If we omit the second then by default it assumes the end of the string



```python
"abcdefgij"[1::3]
```




    'bei'




We can skip both so it will take from the beginning to the end of the string



```python
"abcdefgij"[::3]
```




    'adg'




If we omit the third then by default it uses 1



```python
"abcdefgij"[1:7:]
```




    'bcdefg'




Step cannot be 0!



```python
"abcdefgij"[1:7:0]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-219-96e6dd4da4bc> in <module>()
    ----> 1 "abcdefgij"[1:7:0]
    

    ValueError: slice step cannot be zero



### Negative indexing steps.

 Step `c` can be negative!



```python
"abcdefgij"[7:1:-1]
```




    'igfedc'




```python
"abcdefgij"[7:1:-2]
```




    'ifd'




```python
"abcdefgij"[7::-2]
```




    'ifdb'




```python
"abcdefgij"[::-2]
```




    'jgeca'




```python
"abcdefgij"[::-1] # Reverse a string! 
```




    'jigfedcba'




Useful when we have a cDNA sequence!



```python
"ACGT"[::-1]
```




    'TGCA'




Of course, we can use variables in these indexing spaces:



```python
a=3
"abcde"[0:a]
```




    'abc'




### Special Characters

We have said that with single or double quotes we can declare a string. But what happens when we want to include in a string a single or double quote? In that case we can use ```\``` or else backslash:



```python
print("mitsos")
```

    mitsos



```python
print("My name is \"mitsos\"")
```

    My name is "mitsos"



```python
print('My name is "mitsos"')
```

    My name is "mitsos"



```python
print ('My name is \'Mitsos\'')
```

    My name is 'Mitsos'



```python
print ("My name is 'Mitsos'")
```

    My name is 'Mitsos'



There are also the following special characters:
-  New line: `\n` (n = New line)
-  Tab: `\t`



```python
print("Line 1\nLine 2")
```

    Line 1
    Line 2



```python
print ("Col 1\tCol2")
```

    Col 1	Col2



In case we want to write a large string that has many special characters inside (quotes, new lines, etc ..) we can use the triple single or double quotes:



```python
print( '''
"Be realistic - demand the impossible!"
    Soyez réalistes, demandez l'impossible! - Anonymous graffiti, Paris 1968
''')
```

    
    "Be realistic - demand the impossible!"
        Soyez réalistes, demandez l'impossible! - Anonymous graffiti, Paris 1968
    



```python
print("""
"I have the simplest tastes. I am always satisfied with the best."
       Oscar Wilde
""")
```

    
    "I have the simplest tastes. I am always satisfied with the best."
           Oscar Wilde
    



### Combination of variables of different types



float ```+``` int result in float:



```python
3+0.0
```




    3.0




```python
0 + 0.0
```




    0.0




The division always results in float:



```python
5/2
```




    2.5




```python
6/2
```




    3.0



float/int και string δεν επιτρέπεται


```python
4.5 + "μίτσος"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-835a49c7937c> in <module>()
    ----> 1 4.5 + "μίτσος"
    

    TypeError: unsupported operand type(s) for +: 'float' and 'str'



when we mix float / int with boolean then True corresponds to 1 and False to 0:



```python
4 + True
```




    5




```python
4 * False
```




    0




```python
6 / True
```




    6.0




We can also do the following:



```python
'Μήτσος' * True # είναι το ίδιο με 'Μήτσος' * 1
```




    'Μήτσος'




```python
'Μήτσος' * False #  είναι το ίδιο με 'Μήτσος' * 0
```




    ''




### We can add True / False variables to each other!

 And in general we can do any mathematical operation



```python
True + True
```




    2




```python
True + False + True
```




    2




```python
(True + False) / (True + True)
```




    0.5




```python
True * True * True * True * True * True
```




    1




```python
True * True * True * True * False * True
```




    0




### The `and` and `or` operators with variables that are NOT boolean



Remember the operators `and` and `or` . E.g:



```python
True and False
```




    False




What if I use them with variables (or constants) that are NOT boolean?

The expression `Α and B and C and ... and Z` will return the first expression which is False. If there is none that is False, it will return the last one:



```python
5 and '' and 'Μήτσος'
```




    ''




```python
5 and 'Μήτσος' and 0.0
```




    0.0




```python
5 and 'Μήτσος' and 3.2
```




    3.2




But why is this happening? Because when in an expression of the form: ```A and B and C```, ```B``` is False, then it does not make sense to see what value is ```C```. Whether ```C``` is True or False, the result will always be False. So in essence python returns the value of the expression it last evaluated.



This technique is called [short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation)



Similary the following expression: ```A or B or C or ... or Z```, will return the first value which is True. If there is none that is True, then it will return the last one:



```python
0 or 5.3 or 'Μήτσος'
```




    5.3




```python
0 or 5.3 or ''
```




    5.3




```python
0 or False or ''
```




    ''




### Check the type of a value

 The `type` function returns a string that contains the type of a value:



```python
type(2)
```




    int




```python
type(2.0)
```




    float




```python
type('')
```




    str




```python
type('mitsos')
```




    str




```python
type(True)
```




    bool




```python
type(1==2)
```




    bool




```python
type(1+2)
```




    int




### Type conversion



These are some special functions to convert variables from one type to another:
-  `int` converts to integer
-  `float` converts to decimal
-  `bool` converts to binary
-  `str` converts to alphanumeric

 Some examples:



```python
int('42')
```




    42




```python
int('42.4')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-c0c93863b08a> in <module>()
    ----> 1 int('42.4')
    

    ValueError: invalid literal for int() with base 10: '42.4'



```python
int(42.4)
```




    42




```python
int(True)
```




    1




```python
int(False)
```




    0




```python
int(42)
```




    42




```python
int('mitsos')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-39-24e8b5b4a1dd> in <module>()
    ----> 1 int('mitsos')
    

    ValueError: invalid literal for int() with base 10: 'mitsos'



```python
int('                                 42')
```




    42




```python
int('42                                  ')
```




    42




```python
int('               42                    ')
```




    42




```python
float('3.4')
```




    3.4




```python
float('3')
```




    3.0




```python
float('')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-45-45d756431581> in <module>()
    ----> 1 float('')
    

    ValueError: could not convert string to float: 



```python
float('mitsos')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-46-a78f2c30f998> in <module>()
    ----> 1 float('mitsos')
    

    ValueError: could not convert string to float: 'mitsos'



```python
float('3.4             ')
```




    3.4




```python
float('   3.4           ')
```




    3.4




```python
float('               3.4')
```




    3.4




```python
float(3)
```




    3.0




```python
float(3.4)
```




    3.4




```python
float(True)
```




    1.0




```python
float(False)
```




    0.0




```python
bool(2)
```




    True




```python
bool(0)
```




    False




```python
bool(3.3)
```




    True




```python
bool(0.0)
```




    False




```python
bool(0.000000000001)
```




    True




```python
bool('mitsos')
```




    True




```python
bool('')
```




    False




```python
bool(' ')
```




    True




```python
bool(True)
```




    True




```python
bool(False)
```




    False




### Help and instructions

But this is a lot! How will I remember all of these?

You do not need to remember much .. You always have google .. if you ask "how to ... in python" usually the first result will have a very good answer! Recently [the creator of python](https://en.wikipedia.org/wiki/Guido_van_Rossum) said that he uses google himself to find out how to do some things in .. python.

Nevertheless python contains some basic instructions and documentation with the ```help``` function:



```python
help(len)
```

    Help on built-in function len in module builtins:
    
    len(obj, /)
        Return the number of items in a container.
    



```python
help("".count)
```

    Help on built-in function count:
    
    count(...) method of builtins.str instance
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
    



Try also:



```python
?len
```
