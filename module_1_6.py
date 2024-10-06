from os import remove

my_dict = {'Dasha': 2001, 'Sveta': 2000, 'Vlada': 2002}
print(my_dict['Vlada'])
print(my_dict.get('Max'))
my_dict.update({'Mark': 1999, 'Sasha': 2004})
print(my_dict)
my_set = {1, 1, 'mom', False, 'mom', 1}
print(my_set)
my_set.add(6)
my_set.add('dad')
print(my_set)
my_set.remove(1)
print(my_set)
