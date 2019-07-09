# B_R_R
# M_S_A_W



"""
Coding Problem on Regular expressions:

In order to work with regular expressions or we can say regex too,
we have to import its module which is called re

Specifically we use search method of regex library

search method returns match object if it finds any

"""


import re



price='Price: $12,065.99'
expression='Price: \$([0-9\,]*\.[0-9]*)'
matches=re.search(expression, price)

print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

# price_number=float(matches.group(1)) # As soon as our price contains comma, this method does not work
# print(price_number)

# If price is comma separated, it is better to replace it with empty string first
price_number_comma=matches.group(1).replace(",","")
price_number=float(price_number_comma)
print(price_number_comma)




