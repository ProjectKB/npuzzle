#!/bin/bash

diff <(python3 main.py -p -f test1.txt) <(python3 main.py -p -f test2.txt)

diff <(cat test1.txt | python3 main.py -p -i) <(python3 main.py -p -f test1.txt)

diff <(cat test1.txt | python3 main.py -p -i) <(cat test2.txt | python3 main.py -p -i)
