import os
import sys
import math
from sage.all import *

'''
def stupid_func(num):
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			return False
	return True
'''

def main(argv):
	if len(argv) <2:
		sys.exit(0)
	else:
		path = argv[0]
		arr = []
		flag = ''
		for filename in os.listdir(path):
			'''
			You can use stupid func kid's stupid_func(num)
			or using SageMath like me (not for Python 3.x)
			'''
			if is_prime(int(filename))==True:
				arr.append(filename)
		arr.sort()
		for i in range(0, len(arr)):
			f = open(path+"/"+arr[i],"r")
			flag = flag+f.read().strip()
			f.close()
		f = open(argv[1],"w")
		f.write(flag)
		f.close()
		print '+\tSAVED to '+argv[1]
		print '========================================'
		print '============= CREDIT MrV ==============='
		print '=============Ph03nix Team==============='
		print '========================================'

main(sys.argv[1:])