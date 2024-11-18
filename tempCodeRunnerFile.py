from numpy import sin,cos,radians,array,roots
import builtins

y0 = int(input())
u = int(input())
alpha = int(input())

g = 9.81
alpha = radians(alpha)

# gt^2 - 2usin(alpha)t -2y0 = 0

a= g
b = -2*u*sin(alpha)
c = -2*y0

# array of coefficients
coefficients = array([a,b,c])

t1 ,t2 = roots(coefficients)
# print(f"t1= {t1} and t2= {t2}")

t = builtins.max(t1,t2)
print(f"t= {round(t, 5)}")


# verticle height from the shooting point

h0 = (u**2 * (sin(alpha))**2) / (2*g)

hmax = h0 + y0
print(f"hmax= {round(hmax,5)}")

# Horizontal range of the bullet

R = u*cos(alpha)*t
print(f"Horizontal range= {round(R,5)}")


