'''
The table used to represent the boolean expression of a logic gate function is commonly called a Truth Table.
 A logic gate truth table shows each possible input combination to the gate or circuit with the resultant output depending upon
 the combination of these input(s).
 There are several basic logic gates used in performing operations in digital systems. The common ones are;

OR Gate
AND Gate
NOT Gate
Additionally, these gates can also be found in a combination of one or two. Therefore we get other gates such as NAND Gate, NOR Gate, EXOR Gate, EXNOR Gate.

The Boolean expression of OR gate is Y = A + B, read as Y equals A ‘OR’ B.

The truth table of a two-input OR basic gate is given as;

A	B	Y
0	0	0
0	1	1
1	0	1
1	1	1
AND Gate
In AND gate the output of an AND gate attains the state 1 if and only if all the inputs are in state 1.

Logic Symbol of AND Gate



The Boolean expression of AND gate is Y = A.B

The truth table of a two-input AND basic gate is given as;

A	B	Y
0	0	0
0	1	0
1	0	0
1	1	1
NOT Gate
In NOT gate the output of a NOT gate attains the state 1 if and only if the input does not attain the state 1.

Logic Symbol of NOT gate





The Boolean expression is Y =


, read as Y equals NOT A.
The truth table of NOT gate is as follows;

A	Y
0	1
1	0


'''
a = 10
b = 2
print (a and b )
print ( a or b)
print ( not a )