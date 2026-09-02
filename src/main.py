import math  # noqa: I001
import plotly.graph_objects as go

def f(x, y):
    return 7 * x * y / math.exp(x**2 + y**2)

def generateGrid(f, m):
    n = 2*m/149
    X = []
    Y = []
    for i in range(150):
        X.append(-m + i*n)
        Y.append(-m + i*n)
    Z = []
    for y in Y:
        row = []
        for x in X:
            row.append(f(x, y))
        Z.append(row)
    return X, Y, Z

X, Y, Z = generateGrid(f, 2)
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
fig.show()

def pDifferentiate(f, x, y, h=1e-7):
    dfdx = (f(x+h, y) - f(x-h,y))/(2*h)
    dfdy = (f(x,y+h) - f(x,y-h))/(2*h)
    gradient = [dfdx, dfdy]
    return gradient

def descend(f, x, y, a=0.05, epsilon=0.001, maximum=10000):
    df = pDifferentiate(f, x, y)
    mdf = math.sqrt(df[0]**2 + df[1]**2)
    i = 0
    while mdf > epsilon and i < maximum:
        x = x - a*df[0]
        y = y - a*df[1]
        df = pDifferentiate(f, x, y)
        mdf = math.sqrt(df[0]**2 + df[1]**2)
        i = i + 1
    return x, y, i

x, y, i = descend(f, 1.06, 0.20)
print(f"Final position: ({x}, {y})")
print("Iterations:", i)