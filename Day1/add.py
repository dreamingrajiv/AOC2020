
num=[]

h = open('D:\\python\\AOC2020\\Day1\\num.txt','r')

content = h.readlines()

for line in content:
        num.append(int(line))


for x in num:
    for y in num:
        if(int(x+y)==2020):
            print(x,y)
            print(x*y)