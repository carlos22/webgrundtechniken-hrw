#!/usr/bin/env python

import os
import codecs
import string

def find_files(pattern):
	l = []
	for r,d,f in os.walk('.'):
		if r.find(pattern) > 0:
			for fn in f:
				l += [r + '/' + fn]
	return l

def obfuscate(f):
	rot13 = string.maketrans(
		"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
	)
	os.rename(f, f + '.in')
	i = open(f + '.in', mode='rb')
	o = open(f,         mode='wb')
	o.write(string.translate(i.read(), rot13))
	#o.write(i.read())
	i.close()
	o.close()
	os.unlink(f + '.in')

def main():
	for f in find_files('sample solution'):
		obfuscate(f)

if __name__ == '__main__':
	main()
