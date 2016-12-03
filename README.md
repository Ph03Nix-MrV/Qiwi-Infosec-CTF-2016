# ``Those spies learned in university that prime numbers are essential for cryptography. Unfortunately, they got in wrong. A tar.gz file is given.```
```
encrypted.tar.gz
```
```
Extracting...
```
# Lets test some file
```
  17589952271 ==> Its not a Prime number ???
  17327339387 ==> Its not a Prime number ???
  20165380633 ==> Still not a Prime number ???
```
# What the hell is going on ???
# ~23k files and no one is Prime number ???

# Lets write a lazy script to test all
```
import os
path = 'encrypted'
arr = []
for filename in os.listdir(path):
  if is_prime(int(filename))==True:
	  arr.append(filename)
print str((len(arr)))+' Prime numbers'
```
```
90 Prime numbers
```
# Only 90 Prime numbers??? 
# SOMETHING WRONG :)
```
# sage PPC100_1.py encrypted flag.txt
# cat flag.txt
```
``` 
# c93c0f30299130cde942fce8ec5dd0b3012dcfa478a4ab2314ee525098fb779e2812d6731d372bae6d71e220a6 
```
# Lets try submit
# YAHOOOOOO !!! SOLVED !!!
