my_list = []
print(my_list)
my_list = [1, 2, 3, 'happy', 3.132]
print(my_list)
my_list = [1, 2, 3]
print(my_list)
my_list.append([555, 12])
print(my_list)
my_list.extend([234, 'pavitra'])
print(my_list)
my_list.insert(1, 'kiran')
print(my_list)
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list:
    print(element)
print(my_list)
print(my_list[3])
print(my_list[0:2])
print(my_list[::-1])
my_dict = {} #empty dict
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'}
print(my_dict)
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++'
print(my_dict)
my_dict['Third'] = 'Ruby'
print(my_dict)
my_tuple2 = (1, 2, 3, 'vn2','lti')
for x in my_tuple2:
    print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[1][2])
my_tuple = (1, 2, 3, ['hindi', 'python'])
my_tuple[3][0] = 'english'
print(my_tuple)
print(my_tuple.count(2))
print(my_tuple.index(['english', 'python']))
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)