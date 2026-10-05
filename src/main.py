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

def pDifferentiate(f, x, y, h=1e-7):
    dfdx = (f(x+h, y) - f(x-h,y))/(2*h)
    dfdy = (f(x,y+h) - f(x,y-h))/(2*h)
    gradient = [dfdx, dfdy]
    return gradient

def descend(f, x, y, a=0.05, epsilon=0.001, maximum=10000):
    df = pDifferentiate(f, x, y)
    mdf = math.sqrt(df[0]**2 + df[1]**2)
    path = [[x, y, f(x, y)]]
    i = 0
    while mdf > epsilon and i < maximum:
        x = x - a*df[0]
        y = y - a*df[1]
        df = pDifferentiate(f, x, y)
        mdf = math.sqrt(df[0]**2 + df[1]**2)
        path.append([x, y, f(x, y)])
        i = i + 1
    return x, y, i, path

x_a, y_a, i_a, path_a = descend(f, 1.06, 0.20)
print(f"Final position: ({x_a}, {y_a})")
print("Iterations:", i_a)

path_x_a = [point[0] for point in path_a]
path_y_a = [point[1] for point in path_a]
path_z_a = [point[2] for point in path_a]

fig.add_trace(go.Scatter3d(
    x=path_x_a,
    y=path_y_a,
    z=path_z_a,
    mode="lines+markers",
    line={"color": "red", "width": 5},
    marker={"color": "red", "size": 3},
    name="Descent path A"
))

x_b, y_b, i_b, path_b = descend(f, -0.49, -0.36)
print(f"Final position: ({x_b}, {y_b})")
print("Iterations:", i_a)

path_x_b = [point[0] for point in path_b]
path_y_b = [point[1] for point in path_b]
path_z_b = [point[2] for point in path_b]

fig.add_trace(go.Scatter3d(
    x=path_x_b,
    y=path_y_b,
    z=path_z_b,
    mode="lines+markers",
    line={"color": "blue", "width": 5},
    marker={"color": "blue", "size": 3},
    name="Descent path B"
))

fig.show()