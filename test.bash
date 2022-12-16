#!/bin/bash

diff <(python3 main.py -p -f test.txt) <(python3 main.py -p -f test2.txt)

diff <(cat test.txt | python3 main.py -p -i) <(python3 main.py -p -f test.txt)

diff <(cat test.txt | python3 main.py -p -i) <(cat test2.txt | python3 main.py -p -i)
