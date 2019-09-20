Assignment 2: Unit $ Functional Testing
=============================

# Description
`get_column_stats.py` allows you to calculate mean and standard deviation of a specific column within the file. This is a demonstration of best practices along with unit and functional testing.

### Usage
To get mean and standard deviation for a specific column using `get_column_stats.py`:
```
python get_column_stats.py -i <input_file> -c <column_number_to_get_stats>
```
 Where the input file is a tab-separated file containing numbers in each column, and the column number is a one-indexed number indicating the column to be used to calculate mean and standard deviation.

# Unit Testing
`basics_test.py` test for each individual function within the `get_column_stats.py` and making sure correct number is returned, or appropriate exceptions are raised.

### Usage
To run unit tests on get_column_stats one can run through the python command:
```
python basics_test.py
```

# Functional Testing
`basics_test.sh` is a functional testing script to ensure correct output is given under different circumstances when running `get_column_stats.py`. This includes:
+ Utilized ssshtest to test PEP8 style of all python code using pycodestyle
+ Included wrapper code to carry out unit test from previous step using `basics_test.py`
+ Ensure the correct mean and standard deviation is calculated using constant or random input
+ Added addtional test to make sure the get_column_stats is able to catch all kinds of errors

### Usage
To run tests on get_column_stats one can run the shell script:
```
bash basics_test.sh
```
