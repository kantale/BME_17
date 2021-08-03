<!-- https://github.com/kantale/python_lessons/blob/master/assignment_5.ipynb -->

Suppose that a town has a population of `P`. 
Each individual is living in a single house. 
The town is hit by the new coronavirus pandemic!
The virus is spread in the town with the following characteristics:

* Every day `N` random people (cheaters) visit other houses.
* If the visitors are infected and the hosts are not infected, then the hosts are getting infected with a probability `S`.
* If the visitors are not infected and the hosts are infected, then the visitors are getting infected with the same probability `S`.
* If an individual gets infected in day `D`, then he/she is able to transmit the virus from days: `D+D1` to `D+D2`. After day `D+D2` he/she cannot infect or get infected (he/she is immune). 
* We suppose that at day 1, `I` people have just got infected. 

In this project you will have to create a program in python that will answer the following basic question:

> What is the maximum number of infectious inhabitants that the city will have **in a single day** over the course of the pandemic?

Let `M` be this value. 

You will also have to answer to following question:

> What is maximum number of `N` (people that break the lockdown measures!) that can be if we don't want `M` to go over a given value?
 
We suppose that the pandemic ends when no one is infectious any more. 
For example suppose that the number of infectious people for each day is (random numbers):

```text
Day    Infectious people
1      100
2      120
3      140 
4      160
5      180
6      200
7      220
8      250
9      350
10     400
11     340
12     300
13     260
14     250
15     200
16     150
17     100
18     60
19     40
20     0
```

In this particular example the value of `M` is 400 (on day 10)

In this project you will have to create a program in python that will take the following parameters:
* P : Number of town's inhabitants. If not given then assume P=10.000
* I : Number of initial positive cases. If not given then assume I=100
* N : Number of "cheaters" or else people that ignore lockdown measures and visit other houses. If not given then the program should terminate with an error message, except if the options `--plot_cheaters`  or `--compute_cheaters` have been given (see below). 
* S : Transmission probability. A number between 0 and 1. This is the probability that the virus is spread when an infected person gets in contact with an infected and non immunized person. Of not set then assume P=1 
* D1 : Days after on which an infected person becomes infectious. If not set then assume D1=3.
* D2 : Days after on which an infected person stops being infectious. If not set then assume D2=10.

Your program should also accept one of the following parameters: 

* `--compute_M`: Prints M for the given set of parameters 
* `--plot_population A B C` : shows or saves (whatever you want) a plot. On X axis are the values of the population (parameter `P`) from `A` to `B` with `C` intermediate steps (use ```np.linspace(A, B, C)```). On Y axis there are the corresponding `M` values. 

For example:
```bash
python program.y --plot_population 10000 20000 11 -I 200
```

Creates a plot as described where X contains 11 data points (10.000, 11.000, ..., 20.000) and Y are the `M` values for each X. For the calculations of `M` use the default values except for `I` which it should be 200. 

* `--plot_initial A B C` : shows or saves (whatever you want) a plot. On X axis are the initial cases (parameter `I`) from A to B with C steps (use ```np.linspace(A, B, C)```). On Y axis there are the corresponding `M` values. 

* `--plot_cheaters A B C` : shows or saves (whatever you want) a plot. On X axis are the cheaters (parameter `N`) from A to B with C steps (use ```np.linspace(A, B, C)```). On Y axis there are the corresponding `M` values. 

* `--compute_cheaters Μ`: prints the maximum number of cheaters (`N`) that can be if don't want `Μ` to go over the given value. For example:

```bash
python program.py --compute_cheaters 1500
# Prints the maximum number of cheaters that can be if we don't want the maximum number of cases to go over 1500, 
# with the default values of the rest parameters. 

python program.py --P 100000 --compute_cheaters 1500
# Prints the maximum number of cheaters that can be if we don't want the maximum number of cases to go over 1500, 
# with the default values of the rest parameters, except of P which is 100.000
```

Overall these tasks can help us understand how the various parameters of the spreading pattern of the virus affect the pressure in a healthcare system.


**Implementation Note 1**. Your program should perform a *simulation* of the pandemic. Namely, it should create initially `P` inhabitants and randomly infect `I` of them. After that it should go through an iteration over all days until the pandemic is over. Every iteration (or else, every day), random `N` people go to visit other people. So in your program, for each day, you should update the status of every inhabitant if needed (i.e from `healthy` to `infected`, or from `infected` to `immune`) and calculate the total number of infectious people of that day. The maximum number of infected people over all days is the value `M`. 

**Implementation Note 2**. Regarding the "Your program should also accept one of the following parameters: ". This does not mean that you have to choose which one to implement. **You should implement all options**. When I am running your programming I should be able to apply only one of the following parameters `--compute_M`, `--plot_population`, `--plot_initial`, `--plot_cheaters`, `--compute_cheaters`, and not two or more. For example this should be fine:

```bash
python program.py --compute_cheaters 1500
```

This should raise an error:
```bash
python program.py --compute_cheaters 1500 --plot_population 10000 20000 11
```

**Implementation Note 3**. Do not use the ```input``` function to read the parameters. Read the lecture notes on [how to read parameters from the command line](notes/python_gen_imp_cons_exc.md) (chapter: Running programs from the command line). 

**Implementation Note 4**. For simplicity consider that a cheater can visit a single host at a single day. A hosy can receive at most one cheater as a visitor on a single day. 





