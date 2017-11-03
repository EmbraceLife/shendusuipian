
# from sympy import symbols
# from sympy.plotting import plot
from sympy import plot, diff, exp
from sympy.abc import x,y,z,m,n,p,q,A,Y
import sympy as sp
import numpy as np
##################################################
# 如何一步一步计算linear导数
w1,w2,w3,x1,x2,x3 = symbols("w1 w2 w3 x1 x2 x3")
linear = w1*x1 + w2*x2 + w3*x3
grad_w1 = linear.diff(w1)
grad_w2 = linear.diff(w2)
grad_w3 = linear.diff(w3)
grad_W = [x1, x2, x3]


##################################################
# 如何一步一步计算relu导数
l1 = 0
l2 = x
lines = plot((l1,(x, -2, 0)), (l2, (x, 0, 2)), show=False)
lines[0].line_color = 'green'
lines[1].line_color = 'red'
lines.show()
grad_relu_x = 0 if x < 0 else 1


##################################################
# 如何一步一步计算sigmoid导数
plot(1/(1+exp(-z)))

sigmoid = 1/(1+exp(-z))
s = 1/(1+p)
grad1 = s.diff(p)
p = exp(-z)
grad2 = p.diff(z)
grad1*grad2
sigmoid.diff(z)

##################################################
# 如何一步一步计算logloss导数
loss1 = -Y*log(A)
loss2 = -(1-Y)*log(1-A)
loss1.diff(A)
loss2.diff(A)

dw = (1/m)*np.dot(X, (A-Y).T)
db = (1/m)*np.sum(A-Y)



import numpy as np
np.exp(-3)
1/np.exp(3)

y, yp = symbols('y yp')
loss = -(y*log(yp)+(1-y)*log(1-yp))
pprint(loss)
lines = plot(-log(yp), -log(1-yp), show=False)
lines[0].line_color = 'red'
lines[1].line_color = 'cyan'
lines.show()


x = symbols('x')
f1 = x
f2 = 0

# plot() allows only one line_color argument
p = plot((f1, (x, 0, 10)), (f2, (x, -10, 0)), title="x for (0, oo), -x**2 for (-oo, 0]", show=False)
p[0].line_color = 'blue'
p[1].line_color = 'green'
p.show()


# one x range for 3 functions
plot(x, x**2, x**3, (x, -5, 5), line_color=['red','blue', 'green'] )

## x range for two functions
plot((x**2, (x, -6, 6)), (x, (x, -5, 5)))

# plot(x**2, adaptive=False, nb_of_points=400)

## plot derivatives
x = symbols('x')
y = (sqrt(x)/(1 + x))**2
dy = diff(y, x)
yl = 10
lines = plot(y, dy, (x, -5, 5), ylim=(-yl, 1), title=str(y)+str(dy), show=False)
lines[0].line_color='firebrick'
lines[1].line_color='cyan'
lines.show()

from IPython.display import Math
Math(r'$$\frac{1}{\sqrt{2\pi\sigma^2} } e^{ -\frac{(x-\mu)^2}{2\sigma^2} }.$$')

Math(r'$$\left[\begin{matrix}1 & 0 & 1\\-1 & 2 & 3\\1 & 2 & 3\end{matrix}\right]$$')
Matrix([[1,0,1], [-1,2,3], [1,2,3]])

Math(r'i\hbar \frac{dA}{dt}~=~[A(t),H(t)]+i\hbar \frac{\partial A}{\partial t}.')
Math(r'$$\left[\begin{matrix}x\\y\\z\end{matrix}\right]$$ $$\left[\begin{matrix}x + z\\- x + 2 y + 3 z\\x + 2 y + 3 z\end{matrix}\right]$$')

from IPython.display import Latex
Latex("""SymPy can also operate on matrices of symbolic dimension ($n \\times m$). `MatrixSymbol("M", n, m)` creates a matrix $M$ of shape $n \\times m$.""")

Math(r'$$\begin{align}z &= x^2 - y^2\\z^2 &= x^2 + y^2 + 4\\z &= x + y\end{align}$$')

Math(r"$$f''(x) = -f(x)$$")
