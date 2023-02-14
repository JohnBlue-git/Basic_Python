# Auther: John Blue
# Time: 2023/2
# Object: file IO in Python

##import numpy as np
##
##np.save('123', np.array([['a', 2, 3], [4, 5, 6]]))
##a=np.load('123.npy')

# open file
fo = open("out.txt", 'w')
print ("file name: ", fo.name)
str = ['a','\t','112','\t','112','\t']
fo.write(str[0])
fo.write(str[1])
fo.write(str[2])
fo.write(str[3])
fo.write(str[4])
fo.write(str[5])
fo.write('\n')
fo.writelines( str )
fo.write('\n')
fo.writelines( str )
fo.write('\n')
# close file
fo.close()

# open file
fo = open("out.txt", "r")
result=list()
for line in open('test.txt'):
    line = fo.readline().split('\t')
    print(line)
    m=len(line)/2+1
    del line[int(m)]
    print(line)
    result.append(line)
print(result)
# close file
fo.close()

# split simple list
##df_list = ['foo bar']
##df = []
##for item in df_list :
##        df.extend(item.split())

# string to number
#x = '123f'
#print('hello', float(x[0:3]))
