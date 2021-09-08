# Python-String-Data 🐍
## Manipulate and format string data for display in Python - In An Hour
More information can be found here: https://docs.microsoft.com/en-us/learn/modules/python-format-strings/ <br>
There are many situations where you may receive string data that you need to manipulate. Python provides in-built features for string manipulation. 
This repo consist of small python string data manipulation exercises. 

## Task 1
#### Using single or double quotes<br>
Python
```python
first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string)
```

Output
```output
True
```

#### Add quotes inside quotes<br>
Python
```python
third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)
```

Output
```output
A single quoted literal string with a " double quote
A double quoted literal string with a ' single quote
```

#### Lines breaks and tabs<br>
Python
```python
fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)
```

Output
```output
A single quoted literal string with an ' escaped single quote
A double quoted literal string with a " double quote
A literal string with a
 new line character
A literal string with a          tab character
```

#### Contents of the escape sequence without performing the escape sequence<br>
Python
```python
ninth_string = r"A literal string with a \n new line character printed raw"

print(ninth_string)
```

Output
```output
A literal string with a \n new line character printed raw
```

#### Strings across multiple lines<br>
Python
```python
tenth_string = '''A literal string
on more than one line
sometimes known as a verbatim string'''

eleventh_string = """Another literal string
     on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)
```

Output
```output
A literal string
on more than one line
sometimes known as a verbatim string
Another literal string
     on more than one line
using double quotes
```

#### Built-in features in the print() function<br>
Python
```python
first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first, second)
print(first, second, third)
print(first, second, third, sep='-')
print(first, second, third, sep='-', end='.')
```

Output
```output
Conrad Grant
Conrad Grant Bob
Conrad-Grant-Bob
Conrad-Grant-Bob.
```

## Task 2

#### Locate a letter based on its position in a string<br>
Python
```python
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))
```

Output
```output
4
31
0
```

#### Remove empty spaces from the left and righ of the string<br>
Python
```python
message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')
```

Output
```output
.middle     .
.    middle.
.middle.
```

#### Replace parts of a string with another word<br>
Python
```python
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)
```

Output
```output
brevity is the soul of wit
```

#### Add empty spaces to the left and the right of the string<br>
Python
```python
message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '-'))
print(message.ljust(20))
print(message.ljust(20, '-'))
```

Output
```output
howdy
---------------howdy
howdy
howdy---------------
```

## Task 3

#### A format string with replacement fields<br>
Python
```python
medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)
```

Output
```output
Coughussin - Take 5 ML by mouth every 4.5 hours
4.5 - Take 5 ML by mouth every Coughussin hours
Sneezergen - Take 10 ML by mouth every 6 hours
```

#### A format string with replacement fields using f-strings<br>
Python
```python
name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message)
```

Output
```output
Hello, World.
Count to 10.  Multiply by 3.14.
```

#### A format string with calculations<br>
Python
```python
width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')
```

Output
```output
The perimeter is 30 and the area is 50.
```

#### A format string with special format specifiers<br>
Python
```python
value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
```

Output
```output
.hi                       .
.                       hi.
.           hi            .
.-----------hi------------.
```
