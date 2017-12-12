@echo off

python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9 clientVersion
python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9 serverVersion
python compile.py tag %1 %2 %3 %4 %5 %6 %7 %8 %9
rm cur_compilation.py
rm *.pyc

pause

