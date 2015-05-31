New Zealand Fire Service (NZFS) Pager Parser

This is a python class used to parse and manipulate the output of a NZFS pager message.

At the time of writing this is used in conjunction with PDW, a FLEX pager decoder for Windows.  PDW allows certain
filters to output to a command file with command line arguments.  PDW cannot execute a python file, therefore py2exe
is used to convert the NZZFSPP.py file to an Windows binary .exe which can accept command line arguments from PDW.