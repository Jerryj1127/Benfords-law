# All the blah..blah..blahs...
from requests import get
from re import search, findall
import matplotlib.pyplot as plt
num_lst = []
first_dig_lst = []
sum_all = 0
count = {}
def format_tick(d):
    nums = []
    for x in d:
        nums.append("{}({})".format(x, d[x]))
    return nums

def colorize(d):
    clr_lst = ["green"]*10
    nd = sorted(d, key = lambda x: d[x], reverse = True)
    clr_lst[nd[0]] = "red"
    clr_lst[nd[1]] = "orange"
    return(clr_lst)


#retreving data from the site...Make sure theres an active internet connection
url = input('Enter the url: ')
data = get(url)

#processing the data ; extracting nos from the data
for line in data.text.split():
    num_lst += (findall('[0-9]{1,100}',line))

# Getting the first digits of the numbers
for num in num_lst:
    first_dig_lst.append(int(num[0]))


#ahh...atlast...the output part
for i in range(10):
    count_occur = first_dig_lst.count(i)
    count[i] = count_occur
    #print("{} : {}".format(i, count_occur))
    sum_all += count_occur

#print('After the division:', count[1]/sum_all)

left = list(range(10))
height = list(count.values())
tick_label = format_tick(count)
plt.bar(left, height, tick_label = tick_label, width = 0.8, color = colorize(count))
plt.xlabel('Digit-->')
plt.ylabel('Frequency-->') 
plt.title('URL: ' + url) 
  
# function to show the plot 
plt.show() 