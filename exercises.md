
## Some notes 
* **NEVER USE python's [input](https://docs.python.org/3/library/functions.html#input) function**. You can test your code by simply calling your functions (see later) with some random/testing arguments.
* As you can see **all** the exercises request to create one (or more) python function(s). That means that ALL your implementation in a given exercise should reside in one (or more) functions. If your implementation is not in a function then it will take half points (5/10)
* As you can see on the description of every exercise you will have to write a function. That means that you have to take **special** attention to the following three items:
   1. Implement the exact parameters as the description. If the description mentions `create a function that takes one argument`. That means that you should create a function that takes exactly one argument (not two, not three and not zero).
   2. Add a `return` statement, except if the description says `this function does not return anything` (or something similar). If the description says `your function should return ....` and your function does not return anything, then the exercise will take half points (5/10). 
   3. Take special attention on the type of the variable that you have to return. If the description says "the function will return an integer", then you have to return an integer. If your function returns a type that is different from the one requested, the exercise will take half points (5/10).
* You don't have to check the type of the arguments from inside your functions. 
* If a description mentions that a function should return `True`/`False`. That means that the function should return a boolean value NOT a string value. For example `return "True"` is wrong! the correct is `return True`.
* **NEVER USE python's [input](https://docs.python.org/3/library/functions.html#input) function** (Saying it once is not enough)

## Basics arithmetics
### 1 
Create a function that takes as argument an integer value. The function should return:
* `True` if the number is in between `100<x<200`
* `False` Otherwise 

### 2 
Create a function that takes as argument an integer value. The function should return:
* `True` if the number has at least one even digit.
* `False` otherwise 

To test:
```python
f(135) # Returns False
f(245) # Returns True 
```
### 3
Create a function that takes as argument two numbers. The function will return a float number which is [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean) of these numbers. 


## Basics strings

### 4
Create a function that takes as argument a string. The function should return:
* `True` if the string contains at least one vowel (`a`, `e`, `i`, `o`, `u`, `y`) including capital vowels.
* `False` otherwise 

## If
### 5
Create a function that takes as argument three numbers. The function will return the middle number (according to a numerical ordering). You are not allowed to use `min`, `max`, `sort`, `sorted`. 


## Advanced strings 
### 6
Suppose the following string:
```python
a = '''
#CHROM  POS     ID      REF     ALT     QUAL
chr19   617614  .       G       A       39.2648
chr19   617804  .       G       A       0.309945
chr19   617959  .       A       C       0.0608339
chr19   618159  .       A       G       193.704
chr19   618428  .       T       G       1.87498E-5
chr19   618851  .       T       C       74.4613
chr19   618854  .       G       A       74.4613
chr19   618911  .       T       G       2.88308E-4
chr19   619021  .       G       C       352.245
chr19   619139  .       G       A       137.482
chr19   619408  .       A       G       207.722
chr19   619574  .       T       G       594.095
chr19   619772  .       G       C       612.352
chr19   619913  .       T       C       276.649
chr19   620004  .       T       C       0.00524165
chr19   620045  .       A       T       15.5734
chr19   620201  .       A       C       5.61107E-5
chr19   620210  .       A       C       1.63995E-5
chr19   620214  .       T       C       3.42253E-5
chr19   620228  .       A       C       8.62681E-4
chr19   620299  .       C       A       6.06919
chr19   620315  .       A       C       3.3417E-4
chr19   620381  .       T       G       5.01393E-4
chr19   620414  .       A       C       6.37073E-6
chr19   620429  .       T       C       2.46975E-5
chr19   620454  .       A       C       4.25049E-5
chr19   620459  .       T       C       4.96425E-5
chr19   620728  .       A       G       0.0198511
chr19   620807  .       G       A       41.4442 
'''
```

As you can see this string contains information regarding a list of mutations.  
* The first column is always chr19
* The second column contains a location in the chromosome
* The third column contains an id which is always `.`
* The forth column contains the reference nucleotide (can be either `A`,`C`,`G`,`T`)
* The fifth column contains the altenative nucleotide (can be either `A`,`C`,`G`,`T`)
* The sixth column contains a quality score. It is a decimal number

Write a function that takes as argument a string similar to `a`. The function will return a **dictionary** where the key is the position and the value is the quality score. For example it should:

```python
q = f(a)
print (q)
# It prints something like:
{
  617614 : 39.2648,
  617804 : 0.309945,
  ...
}
```

### 7
Suppose the following string:
```python
a = '''
#CHROM  POS     ID      REF     ALT     QUAL
chr19   617614  .       G       A       39.2648
chr19   617804  .       G       A       0.309945
chr19   617959  .       A       C       0.0608339
chr19   618159  .       A       G       193.704
chr19   618428  .       T       G       1.87498E-5
chr19   618851  .       T       C       74.4613
chr19   618854  .       G       A       74.4613
chr19   618911  .       T       G       2.88308E-4
chr19   619021  .       G       C       352.245
chr19   619139  .       G       A       137.482
chr19   619408  .       A       G       207.722
chr19   619574  .       T       G       594.095
chr19   619772  .       G       C       612.352
chr19   619913  .       T       C       276.649
chr19   620004  .       T       C       0.00524165
chr19   620045  .       A       T       15.5734
chr19   620201  .       A       C       5.61107E-5
chr19   620210  .       A       C       1.63995E-5
chr19   620214  .       T       C       3.42253E-5
chr19   620228  .       A       C       8.62681E-4
chr19   620299  .       C       A       6.06919
chr19   620315  .       A       C       3.3417E-4
chr19   620381  .       T       G       5.01393E-4
chr19   620414  .       A       C       6.37073E-6
chr19   620429  .       T       C       2.46975E-5
chr19   620454  .       A       C       4.25049E-5
chr19   620459  .       T       C       4.96425E-5
chr19   620728  .       A       G       0.0198511
chr19   620807  .       G       A       41.4442 
'''
```

As you can see this string contains information regarding a list of mutations.  
* The first column is always chr19
* The second column contains a location in the chromosome
* The third column contains an id which is always `.`
* The forth column contains the reference nucleotide (can be either `A`,`C`,`G`,`T`)
* The fifth column contains the altenative nucleotide (can be either `A`,`C`,`G`,`T`)
* The sixth column contains a quality score. It is a decimal number

Write a function that takes as argument a string similar to `a`. The function will return a **dictionary** where the key is the position and the value is a dictionary that will have a key 'REF' and a key 'ALT' containing all relevant values. For example it should:

```python
q = f(a)
print (q)
# It prints:
{
  617614 : {'REF': 'G', 'ALT': 'A'},
  617804 : {'REF': 'G', 'ALT': 'A'},
  617959 : {'REF': 'A', 'ALT': 'C'},
  ...
}
```


## Iterations 
### 8

Let the following function:
```python
import random

def f():
    l = [random.randint(100, 10000) for x in range(10_000)]
    return l
```

This function creates a list with 10.000 random integers from 100 to 10.000

Create a function that takes as argument a list similar to the one returned by `f`. The function should return an integer which is the maximum sum of digits for all numbers in the argument. 

### 9

Let the following function:
```python
import random

def f():
    l = [random.randint(100, 10000) for x in range(10_000)]
    return l
```

This function creates a list with 10.000 random integers from 100 to 10.000

Create a function that takes as argument a list, let `l` similar to the one returned by `f`. The function should return an integer which is the element in `l` that has the maximum sum of digits.

### 10
Let the following function:
```python
import random

def f():
    l = [random.randint(100, 10000) for x in range(1000)]
    return l
```
This function creates a list with 10.000 random integers from 100 to 10.000. 
Create a function that takes as argument a list, let `l` similar to the one returned by `f`. The function should return a **list** containing tuples. Each tuple should contain all possible pairs of number in `l` whose sum is equal to 2021. 

For example a possible return is:
```python
[(1012, 1009), (1672, 349), (818, 1203), (548, 1473), (952, 1069)]
```

Note 1: If the pair (a,b) is in the list, you do not have to also include the pair (b,a), but if you do this is not a mistake. 

### 11
Create a function that will take as an argument a list containing only strings. The function will return a **float number**: the average length of the strings. For example:
```python
a = ['mitsos', 'anna', 'epameinonas']
f(a) # Returns 7.0 ((6+4+11)/3)
```

### 12
Create a function that will take no arguments. The function will return a **list** with all number that are perfect squares from 100 to 10.000. A number `a` is perfect square if there exist an integer `b` such that b<sup>2</sup>=a. Some examples of perfect squares are: 100 (=10<sup>2</sup>), 121(=11<sup>2</sup>), 144(=12<sup>2</sup>), 225(=15<sup>2</sup>), 256(=16<sup>2</sup>).  



## Sets
### 13
Create a function that will take as argument 2 strings. The function will return:
* `True`: If all letters of the first string exist in the second string.
* `False`: Otherwise


For example:
```python
f("mpanana", "mpania") #  Returns True 
f("mpanana", "pania")  # Return False
```

## Files
### 14
The HUGO Gene Nomenclature Committee or else HGNC is a committee which is responsible for maintaining gene names along with information regarding their location and function.  

In this site: https://www.genenames.org/download/statistics-and-files/ there is a list with all datasets maintained from HGNC. You can see that these files are available in TSV (Tab Separated Values) and also in JSON. 

In this exercise you will have to download the first file titled "protein-coding gene". You will have to download two files:
* The file in TSV format: ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/tsv/locus_groups/protein-coding_gene.txt
* The file in JSON format: ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/json/locus_groups/protein-coding_gene.json

Create a function named `f_1` that will take as argument a string with the name of the TSV file. The function will return the number of genes that exist in the big arm of chromosome 17 (17q).

Create a function named `f_2` that will take as argument a string with the name of the JSON file. The function will return the number of genes that exist in the big arm of chromosome 17 (17q).

Note 1: In order to check if the gene is in 17q, just check if the field ```location``` contains the string ```17q```.  

## Regular Expressions 
### 15
Suppose we have the following string:
```
genes = '''
ADTRP: encoding protein Androgen-dependent TFPI-regulating protein
APOM: encoding protein Apolipoprotein M (6p21.33)
C6orf10: encoding protein Uncharacterized protein C6orf10 (6p21.32)
C6orf62: chromosome 6 open reading frame 62 (6p22.3)
C6orf89: chromosome 6 open reading frame 89 (6p21.2)
CDKAL1: CDK5 regulatory subunit associated protein 1 like 1 (6p22.3)
COL11A2: collagen, type XI, alpha 2(6p21.3)
CYP21A2: cytochrome P450, family 21, subfamily A, polypeptide 2 (6p21.33)
DHX16: DEAH-box helicase 16 (6p21.33)
DOM3Z: Decapping exoribonuclease (6p21.33)
DSP: Desmoplakin gene linked to cardiomyopathy (6p24.3)
ELOVL5: ELOVL fatty acid elongase 5 (6p12.1)
FBXO9: F-box protein 9 (6p12.1)
G6B: Protein G6b (6p21.33)
GCNT2: N-acetyllactosaminide beta-1,6-N-acetylglucosaminyl-transferase (6p24.3)
GMDS: GDP-mannose 4,6-dehydratase (6p25.3)
HCG4P11: HLA complex group 4 pseudogene 11
HFE: hemochromatosis (6p22.2)
HIST1H2AH: histone cluster 1 H2A family member h (6p22.1)
'''
```

Create a function named `f_1` that will take as input a string with the same structure as `genes`. The function will use regular expressions to parse this string and it will return a list with the names of all genes that it contains.

Create a function named `f_2` that will take as input a string with the same structure as `genes`. The function will use regular expressions to parse this string and it will return a dictionary. The keys will be the name of the gene and values will be the position of the gene as it is shown in the end of each line. For example it should:

```python
a = f_2(gene)
print (a)
# It should print something like:
{
  'APOM': '6p21.33',
  'C6orf10': '6p21.32',
  ...
}
```

Ignore lines that do not have a position (i.e. gene `HCG4P11`)

### 16
The following function downloads a file named `greek_words.txt` that contains almost all greek words (in total 407752). 
```python
import requests
def get_greek_words(fn='greek_words.txt'):
    url = 'https://www.dropbox.com/s/kqlivmkg6nl2v8l/102bc23ac61f14c16903613aa48fe1c6.txt?dl=1'

    r = requests.get(url, allow_redirects=True)
    if not r.ok:
        r.raise_for_status()

    with open(fn, 'x', encoding='utf-8') as f:
        f.write( str(r.content, encoding='utf8') )
```

The words are in lowercase except names that start with a capital letter. 

Now let's play the game [spelling-bee](https://www.nytimes.com/puzzles/spelling-bee) with Greek letters!

Suppose that we have a set of 7 letters arranged on the following "honeycomb":
```text

      Η
   Ο     Π
      Ν
   Ε     Λ
      Σ

```

The purpose of this game is to Locate as many as possible words greek that meet the following criteria:
* The word must be at least four letters long.
* The word must include the central letter. (`N` in our example)
* The word cannot include any letter beyond the seven given letters. 

* Four-letter words are worth 1 point each
* Five-letter words are worth 5 points 
* Six-letter words are worth 6 points
* Seven-letter words are worth 7 points, etc. 

Words that use all of the seven letters in the honeycomb are known as "pangrams" and earn 7 bonus points (in addition to the points for the length of the word). So in the above example, `ΠΕΛΟΠΟΝΝΗΣΟΣ` is worth 12+7 = 19 points.

Create a function that takes as an argument two strings. The first consists of 6 different greek capital characters, the second consist of a single character. These will consist the "honeycomb" (the first parameter with the 6 letters is the perimeter and the second with the single letter is the center of the honeycomb). The function will return the sum of the score of all greek letters that match the "honeycomb" according to the rules presented above. 

It is given that:
```python
f('ΟΗΠΕΛΣ', 'N') # Returns 463 
```

## Numpy 

### 17
The following function generates a list with a random time series with 1000 data points. For example this can be the closing stock price of a company for a period of 1000 days. 

```python
def f():
    a = []
    start = 100
    for x in range(1000):
        start += random.random() - 0.5
        a.append(start)
        
    return a
```

Write a function that takes one argument, let `l`. This argument is a list like the one returned by function `f`. The function should return 2 values a,b. These values should have the following properties:

1. ```a<b```
2. the value `l[b] - l[a]` has the maximum value over all possible values of a and b 

Another way of describing this exercise is: Given a time series that contains the stock price for a continuous period of time what are the two optimal days for buying and selling respectively? (We suppose that you cannot sell before you buy) 

<!--
   inspired by: http://varianceexplained.org/r/stock-changes/ 
-->

### 18
Create a function `f` that takes an integer number as an argument, let `a`. The function returns a list of length `a`. The list contains the birthday of random `a` people. Each birthday is a number from 1 to 365.

Create a function `g` that takes two integer numbers as arguments, let `a` and `b`. The function calls function `f` `b` times with the argument `a`. The function returns the percentage of times for which the returned list of `b` contains at least 2 equal numbers. 

Some examples: 
* if `f(5)` returns `[100, 150, 200, 250, 300]` then this list  does NOT contain at least 2 equal numbers
* if `f(5)` returns `[100, 100, 200, 250, 300]` then this list  does contain at least 2 equal numbers
* if `f(5)` returns `[100, 100, 200, 200, 300]` then this list  does contain at least 2 equal numbers
* if `f(5)` returns `[100, 100, 100, 250, 300]` then this list  does contain at least 2 equal numbers

Or else the function `g` returns the percentage of which the random list of people generated by `f` contains at least 2 people with the same birthday.

Create a function `h` the function does not take any parameter. The function creates a plot. On the X axis are the numbers from 2 to 50. On the Y axis is the value returned from `g` with the following arguments:
* `a` : the respective value of the X axis
* `b` : The value 1000

<!--
    Inspired by: http://varianceexplained.org/r/birthday-problem/ 
-->

### 19
Create a function that will take as an argument a 2D matrix array. The function will return a new array where all elements have been set to 0 except the elements that belong to the perimeter of the array. The perimeter of the array is the first and last row and first and the last column. For example:

```python
Α = np.array([
[1,2,3,4],
[5,6,7,8],
[9,0,1,2],
[3,4,5,6],])

B = f(A)
print (B)
# It should print:
array([[1, 2, 3, 4],
       [5, 0, 0, 8],
       [9, 0, 0, 2],
       [3, 4, 5, 6]])
```

### 20

Create a function that will take no argument. The function should:
* Create 10.000 random numpy arrays 3X3 with elements 0 or 1 (chosen randomly) so that that the absolute difference between the number of "1"s and "0"s is always 1. Or else the number of "1"s and "0"s should be either 5 and 4 or 4 and 5 respectively. 
* For each array it should check if the 1's win or 0's in a [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game. Some examples are:

1 wins:
```text
1 1 0
0 1 1
0 0 1
```

0 wins:
```text
0 1 1
1 0 1
1 0 0
```

Both win:
```text
0 0 0
1 1 1
0 1 1
```

No one wins
```text
1 0 1
0 0 1
1 1 0
```

* The function should return the ratio: ``` (1_wins + 0_wins / ( both_win + no_one_wins ) ```

## Pandas 
### 21

The following function returns a pandas DataFrame with the population of Greece cities according to the 1991, 2001 and 2011 census. Every city belongs to one region. [data are from wikipedia](https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Greece)

```python
import pandas as pd
import json

def load_cities():
  s = '''{"Rank": {"0": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "10": 11, "11": 12, "12": 13, "13": 14, "14": 15, "15": 16, "16": 17, "17": 18, "18": 19, "19": 20, "20": 21, "21": 22, "22": 23, "23": 24, "24": 25, "25": 26, "26": 27, "27": 28, "28": 29, "29": 30, "30": 31, "31": 32, "32": 33, "33": 34, "34": 35, "35": 36, "36": 37, "37": 38, "38": 39, "39": 40, "40": 41, "41": 42, "42": 43, "43": 44, "44": 45, "45": 46, "46": 47, "47": 48, "48": 49, "49": 50, "50": 51, "51": 52, "52": 53, "53": 54, "54": 55, "55": 56, "56": 57, "57": 58, "58": 59, "59": 60, "60": 61, "61": 62, "62": 63, "63": 64, "64": 65, "65": 66, "66": 67, "67": 68, "68": 69, "69": 70, "70": 71, "71": 72, "72": 73, "73": 74, "74": 75, "75": 76, "76": 77, "77": 78, "78": 79, "79": 80, "80": 81, "81": 82, "82": 83, "83": 84, "84": 85, "85": 86, "86": 87, "87": 88, "88": 89, "89": 90, "90": 91, "91": 92, "92": 93, "93": 94, "94": 95, "95": 96, "96": 97, "97": 98, "98": 99, "99": 100, "100": 101, "101": 102, "102": 103, "103": 104, "104": 105, "105": 106, "106": 107, "107": 108, "108": 109, "109": 110, "110": 111, "111": 112, "112": 113, "113": 114, "114": 115, "115": 116, "116": 117, "117": 118, "118": 119, "119": 120, "120": 121, "121": 122, "122": 123, "123": 124, "124": 125, "125": 126, "126": 127, "127": 128, "128": 129, "129": 130, "130": 131, "131": 132, "132": 133, "133": 134, "134": 135, "135": 136, "136": 137, "137": 138, "138": 139, "139": 140, "140": 141, "141": 142, "142": 143, "143": 144}, "City": {"0": "Athens", "1": "Thessaloniki", "2": "Patras", "3": "Piraeus", "4": "Larissa", "5": "Heraklion", "6": "Peristeri", "7": "Kallithea", "8": "Acharnes", "9": "Kalamaria", "10": "Nikaia", "11": "Glyfada", "12": "Volos", "13": "Ilio", "14": "Ilioupoli", "15": "Keratsini", "16": "Evosmos", "17": "Chalandri", "18": "Nea Smyrni", "19": "Marousi", "20": "Agios Dimitrios", "21": "Zografou", "22": "Egaleo", "23": "Nea Ionia", "24": "Ioannina", "25": "Palaio Faliro", "26": "Korydallos", "27": "Trikala", "28": "Vyronas", "29": "Agia Paraskevi", "30": "Galatsi", "31": "Agrinio", "32": "Chalcis", "33": "Petroupoli", "34": "Serres", "35": "Alexandroupoli", "36": "Xanthi", "37": "Katerini", "38": "Kalamata", "39": "Kavala", "40": "Chania", "41": "Lamia", "42": "Komotini", "43": "Irakleio", "44": "Rhodes", "45": "Kifissia", "46": "Stavroupoli", "47": "Chaidari", "48": "Drama", "49": "Veria", "50": "Alimos", "51": "Kozani", "52": "Polichni", "53": "Karditsa", "54": "Sykies", "55": "Ampelokipoi", "56": "Pylaia", "57": "Agioi Anargyroi", "58": "Argyroupoli", "59": "Ano Liosia", "60": "Nea Ionia", "61": "Rethymno", "62": "Ptolemaida", "63": "Tripoli", "64": "Cholargos", "65": "Vrilissia", "66": "Aspropyrgos", "67": "Corinth", "68": "Gerakas", "69": "Metamorfosi", "70": "Giannitsa", "71": "Voula", "72": "Kamatero", "73": "Mytilene", "74": "Neapoli", "75": "Eleftherio-Kordelio", "76": "Chios", "77": "Agia Varvara", "78": "Kaisariani", "79": "Nea Filadelfeia", "80": "Moschato", "81": "Perama", "82": "Salamina", "83": "Eleusis", "84": "Corfu", "85": "Pyrgos", "86": "Megara", "87": "Kilkis", "88": "Dafni", "89": "Thebes", "90": "Melissia", "91": "Argos", "92": "Arta", "93": "Artemida", "94": "Livadeia", "95": "Pefki", "96": "Oraiokastro", "97": "Aigio", "98": "Kos", "99": "Koropi", "100": "Preveza", "101": "Naousa", "102": "Orestiada", "103": "Peraia", "104": "Edessa", "105": "Florina", "106": "Panorama", "107": "Nea Erythraia", "108": "Elliniko", "109": "Amaliada", "110": "Pallini", "111": "Sparta", "112": "Agios Ioannis Rentis", "113": "Thermi", "114": "Vari", "115": "Nea Makri", "116": "Tavros", "117": "Alexandreia", "118": "Menemeni", "119": "Paiania", "120": "Kalyvia Thorikou", "121": "Nafplio", "122": "Drapetsona", "123": "Efkarpia", "124": "Papagou", "125": "Nafpaktos", "126": "Kastoria", "127": "Grevena", "128": "Pefka", "129": "Nea Alikarnassos", "130": "Missolonghi", "131": "Gazi", "132": "Ierapetra", "133": "Kalymnos", "134": "Rafina", "135": "Loutraki", "136": "Agios Nikolaos", "137": "Ermoupoli", "138": "Ialysos", "139": "Mandra", "140": "Tyrnavos", "141": "Glyka Nera", "142": "Ymittos", "143": "Neo Psychiko"}, "Census 1991": {"0": 772072, "1": 383967, "2": 152570, "3": 182671, "4": 112777, "5": 115270, "6": 137288, "7": 194233, "8": 61052, "9": 80698, "10": 87597, "11": 63306, "12": 77192, "13": 78326, "14": 75037, "15": 71982, "16": 28821, "17": 66285, "18": 69749, "19": 64092, "20": 57574, "21": 80492, "22": 78563, "23": 60635, "24": 56699, "25": 61371, "26": 63184, "27": 45835, "28": 58523, "29": 47463, "30": 57230, "31": 52081, "32": 51646, "33": 38278, "34": 50017, "35": 37904, "36": 37430, "37": 43613, "38": 43625, "39": 56571, "40": 50077, "41": 44084, "42": 37036, "43": 42905, "44": 42400, "45": 39166, "46": 37596, "47": 44831, "48": 37604, "49": 37858, "50": 32024, "51": 31553, "52": 27894, "53": 30067, "54": 34059, "55": 40093, "56": 20785, "57": 30739, "58": 31530, "59": 21397, "60": 27904, "61": 23420, "62": 25125, "63": 22429, "64": 33691, "65": 16571, "66": 15715, "67": 27412, "68": 8512, "69": 21052, "70": 22504, "71": 17998, "72": 17410, "73": 23971, "74": 30568, "75": 16549, "76": 22894, "77": 28706, "78": 26701, "79": 25261, "80": 22039, "81": 24119, "82": 22567, "83": 22793, "84": 31359, "85": 28465, "86": 20403, "87": 12139, "88": 24152, "89": 19505, "90": 13469, "91": 21901, "92": 19087, "93": 9485, "94": 18437, "95": 17987, "96": 5458, "97": 22178, "98": 14714, "99": 12790, "100": 13695, "101": 19794, "102": 12691, "103": 2949, "104": 17128, "105": 12355, "106": 10275, "107": 12993, "108": 13517, "109": 15232, "110": 8021, "111": 13011, "112": 14218, "113": 5156, "114": 8488, "115": 12120, "116": 15456, "117": 12109, "118": 12932, "119": 9710, "120": 8488, "121": 11897, "122": 13094, "123": 3480, "124": 13974, "125": 10854, "126": 14775, "127": 9345, "128": 3561, "129": 10683, "130": 10916, "131": 1395, "132": 9541, "133": 10543, "134": 7752, "135": 9388, "136": 8093, "137": 13030, "138": 7193, "139": 10012, "140": 12028, "141": 5813, "142": 11671, "143": 12023}, "Census 2001": {"0": 745514, "1": 363987, "2": 160400, "3": 175697, "4": 124394, "5": 130914, "6": 137918, "7": 109609, "8": 75329, "9": 87255, "10": 93086, "11": 80409, "12": 82439, "13": 80859, "14": 75904, "15": 76102, "16": 52624, "17": 71684, "18": 73986, "19": 69470, "20": 65173, "21": 76115, "22": 74046, "23": 66017, "24": 61629, "25": 64759, "26": 67456, "27": 48686, "28": 61102, "29": 56836, "30": 58042, "31": 54523, "32": 53584, "33": 48327, "34": 54266, "35": 48885, "36": 45111, "37": 50510, "38": 49154, "39": 58663, "40": 53373, "41": 46406, "42": 43326, "43": 45926, "44": 52318, "45": 43929, "46": 41653, "47": 45227, "48": 42501, "49": 42794, "50": 38047, "51": 35242, "52": 36146, "53": 32031, "54": 41726, "55": 40959, "56": 22744, "57": 32957, "58": 33158, "59": 26423, "60": 30804, "61": 27868, "62": 28679, "63": 25520, "64": 32166, "65": 25582, "66": 27741, "67": 29787, "68": 13921, "69": 26448, "70": 26296, "71": 25532, "72": 22234, "73": 27247, "74": 29995, "75": 21630, "76": 23779, "77": 30562, "78": 26323, "79": 24112, "80": 23153, "81": 25720, "82": 25730, "83": 25863, "84": 28185, "85": 23274, "86": 23032, "87": 17430, "88": 23674, "89": 21211, "90": 19526, "91": 24239, "92": 19435, "93": 17391, "94": 20061, "95": 19887, "96": 11896, "97": 21061, "98": 17890, "99": 15860, "100": 16321, "101": 19870, "102": 15246, "103": 13306, "104": 18253, "105": 14279, "106": 14552, "107": 15439, "108": 16740, "109": 18261, "110": 12552, "111": 14817, "112": 15060, "113": 11360, "114": 10998, "115": 13986, "116": 14963, "117": 13229, "118": 14910, "119": 12855, "120": 12202, "121": 13822, "122": 12944, "123": 6598, "124": 13207, "125": 12924, "126": 14813, "127": 10177, "128": 6434, "129": 11551, "130": 12225, "131": 8018, "132": 11678, "133": 10149, "134": 11352, "135": 11383, "136": 10080, "137": 11799, "138": 10107, "139": 10947, "140": 11116, "141": 6623, "142": 11139, "143": 10848}, "Census 2011": {"0": 664046, "1": 315196, "2": 167446, "3": 163688, "4": 144651, "5": 140730, "6": 139981, "7": 100641, "8": 99346, "9": 91279, "10": 89380, "11": 87305, "12": 86046, "13": 84793, "14": 78153, "15": 77077, "16": 74686, "17": 74192, "18": 73076, "19": 72333, "20": 71294, "21": 71026, "22": 69946, "23": 67134, "24": 65574, "25": 64021, "26": 63445, "27": 61653, "28": 61308, "29": 59704, "30": 59345, "31": 59329, "32": 59125, "33": 58979, "34": 58287, "35": 57812, "36": 56122, "37": 55997, "38": 54100, "39": 54027, "40": 53910, "41": 52006, "42": 50990, "43": 49642, "44": 49541, "45": 47332, "46": 46008, "47": 45642, "48": 44823, "49": 43158, "50": 41720, "51": 41066, "52": 39332, "53": 38554, "54": 37753, "55": 37381, "56": 34625, "57": 34168, "58": 34097, "59": 33565, "60": 32661, "61": 32468, "62": 32127, "63": 30866, "64": 30840, "65": 30741, "66": 30251, "67": 30176, "68": 29939, "69": 29891, "70": 29789, "71": 28364, "72": 28361, "73": 27871, "74": 27084, "75": 27067, "76": 26850, "77": 26550, "78": 26370, "79": 25734, "80": 25441, "81": 25389, "82": 25370, "83": 24910, "84": 24838, "85": 24359, "86": 23456, "87": 22914, "88": 22913, "89": 22883, "90": 22741, "91": 22209, "92": 21895, "93": 21488, "94": 21379, "95": 21352, "96": 20852, "97": 20422, "98": 19432, "99": 19164, "100": 19042, "101": 18882, "102": 18426, "103": 18326, "104": 18229, "105": 17686, "106": 17444, "107": 17379, "108": 17259, "109": 16763, "110": 16415, "111": 16239, "112": 16050, "113": 16004, "114": 15855, "115": 15554, "116": 14972, "117": 14821, "118": 14746, "119": 14595, "120": 14424, "121": 14203, "122": 13968, "123": 13905, "124": 13699, "125": 13415, "126": 13387, "127": 13137, "128": 13052, "129": 12925, "130": 12785, "131": 12606, "132": 12355, "133": 12324, "134": 12168, "135": 11564, "136": 11421, "137": 11407, "138": 11331, "139": 11327, "140": 11069, "141": 11049, "142": 10715, "143": 10137}, "Region": {"0": "Attica", "1": "Central Macedonia", "2": "Western Greece", "3": "Attica", "4": "Thessaly", "5": "Crete", "6": "Attica", "7": "Attica", "8": "Attica", "9": "Central Macedonia", "10": "Attica", "11": "Attica", "12": "Thessaly", "13": "Attica", "14": "Attica", "15": "Attica", "16": "Central Macedonia", "17": "Attica", "18": "Attica", "19": "Attica", "20": "Attica", "21": "Attica", "22": "Attica", "23": "Attica", "24": "Epirus", "25": "Attica", "26": "Attica", "27": "Thessaly", "28": "Attica", "29": "Attica", "30": "Attica", "31": "Western Greece", "32": "Central Greece", "33": "Attica", "34": "Central Macedonia", "35": "Eastern Macedonia and Thrace", "36": "Eastern Macedonia and Thrace", "37": "Central Macedonia", "38": "Peloponnese", "39": "Eastern Macedonia and Thrace", "40": "Crete", "41": "Central Greece", "42": "Eastern Macedonia and Thrace", "43": "Attica", "44": "South Aegean", "45": "Attica", "46": "Central Macedonia", "47": "Attica", "48": "Eastern Macedonia and Thrace", "49": "Central Macedonia", "50": "Attica", "51": "Western Macedonia", "52": "Central Macedonia", "53": "Thessaly", "54": "Central Macedonia", "55": "Central Macedonia", "56": "Central Macedonia", "57": "Attica", "58": "Attica", "59": "Attica", "60": "Thessaly", "61": "Crete", "62": "Western Macedonia", "63": "Peloponnese", "64": "Attica", "65": "Attica", "66": "Attica", "67": "Peloponnese", "68": "Attica", "69": "Attica", "70": "Central Macedonia", "71": "Attica", "72": "Attica", "73": "North Aegean", "74": "Central Macedonia", "75": "Central Macedonia", "76": "North Aegean", "77": "Attica", "78": "Attica", "79": "Attica", "80": "Attica", "81": "Attica", "82": "Attica", "83": "Attica", "84": "Ionian Islands", "85": "Western Greece", "86": "Attica", "87": "Central Macedonia", "88": "Attica", "89": "Central Greece", "90": "Attica", "91": "Peloponnese", "92": "Epirus", "93": "Attica", "94": "Central Greece", "95": "Attica", "96": "Central Macedonia", "97": "Western Greece", "98": "South Aegean", "99": "Attica", "100": "Epirus", "101": "Central Macedonia", "102": "Eastern Macedonia and Thrace", "103": "Central Macedonia", "104": "Central Macedonia", "105": "Western Macedonia", "106": "Central Macedonia", "107": "Attica", "108": "Attica", "109": "Western Greece", "110": "Attica", "111": "Peloponnese", "112": "Attica", "113": "Central Macedonia", "114": "Attica", "115": "Attica", "116": "Attica", "117": "Central Macedonia", "118": "Central Macedonia", "119": "Attica", "120": "Attica", "121": "Peloponnese", "122": "Attica", "123": "Central Macedonia", "124": "Attica", "125": "Western Greece", "126": "Western Macedonia", "127": "Western Macedonia", "128": "Central Macedonia", "129": "Crete", "130": "Western Greece", "131": "Crete", "132": "Crete", "133": "South Aegean", "134": "Attica", "135": "Peloponnese", "136": "Crete", "137": "South Aegean", "138": "South Aegean", "139": "Attica", "140": "Thessaly", "141": "Attica", "142": "Attica", "143": "Attica"}}'''

  return pd.DataFrame(json.loads(s))
```

Create a function that will not take any argument. The function will return the total population of the cities belonging to the region: ```Crete``` according to the census of 2011. 


### 22
Create a function that will not take any argument. The function will use the ```load_cities``` function and it will return a new DataFrame which will contain the city with the largest population for every region according to the census of 2011. 

### 23
Create a function that will not take any argument. The function will use the ```load_cities``` function to create a barplot where it will show for each region 2 bars: one for the census of 1991 and one for the census of 2011. Every bar will contain the total population for all cities belonging on this region. The function should not return anything.

The plot should look like this:

![img](https://i.imgur.com/UekhSPu.png)


## Plotting 

### 24

For the following exercise you might have to install the [requests](https://docs.python-requests.org/en/master/) library. In jupyter you can do this with:

```text
! pip install requests
```

The following function returns the number of scientific papers that have been published in a given year that contain a given word:

```python
import requests

def pubmed_results(year, search):
    
    url_p = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(ABSTRACT:%22{search}%22)+AND+(FIRST_PDATE:[{year}-01-01+TO+{year}-12-31])&format=JSON'
    url = url_p.format(
        year = year,
        search = search,
    )
    r = requests.get(url)
    if not r.ok:
        r.raise_for_status()
        
    j = r.json()
    hit_count = int(j['hitCount'])
    return hit_count
```

For example how many papers have been published in 2013 containing in their abstract the word: `CRISPR`?

```python
pubmed_results(2013, "CRISPR")
```

Create a function that will not take any argument. The function should create barplot with the number of papers containing the word `python` and `perl` for all years from 2000 until 2020. 

The plot show have the savr structure as this plot showing the woldlife population of dolphins and whales over a period of time. 

![img](https://www.excel-easy.com/examples/images/column-chart/column-chart.png)


### 25

For the following exercise you might have to install the [requests](https://docs.python-requests.org/en/master/) library. In jupyter you can do this with:

```text
! pip install requests
```

The following function returns the number of scientific papers that have been published in a given year that contain a given word:

```python
import requests

def pubmed_results(year, search):
    
    url_p = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(ABSTRACT:%22{search}%22)+AND+(FIRST_PDATE:[{year}-01-01+TO+{year}-12-31])&format=JSON'
    url = url_p.format(
        year = year,
        search = search,
    )
    r = requests.get(url)
    if not r.ok:
        r.raise_for_status()
        
    j = r.json()
    hit_count = int(j['hitCount'])
    return hit_count
```

For example how many papers have been published in 2013 containing in their abstract the word: `CRISPR`?

```python
pubmed_results(2013, "CRISPR")
```

Create a function that will not take any argument. The function will create a scatter plot. X axis will be the years from 2010 to 2020. Y axis will contain the number of publications that contain the word `python` with red dots and the number of publications that contain the word `perl` with blue dots.





