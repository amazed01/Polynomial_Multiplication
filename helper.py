def ar1_greater_than_ar2(ar1, ar2): # ar1, ar2 in natural order
    n1, n2 = len(ar1), len(ar2)
    if n1 > n2:
        return True
    elif n1 < n2:
        return False
    i = 0
    while i < n1:
        if ar1[i] > ar2[i]:
            return True
        elif ar1[i] < ar2[i]:
            return False
        if i == n1-1:
            return True
        i += 1

def add_array(p:list,q:list): # ar1, ar2 in natural order
    l = p.copy()
    m = q.copy()
    if not ar1_greater_than_ar2(l,m):
        l,m = m,l

    l.reverse()
    m.reverse()
    
    z = [0] * (len(l) + 1)
    c = 0

    for i in range(len(m)):
        z[i] = (l[i] + m[i] + c) % 10
        c = (l[i] + m[i] + c) // 10
        # print(z)
        # print(c, 'loop 1')
    for i in range(len(m),len(l)):
        z[i] = (l[i] + c) % 10
        c = (l[i] + c) // 10
        # print(z)
        # print(c, 'loop 2')
    z[len(l)] = c 
    
    z.reverse()
    p = 0
    while p < len(z) - 1 and z[p] == 0:
        p +=1
    return z[p:]

def sub_array(p:list,q:list): # # ar1, ar2 in natural order
    l = p.copy()
    m = q.copy()
    
    flag = False
    if not ar1_greater_than_ar2(l,m):
        l,m = m,l
        flag = True
    
    l.reverse()
    m.reverse()
    
    z = [0] * (len(l) + 1)
    b = 0

    for i in range(len(m)):
        z[i] = (l[i] - m[i] + b) % 10
        b = ((l[i] - m[i] + b) - (l[i] - m[i] + b) % 10 ) // 10
    for i in range(len(m),len(l)):
        z[i] = (l[i] + b) % 10
        b = ((l[i] + b) - (l[i] + b) % 10 ) // 10
    z[len(l)] = b 
    
    if flag:
        z = [-1*x for x in z]
    
    z.reverse()
    p = 0
    while p < len(z) - 1 and z[p] == 0:
        p +=1
    return z[p:]

def make_equal_length(x,y):
    if len(x) - len(y) > 0:
        y = [0] * (len(x) - len(y)) + y
    elif len(x) - len(y) < 0:
        x = [0] * (len(y) - len(x)) + x
    # if len(x) % 2 == 1:
    #     x = [0] + x
    #     y = [0] + y
    return x,y


# a = [1,0,0,0]
# b = [2,8,3]
# print(helper.add_array(a,b))