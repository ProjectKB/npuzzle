#!/bin/bash

diff <(python3 main.py -f test.txt) <(python3 main.py -f test2.txt)

diff <(cat test.txt | python3 main.py -i) <(python3 main.py -f test.txt)

diff <(cat test.txt | python3 main.py -i) <(cat test2.txt | python3 main.py -i)
