# B_R_R
# M_S_A_W



"""
Coding Problem on Regular expressions:
In order to work with regular expressions or we can say regex too,
we have to import its module which is called re
Specifically we use findall method of regex library
findall returns a list containing all matches

"""


import re

email='abdumaliksharipov@gmail.com'
expression='[a-z]+'

matches=re.findall(expression,email)
print(matches)

name=matches[0]
domain=f'{matches[1]}.{matches[2]}'

print(name)
print(domain)


print()
print()
print()
print()

# Let's change it a bit
# So we amend expression whereby it takes in dot as well
# Now there are 2 matches to meet the the expression

email2='somebody@company.net'
expression2='[a-z\.]+'
matches2=re.findall(expression2, email2)

nam=matches2[0]
dom=matches2[1]

print(matches2)
print(nam)
print(dom)


print()
print()
print()
print()

# We can make it simpler by using split method too

email3='name@company.us'
parts=email3.split('@')

nam2=parts[0]
dom2=parts[1]

print(parts)
print(nam2)
print(dom2)
