Assignment 1: best-practices
=============================

Below is the summary of the changes made:

# style.py
+ Fixed all the style error pointed out by Pycodestyle

# get_column_stats.py
+ Fixed all the style error pointed out by Pycodestyle
+ Wrap most of the operations into functions
+ Added exception handling for numerous instances
+ Added comments for most of the steps
+ Fixed the inconsistency of the indexing. Now 1st column means 1st column, instead of 0th column

## Usage
```
python get_column_stats.py -i <input_file> -c <column_number_to_get_stats>
```


# basics_test.sh
+ Utilized ssshtest to test using pycodestyle
+ Added addtional test to make sure the get_column_stats is able to catch all kinds of errors

## Usage
```
bash basics_test.sh
```