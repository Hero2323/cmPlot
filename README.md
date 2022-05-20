# cmPlot
Function Plotter GUI made using python. 

Supported operands: ```+```, ```-```, ```*```, ```/``` and ```^```. 

Supported variables: ```x```. 

Supported characters: the operands above, only the variable ```x```, numbers from ```0``` to ```9``` and the ```.``` character for decimals.

# Dependencies
pysimpleGUI, numpy, matplotlib, sympy.

All dependencies can be installed by running the command ```pip install -r requirements.txt``` from the root project directory.

# Running the plotter
The plotter can be run by using the command ```python3 -m src.cmPlot``` from the project's root directory.

The project can be tested by running the command ```python3 -m test.test_input_verification``` from the project's root directory.

# Snapshots
**What the plotter looks like** <br />
![What the plotter looks like](assets/screenshots/1.png "Initial Looks")
<br />
<br />


**Correct Example 1** <br />
<br />
![Correct example 1](assets/screenshots/2.png "correct1")<br />

**Correct Example 2** <br />
<br />
![Correct example 2](assets/screenshots/3.png "correct2")<br />

**Correct Example 3** <br />
<br />
![Correct example 3](assets/screenshots/4.png "correct3")<br />

<br />
<br />

**Incorrect Example 1** <br />
<br />
![Incorrect example 1](assets/screenshots/5.png "incorrect1")<br />

**Incorrect Example 2** <br />
<br />
![Incorrect example 2](assets/screenshots/6.png "incorrect2")<br />

**Incorrect Example 3** <br />
<br />
![Incorrect example 3](assets/screenshots/7.png "incorrect3")<br />

**Incorrect Example 4** <br />
<br />
![Incorrect example 4](assets/screenshots/8.png "incorrect4")<br />

**Incorrect Example 5** <br />
<br />
![Incorrect example 5](assets/screenshots/9.png "incorrect5")<br />

**Incorrect Example 6** <br />
<br />
![Incorrect example 6](assets/screenshots/10.png "incorrect6")<br />

**Incorrect Example 7** <br />
<br />
![Incorrect example 7](assets/screenshots/11.png "incorrect7")<br />

**Incorrect Example 8** <br />
<br />
![Incorrect example 8](assets/screenshots/12.png "incorrect8")<br />

# Notes about division by zero and discontinuities

This plotter supports division by zero in limited cases like division by zero (such as 1 / x) function. it doesn't support only infinite functions or functions with many discontinuities however (such as 1 / 0).

**Supported Example 1** <br />
<br />
![Supported example 1](assets/screenshots/13.png "supported1")<br />

**Unsupported Example 1** <br />
<br />
![Unsupported example 1](assets/screenshots/14.png "unsupported1")<br />







