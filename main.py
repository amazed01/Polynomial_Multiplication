from helper import *
import math

def multiply(x,y):
    x,y = make_equal_length(x,y)
    
    if len(x) == 0:
        return [0]
    if len(x) == 1:
        unit = (x[0] * y[0]) % 10
        carry = (x[0] * y[0]) // 10
        if carry != 0:
            return [carry,unit]
        else: return [unit]

    print('###########################################')
    print('New Multiply Recursion Level')

    k = len(x) // 2

    input('Break into Two Parts')
    x_left, x_right = x[:k], x[k:]
    y_left, y_right = y[:k], y[k:]
    input('a   b   c   d')
    print(x_left,x_right,y_left,y_right)

    input('Starting P1 (a x c) calculation')
    P1 = multiply(x_left,y_left)
    input('Enter to see P1 (a x c)')
    print(P1)

    input('Starting P2 (b x d) calculation')
    P2 = multiply(x_right,y_right)
    input('Enter to see P2 (b x d)')
    print(P2)

    input('Starting P3 (a+b x c+d) calculation')
    P3 = multiply(add_array(x_left,x_right),add_array(y_left,y_right))
    input('Enter to see P3 (a+b x c+d)')
    print(P3)

    input('Starting final calculation')
    k_dash = k
    if len(x) % 2 == 1:
        k_dash = k + 1
        k = k + 1
        print('CHANGED K DUE TO ODD LENGTH')
    l = add_array(P1,P2)
    print(l, ' P1 + P2', P1 + [0]*2*k_dash, P2)  # K_dash added later
    l = sub_array(P3,l)
    print(l, ' P3 - P1 - P2 ___ Os', [0]*k)
    # print('@@@@@@@@@@@@@@@')
    # print(P1 + [0]*2*k, P2)
    q = add_array(P1 + [0]*2*k_dash,P2)
    print(q,' (P1 + [0]*2*k_dash) + P2', P1 + [0]*2*k_dash,P2 )

    t = add_array(add_array(P1 + [0]*2*k_dash,P2) , sub_array(P3,add_array(P1,P2)) + [0]*k)
    input('Enter to see final calculation at this recursion level')
    print(t)

    return t

a = [7,0,4,2]#[1,2,3,4]
b = [6,7,3]#[1,5,6,2]
print(multiply(a,b))
#print(add_array([1]+ [0]*2,[1,0]))