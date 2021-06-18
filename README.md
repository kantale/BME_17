# BME_17
This page contains notes. exercises, project descriptions and other material relevant to the [Biomedical Engineering MSc](https://www.bme-crete.edu.gr/en/home) program that is held in coordination with [University of Crete](https://en.uoc.gr/), [Technical University of Crete](https://www.tuc.gr/index.php) and the [Foundation for Research and Technology-Hellas](https://www.forth.gr/)

### Lectures
1. Python basics . [html](notes/python_basics.html), [markdown](notes/python_basics.md), [ipynb](notes/python_basics.ipynb), [pdf](notes/python_basics.pdf)
2. Variables, functions and the if syntax . [html](notes/python_vars_if_functions.html), [markdown](notes/python_vars_if_functions.md), [ipynb](notes/python_vars_if_functions.ipynb), [pdf](notes/python_vars_if_functions.pdf)
3. Lists [html](notes/python_lists.html), [markdown](notes/python_lists.md), [ipynb](notes/python_lists.ipynb), [pdf](notes/python_lists.pdf).
4. List comprehension . [html](notes/python_list_comprehensions.html), [markdown](notes/python_list_comprehensions.md), [ipynb](notes/python_list_comprehensions.ipynb), [pdf](notes/python_list_comprehensions.pdf).
5. While, dictionary, tuples, sets . [html](notes/python_while_dictionary_tuples_sets.html), [markdown](notes/python_while_dictionary_tuples_sets.md), [ipynb](notes/python_while_dictionary_tuples_sets.ipynb), [pdf](notes/python_while_dictionary_tuples_sets.pdf). 
6. Files, lambda, string formatting, ternary operator, is operator, variable scoping . [html](notes/python_files_tern_lambda_sf_is.html), [markdown](notes/python_files_tern_lambda_sf_is.md), [ipynb](notes/python_files_tern_lambda_sf_is.ipynb), [pdf](notes/python_files_tern_lambda_sf_is.pdf). 
7. Generators, Exceptions, Collections . [html](notes/python_gen_imp_cons_exc.html), [markdown](notes/python_gen_imp_cons_exc.md), [ipynb](notes/python_gen_imp_cons_exc.ipynb), [pdf](notes/python_gen_imp_cons_exc.pdf).  
8. Serialization, itertools, Regular expressions . [html](notes/python_ser_iter_re.html), [markdown](notes/python_ser_iter_re.md), [ipynb](notes/python_ser_iter_re.ipynb), [pdf](notes/python_ser_iter_re.pdf).  
9. Pandas . [html](notes/python_pandas.html), [markdown](notes/python_pandas.zip), [ipynb](notes/python_pandas.ipynb), [pdf](notes/python_pandas.pdf).  
10. Numpy . [html](notes/python_numpy.html), [markdown](notes/python_numpy.zip), [ipynb](notes/python_numpy.ipynb), [pdf](notes/python_numpy.pdf).  
11. Plotting . [html](notes/python_matplotlib.html), [markdown](notes/python_matplotlib.zip), [ipynb](notes/python_matplotlib.ipynb), [pdf](notes/python_matplotlib.pdf).  

### Regarding copying
Both the Exercises and the Project of this course are assigned individually. You are allowed to discuss potential problems and solutions with your colleagues (I cannot prevent that), but copying and sharing solutions is strictly prohibited. Keep in mind: the programming code that is written by amateurs (in programming) tends to be highly personal. A code that has been shared is very easily identifiable even if various tricks (i.e. change of variable names) have been used. Incidents of copying will be reported and a grade of zero will be assigned.  

### Exercises 
[In this repository there is a file containing 25 exercises](exercises.md). These exercises are covering easy to medium common programming tasks. The deadline for delivering your solutions is *TBA*. 

#### How to hand over solutions
To hand over solutions send an email to [kantale@ics.forth.gr](mailto:kantale@ics.forth.gr). On the subject or on the beginning of your email you will have to mention your name. On the mail you will have to copy-paste the solutions one after the other. On the top of each solution there should exist a python comment in the following format: 

```python
# exercise <NUMBER>
```

For example. Suppose that the exercise is:

> Exercise: 11
>
> Write a function that will take as arguments two numbers. The function should return the sum of these two numbers. 
>

The part of your email that will contain the solution to this exercise should be:

```python

# exercise 11
def f(a,b):
    return a+b
```

Although this is the recommended way of handing over exercises other options are:
* Attachments with .py files. Again on the top of each solution there should be a comment as described before.
* Attachments with .ipynb files. Do not forget to add the python comment with the number of the exercise as described before. This comment should be in the same cell with the one containing your solution.

To save the exercises in .ipynb or in .py format from jupyter: Go to File --> Download as -> Python (or Notebook). Then you can send me as an attachment the downloaded file:

![img](https://i.imgur.com/jm2tmHm.png) 

**ATTENTION The following formats are not accepted:**
* pdf, Microsoft Word doc, Open Office, Libre Office, files 
* Compressed files 
* Screenshots 

#### How are the exercises graded?
Every exercise is graded from 0 to 10. All exercises have the same weight. The logic of grading is the following:
* Grade 0. No solution was handed over.
* Grade 1. Wrong results. Some basic structure of the solutions has been drafted.
* Grade 2. Wrong results. A very small part of the solution has been implemented.
* Grade 3. Wrong results. A significant part of the solution has been implemented. 
* Grade 4. Wrong results. The complete structure has been implemented but is contains important logic errors.
* Grade 5. Wrong results. The complete structure has been implemented but it contains less important logic errors.
* Grade 6. Wrong results. The complete structure has been implemented but is contains minor logic errors.
* Grade 7. Correct results, but not for all possible scenarios / inputs
* Grade 8. Correct results, with wrong logic! (this happens many times..)
* Grade 9. Correct results, with correct logic, but there is one obvious better / more efficient solution. 
* Grade 10. Flawless implementation. Bravo!

### Project 
[The project is described here](project.md).

You should deliver an implementation of the project by *TBA* 

In your email you should include:
* Your code which it should be one or more python (.py) files. 
* A report that should include:
   * A description of how to run the program.
   * A description of the general structure of the code 
   * A discussion that should include: 
      * How is the pressure to local healthcare systems (parameter `M`) is affected according to the rest of the parameters? 
      * Add 4-5 examples of plots demonstrating your findings 
   * A section that should include your opinion regarding the project. Did it help you understand some concepts in programming? What is the most difficult part? Do you have any suggestions for improvement?. This last section is not going to be graded.. it is a chance to get some feedback regarding the project itself.

### Programming with python additional material
* Official Documentation / General links
   * [Python documentation](https://docs.python.org/3/)
   * [The official Python Tutorial](https://docs.python.org/3/tutorial/index.html)
   * [Wikipedia](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
* Courses / Books / Textbooks 
   * [CS61A: Online Textbook ](https://inst.eecs.berkeley.edu//~cs61a/sp12/book/). Ευχαριστώ τον Ιωάννη-Ραφαήλ Τζονευράκη για το link. 
   * [Python Computing for Data Science](https://github.com/profjsb/python-seminar)
   * [EbookFoundation free-programming-books on python](https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md#python)
* Cheatsheets 
   * [pythoncheatsheet](https://www.pythoncheatsheet.org/) . Πολύ καλό και "συμπαγές" σημείο αναφοράς. Χρήσιμο όταν έχεις ξεχάσει πως γίνεται κάτι.
   * [Scientific Python Cheatsheet](https://ipgp.github.io/scientific_python_cheat_sheet/) 
   * [Matplotlib Cheatsheet](https://twitter.com/magnumdessert/status/1280543694760710144)
* For Beginners
   * [A beginner's python tutorial](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial)
   * [A Python course that takes beginners seriously](https://github.com/JdeH/LightOn)
   * [Beginner's Python Cheat Sheets](https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/)
   * [Practical Python Programming from David Beazley](https://dabeaz-course.github.io/practical-python/)
   * [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) Practical programming for total beginners. Written by Al Sweigart. Free to read under a Creative Commons license.
* More advanced  
   * [Python: Notes for professionals book](https://books.goalkicker.com/PythonBook/)
   * [Non-beginner's python cheat sheet](https://gto76.github.io/python-cheatsheet/)
   * [Python Programming And Numerical Methods: A Guide For Engineers And Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)
   * [Python & APIs: A Winning Combo for Reading Public Data](https://realpython.com/python-api/)
   * [Recursion in Python: An Introduction](https://realpython.com/python-recursion/)
* Challenges: 
   * https://www.hackerrank.com/dashboard
   * https://stepik.org  
   * http://rosalind.info/problems/locations/ 
* NumPy
   * [NumPy Tutorial](https://realpython.com/numpy-tutorial/)
   * [NumPy: the absolute basics for beginners](https://numpy.org/devdocs/user/absolute_beginners.html)
   * [NumPy Illustrated: The Visual Guide to NumPy](https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d), from Lev Maximov 
   * [Cheatsheet 1](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
   * [Cheatsheet 2](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)
* Scipy
   * [Paper στο Nature για το scipy](https://www.nature.com/articles/s41592-019-0686-2) published: 3 February 2020
   * [scipy lectures](http://scipy-lectures.org/)
* Pandas:
   * [Cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
   * [Introduction to Pandas](https://realpython.com/pandas-dataframe/) . [plotting with pandas](https://realpython.com/pandas-plot-python/)
   * [100 pandas puzzles](https://github.com/ajcr/100-pandas-puzzles)
* Plotting
   * [Visualizing Data in Python Using plt.scatter()](https://realpython.com/visualizing-python-plt-scatter/)
* Regular Expressions
   * [Python Regex Cheatsheet](https://www.debuggex.com/cheatsheet/regex/python)
   * Debugging 
      * https://www.debuggex.com/
      * https://regexr.com/
* Jupyter
   * [Jupyter notebooks for teaching/learning Python 3](https://github.com/jerry-git/learn-python3)
   * Γιατί jupyter; https://www.nature.com/articles/d41586-018-07196-1 
   * [28 Jupyter Notebook tips, tricks and shortcuts - Dataquest](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/).  Ευχαριστώ τον Thimo Kristani για το link. 
* Tips & Tricks
   * 100 Helpful Python Tips You Can Learn Before Finishing Your Morning Coffee https://towardsdatascience.com/100-helpful-python-tips-you-can-learn-before-finishing-your-morning-coffee-eb9c39e68958 
* Forums & QAs 
   * https://www.reddit.com/r/bioinformatics/ 
   * https://bioinformatics.stackexchange.com/ 
   * https://www.biostars.org/ 



