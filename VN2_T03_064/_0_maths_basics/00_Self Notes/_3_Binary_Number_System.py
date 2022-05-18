'''
S.No.	Number System and Description
1 Binary Number System
bin()
Base 2. Digits used : 0, 1

2 Octal Number System
oct()
Base 8. Digits used : 0 to 7

3 Hexa Decimal Number System
hex()
Base 16. Digits used: 0 to 9, Letters used : A- F
--------------------------
Binary Numbers Table
Some of the binary notations of lists of decimal numbers from 1 to 30,  are mentioned in the below list.

Number	Binary Number	Number	Binary Number	Number	Binary Number
1	1	11	1011	21	10101
2	10	12	1100	22	10110
3	11	13	1101	23	10111
4	100	14	1110	24	11000
5	101	15	1111	25	11001
6	110	16	10000	26	11010
7	111	17	10001	27	11011
8	1000	18	10010	28	11100
9	1001	19	10011	29	11101
10	1010	20	10100	30	11110

How to Calculate Binary Numbers
For example, the number to be operated is 1235.

Thousands	Hundreds	Tens	Ones
1	2	3	5
This indicates,

1235 = 1 × 1000 + 2 × 100 + 3 × 10 + 5 × 1

Given,

1000	= 103 = 10 × 10 × 10
100	= 102 = 10 × 10
10	= 101 = 10
1	= 100 (any value to the exponent zero is one)
We can represent int values in the following ways

1)	Decimal form
2)	Binary form
3)	Octal form
4)	Hexa decimal form

I)	Decimal Form (Base-10):

•	It is the default number system in Python
•	The allowed digits are: 0 to 9
•	Eg: a =10

II)	Binary Form (Base-2):

•	The allowed digits are : 0 & 1
•	Literal value should be prefixed with 0b or 0B

•	Eg: a = 0B1111
a = 0B123
a = b111





III)	Octal Form (Base-8):

•	The allowed digits are : 0 to 7
•	Literal value should be prefixed with 0o or 0O.

•	Eg: a = 0o123
a = 0o786

IV)	Hexa Decimal Form (Base-16):

•	The allowed digits are: 0 to 9, a-f (both lower and upper cases are allowed)
•	Literal value should be prefixed with 0x or 0X

•	Eg: a = 0XFACE
a = 0XBeef a = 0XBeer

Note: Being a programmer we can specify literal values in decimal, binary, octal and hexa decimal forms. But PVM will always provide values only in decimal form.

	a=10
	b=0o10
	c=0X10
	d=0B10
	print(a)10
	print(b)8
	print(c)16
	print(d)2

Base Conversions

Python provide the following in-built functions for base conversions

1)	bin():
We can use bin() to convert from any base to binary 1) >>> bin(15)
3)   >>> bin(0o11)

5)   >>> bin(0X10)






2)	oct():
We can use oct() to convert from any base to octal

1)	>>> oct(10)
2)	'0o12'
3)	>>> oct(0B1111)
4)	'0o17'
5)	>>> oct(0X123)
6) '0o443'

3)	hex():
We can use hex() to convert from any base to hexa decimal

1)	>>> hex(100)
2)	'0x64'
3)	>>> hex(0B111111)
4)	'0x3f'
5)	>>> hex(0o12345)
6) '0x14e5'

'''
print("octal:",oct(0B111))
print("binary:",bin(12))
print("hexadecimal:",hex(123))