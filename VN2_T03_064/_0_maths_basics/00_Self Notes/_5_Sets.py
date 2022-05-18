'''
Union of Sets
Union of sets, which is denoted as A U B, lists the elements in set A and set B or the elements in both set A and set B.
For example, {1, 3} ∪ {1, 4} = {1, 3, 4}

Intersection of Sets
The intersection of sets which is denoted by A ∩ B lists the elements that are common to both set A and set B.
For example, {1, 2} ∩ {2, 4} = {2}

Set Difference
Set difference which is denoted by A - B, lists the elements in set A that are not present in set B.
For example, A = {2, 3, 4} and B = {4, 5, 6}. A - B = {2, 3}.

Set Complement
Set complement which is denoted by A', is the set of all elements in the universal set that are not present in set A.
In other words, A' is denoted as U - A, which is the difference in the elements of the universal set and set A.
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()-Return a set containing the union of sets
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set

intersection()	Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)

'''
s1 = {1, 2, 3, 7}
s2 = {3, 4, 5, 7}
print("union:",s1.union(s2))
print("symmetric_difference:", s1.symmetric_difference(s2))
print("intersection:",s1.intersection(s2))
print("intersection_update:",s1.intersection_update(s2))
print("difference:",s1.difference(s2))
print("difference_update:",s1.difference_update(s2))

