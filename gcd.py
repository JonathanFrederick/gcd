#a file

def gcd_in():
    x = int(input("give me a positive number: "))
    y = int(input("give me another: "))
    return (x,y)

"""gcd(a, 0) = a
gcd(a,b) = gcd(b, a mod b)"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        print("b=",b,"\ta=",a,"\ta%b=",a%b)
        return gcd(b, a%b)

g, h = gcd_in()
print("The GCD of", g, "and", h, "is", gcd(g,h))
