import re
pwd=[]

h = open('D:\\python\\AOC2020\\Day2\\sample.txt','r')

content = h.readlines()

for line in content:
        pwd.append(line.rstrip('\n'))
valid = 0
invalid = 0
for x in pwd:
    y=re.findall('\d+', x )
    pos1 = int(y[0])
    pos2 = int(y[1])
    text = x.split(':')
    #String to be checked against#
    paswd=text[1]
    #value to be checked#
    v=text[0][-1]
    #To keep the counter of characters in string#
    if(paswd[pos1]==v):
        if(paswd[pos2]==v):
            invalid=invalid+1
        else:
            pass
    if(paswd[pos1]==v):
        if(paswd[pos2]==v ):
            invalid=invalid+1
        else:
            valid=valid+1
    if(paswd[pos2]==v ):
        if(paswd[pos1]==v):
            invalid=invalid+1
        else:
            valid=valid+1
    if(paswd[pos1]!=v ):
        if(paswd[pos2]!=v):
            invalid=invalid+1

print(valid)
print(invalid)