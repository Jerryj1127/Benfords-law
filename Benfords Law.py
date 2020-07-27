# All the blah..blah..blahs...
from requests import get
from re import search, findall
num_lst = []
first_no_lst = []

#retreving data from the site...Make sure theres an active internet connection
url = input('Enter the url: ')
data = get(url)

#processing the data ; extracting nos from the data
for line in data.text.split():
    num_lst += (findall('[0-9]{1,100}',line))

# Getting the first digits of the numbers
for num in num_lst:
    first_no_lst.append(int(num[0]))

#ahh...atlast...the output part
for i in range(10):
    print("{} : {}".format(i, first_no_lst.count(i)))