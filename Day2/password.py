import re
pwd=[]

h = open('D:\\python\\AOC2020\\Day2\\sample.txt','r')

content = h.readlines()

for line in content:
        pwd.append(line.rstrip('\n'))
counter = 0
for x in pwd:
    y=re.findall('\d+', x )
    min = y[0]
    max = y[1]
    text = x.split(':')
    #String to be checked against#
    paswd=text[1]
    #value to be checked#
    v=text[0][-1]
    #To keep the counter of characters in string#
    frequencies = {} 
  
    for char in paswd: 
        if char in frequencies: 
            frequencies[char] += 1
        else: 
            frequencies[char] = 1
    
    for key,value in frequencies.items():
        if(key==v):
            if(frequencies.get(key)>=int(min)):
                if(frequencies.get(key)<=int(max)):
                    counter=counter+1


print(counter)
    