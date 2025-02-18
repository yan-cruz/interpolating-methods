import sympy as sp

def newton_interpolation():
    degree = int(input("Entre com o grau do polinômio: "))
    n = degree + 1
    
    x_values = []
    y_values = []
    
    for i in range(n):
        x_val = float(input(f"Entre com X({i}): "))
        x_values.append(x_val)
    
    for i in range(n):
        y_val = float(input(f"Entre com FX({i}): "))
        y_values.append(y_val)
    
    x = sp.Symbol('x')
    
    divided_diff = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        divided_diff[i][0] = y_values[i]
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x_values[i + j] - x_values[i])
    
    P_x = divided_diff[0][0]
    for i in range(1, n):
        term = divided_diff[0][i]
        for j in range(i):
            term *= (x - x_values[j])
        P_x += term
    
    P_x = sp.simplify(P_x)
    
    display_function(P_x)
    
    return P_x

def display_function(P_x):
    print("Pelo método de Newton, o polinômio é:")
    print(sp.pretty(P_x, use_unicode=True))

if __name__ == "__main__":
    newton_interpolation()