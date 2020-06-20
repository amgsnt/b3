#!/bin/bash

python cotacaob3.py
rm -Rf out
mkdir out
mv COTAHIST* out/
cat out/COTAHIST* >> out/COTAHIST.cat
sed '/^01/!d' out/COTAHIST.cat > out/b3_cotahist.out
rm -Rf out/COTAHIST*
