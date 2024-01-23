def decorator(a):
    def mn(v,v0,t):
        a(v,v0,t)
        s = (v**2 - v0**2) / (2*((v-v0)/t))
        print(s)
    return mn

@decorator
def a(v, v0, t):
    a = (v - v0)/t
    print(a)

try:
    v0 = int(input())
    v = int(input())
    t = int(input())
except ZeroDivisionError:
    print("..>0")
except ValueError:
    print("Value")


a(10,0,10)


