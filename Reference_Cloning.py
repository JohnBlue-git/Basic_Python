# Auther: John Blue
# Time: 2023/2
# Object: showing how different is between reference and cloning



# reference (Python usually default object assignment as reference)
a = [1, 2, 3]
b = a         # 不同變數分享相同串列結構：此串列擁有 a 與 b 兩個「別名」(Alias)
print('b reference a ...')
print('a == b: ', a == b)
print('a is b: ', a is b)
print('')



# cloning
a = [1, 2, 3]
b = a[:] # cloning by slicing
print('b cloning a ...')
print('a == b', a == b)
print('a is b', a is b)
print('')



# reference in function
def rf(x):
    x[0] -= x[1]
    return x

x = [1,1]
print('x =', x)
rf(x)
print('x(after rf(x)) =', x)
print('')



#  cloning in function (pure function)
def pf(x):
    t = []
    for i in x:
        tm = []
        for value in i:
            tm.append(value)
            value = 0 # no effect
        t.append(tm)
    t[0][0] -= t[0][1] # mutate t
    return t, x[:]
x = [[1,1],[3,4]]
print('x =', x)
t = pf(x)
#t = pf(x[:]) # or you can send cone to a function to avoid the reference problem
print('x(after pf(x)) =', x)
print('t =', t)
print('')
