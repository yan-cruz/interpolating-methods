import sympy as sp

def lagrange_interpolation():
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
    
    P_x = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_values[j]) / (x_values[i] - x_values[j])
        P_x += y_values[i] * L_i
    
    P_x = sp.simplify(P_x)
    
    display_function(P_x)
    
    return P_x

def display_function(P_x):
    print("Pelo método de Lagrange, o polinômio é:")
    print(sp.pretty(P_x, use_unicode=True))

if __name__ == "__main__":
    lagrange_interpolation()