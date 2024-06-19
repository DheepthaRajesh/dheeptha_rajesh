Project Description 
===================

In today's diverse landscape of income sources and expenditure types, individuals face challenges in effectively managing their finances without the aid of a platform. The absence of a tool for handling income, expenses  and financial goal tracking can lead to difficulties in financial management. To address this issue, our focus will be on the development and optimization of a personal finance management system. This system aims to assist individuals in visualizing their cash flow and expense categories spent in different bank accounts, enabling better control and utilization of money.

This project is written primarily using C with HTML and javascript (Plotly library) used to render the webpage and expense graphs. 

The project utilizes all fundamental concepts of C language such as Finite State Machines with 1 FSM to handle input pages and 1 FSM to handle output pages. It also includes a manual parser to first validate (if in correct format) and then parse the input json files. HTML is used to render the home page, user bar graph page, account overall expenses page and account overall yearly expenses page. Plotly library from javascript is used to render the user bar graphs and account overall and yearly expense scatterplots. 

Project done in Term 6 SUTD - 2024


Getting Started
===================

Compiling the Project
-------------
To compile the project, you need to use the make utility which reads the `Makefile` provided in this repository. The default make command will build two executables: `FSM_output` and `FSM_input`.  

Simple run:
```
make
```
This will compile the source files and link the object files to create the two executables.

Running the Executables
------------
After successful compilation, you can run the executables directly from the command line:

For FSM_output:
```
./FSM_output
```
For FSM_input:
```
./FSM_input
```
Cleaning Build Files
--------
To clean up the build files (object files and executables), use the clean target:
```
make clean
```
This will remove all the compiled and linked files, leaving only the source code.
