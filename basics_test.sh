#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

echo Test using pycodestyle
run test_for_style_style pycodestyle style.py
assert_no_stdout

run test_for_get_column_stats pycodestyle get_column_stats.py
assert_no_stdout

run test_for_basics_test pycodestyle basics_test.py
assert_no_stdout

echo Unit test for mean and standard deviation functions
run unit_test python basics_test.py
assert_exit_code 0

echo Test for expected exit code and/or error message

(for i in `seq 1 100`; do
    echo -e "$RANDOM,$RANDOM,$RANDOM,$RANDOM,$RANDOM";
done )> data.txt
run invalid_delimiter python3 get_column_stats.py -i data.txt -c 1
assert_in_stdout "Input file contains bad formatting please check"
assert_exit_code 1


(for i in `seq 1 100`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run no_input_file python3 get_column_stats.py -i -c 4
assert_in_stderr "expected one argument"

run invalid_input_file python3 get_column_stats.py -i dat.txt -c 4
assert_in_stdout "The specified input file does not exist. Exiting"
assert_exit_code 1

run invalid_column_number python3 get_column_stats.py -i data.txt -c -1
assert_in_stderr "Column number must be greater than 0"
assert_exit_code 1

run run_to_sucess python3 get_column_stats.py -i data.txt -c 1
assert_exit_code 0


V=1
(for i in `seq 1 100`; do
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run no_input_file python3 get_column_stats.py -i -c 4
assert_in_stderr "expected one argument"

run invalid_input_file python3 get_column_stats.py -i dat.txt -c 4
assert_in_stdout "The specified input file does not exist. Exiting"
assert_exit_code 1

run invalid_column_number python3 get_column_stats.py -i data.txt -c -1
assert_in_stderr "Column number must be greater than 0"
assert_exit_code 1

run run_to_sucess python3 get_column_stats.py -i data.txt -c 1
assert_exit_code 0
