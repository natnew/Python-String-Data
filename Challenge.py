first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
print(first_value.rjust(20))

# Second challenge
second_value = second_value.capitalize()
second_value = second_value.replace('-', ' ')
print(second_value.ljust(20))

# Third challenge

third_value = third_value.lower()
third_value = third_value.capitalize()
third_value = third_value.replace('-', ' ')
third_value = third_value.replace(' ', '')
print(third_value.rjust(20))


#print(first_value)
#print(second_value)
#print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#',end='!')


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\n {fourth_value:^25} \n', f' {fifth_value:^25} \n',  f' {sixth_value:^25} ' )