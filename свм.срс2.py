import numpy as np
from scipy.optimize import bisect, newton, root_scalar

#задание 1
print('задание 1')
def f(x):
    return x**2 + x - 1

a, b, n = 0.5, 1.0, 10
x_values = np.linspace(a, b, n + 1)

print(f"{'№':>3} {'x':>12} {'f(x)':>15}")

for i, x in enumerate(x_values):
    y = f(x)

    print(
        f"{i:>3} "
        f"{x:>12.6f} "
        f"{y:>15.8f}"
    )

#задание 2
print()
print('задание 2')
fa = f(a)
fb = f(b)

print(f"a = {a}, b = {b}")
print(f"f(a) = {fa}, f(b) = {fb}")

if fa * fb < 0:
    print("Условие f(a)*f(b)<0 выполнено")
    print("На этом участке есть корень")
else:
    print("На этом участке нет корня")

#задание 3
print()
print('задание 3')
def bisection(a, b, epsilon):
    iterations = []

    for k in range(1, 1000):
        x = (a + b) / 2
        error = abs(b - a) / 2
        fx = f(x)
        iterations.append((k, a, b, x, error, fx))

        if error < epsilon:
            break
        if f(a) * fx < 0:
            b = x
        else:
            a = x
    return iterations

def print_bisection_result(iterations, epsilon):
    print(f"e = {epsilon}")
    print(f"{'№':>4} "
          f"{'a':>12} "
          f"{'b':>12} "
          f"{'x':>15} "
          f"{'Ошибка':>15} "
          f"{'f(x)':>15}")

    for row in iterations:
        k = row[0]
        a_current = row[1]
        b_current = row[2]
        x = row[3]
        error = row[4]
        fx = row[5]

        print(f"{k:>4} "
              f"{a_current:>12.8f} "
              f"{b_current:>12.8f} "
              f"{x:>15.10f} "
              f"{error:>15.8e} "
              f"{fx:>15.8e} ")

    root = iterations[-1][3]

    print(f"Корень: {root:.10f}")
    print(f"f(x) = {f(root):.10f}")
    print(f"Невязка |f(x)| = {abs(f(root)):.5e}")

epsilon_1 = 10**(-3)
epsilon_2 = 10**(-5)

result = bisection(a, b, epsilon_1)
print_bisection_result(result, epsilon_1)

result = bisection(a, b, epsilon_2)
print_bisection_result(result, epsilon_2)

#задание 4
print()
print('задание 4')

def chord(a, b, epsilon):
    iterations = []
    k = 0
    x_old = a

    while True:
        k += 1
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fx = f(x)
        error = abs(x - x_old)
        iterations.append((k, x, error, fx))

        if error < epsilon:
            break
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x_old = x

    return x, iterations

x1, iterations1 = chord(a, b, 10**(-3))

print("е = 10^-3")

for k, x, error, fx in iterations1:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  f(x) = {fx:.7f}")

print(f"Корень: {x1:.7f}")
print(f"f(x) = {f(x1):.7f}")
print(f"Невязка |f(x)| = {abs(f(x1)):.5e}")

x2, iterations2 = chord(a, b, 10**(-5))

print("е = 10^-5")

for k, x, error, fx in iterations2:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  f(x) = {fx:.7f}")

print(f"Корень: {x2:.7f}")
print(f"f(x) = {f(x2):.7f}")
print(f"Невязка |f(x)| = {abs(f(x2)):.5e}")

#задание 5
print()
print('задание 5')

def df(x):
    return 2 * x + 1

def newton_method(x0, epsilon):
    iterations = []
    k = 0
    x_old = x0

    while True:
        k += 1
        x = x_old - f(x_old) / df(x_old)
        fx = f(x)
        error = abs(x - x_old)
        iterations.append((k, x, error, fx))

        if error < epsilon:
            break
        x_old = x

    return x, iterations

x1, iterations1 = newton_method(0.5, 10**(-3))

print("x0 = 0.5, е = 10^-3")

for k, x, error, fx in iterations1:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  f(x) = {fx:.7f}")

print(f"Корень: {x1:.7f}")
print(f"f(x) = {f(x1):.7f}")
print(f"Невязка |f(x)| = {abs(f(x1)):.5e}")

x2, iterations2 = newton_method(0.5, 10**(-5))

print("x0 = 0.5, е = 10^-5")

for k, x, error, fx in iterations2:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  f(x) = {fx:.7f}")

print(f"Корень: {x2:.7f}")
print(f"f(x) = {f(x2):.7f}")
print(f"Невязка |f(x)| = {abs(f(x2)):.5e}")

x3, iterations3 = newton_method(1.0, 10**(-3))

print("x0 = 1.0, е = 10^-3")

for k, x, error, fx in iterations3:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  f(x) = {fx:.7f}")

print(f"Корень: {x3:.7f}")
print(f"f(x) = {f(x3):.7f}")
print(f"Невязка |f(x)| = {abs(f(x3)):.5e}")

x4, iterations4 = newton_method(1.0, 10**(-5))

print("x0 = 1.0, е = 10^-5")

for k, x, error, fx in iterations4:
    print(f"{k:3d}  x = {x:.7f}  "
          f"ошибка = {error:.7f}  "
          f"f(x) = {fx:.7f}")

print(f"Корень: {x4:.7f}")
print(f"f(x) = {f(x4):.7f}")
print(f"Невязка |f(x)| = {abs(f(x4)):.5e}")

#задание 6
print()
print('задание 6')

def phi(x):
    return 1 / (x + 1)

def dphi(x):
    return -1 / (x + 1) ** 2

def simple_iteration(x0, epsilon):
    iterations = []
    k = 0
    x_old = x0

    while True:
        k += 1
        x = phi(x_old)
        fx = f(x)
        error = abs(x - x_old)
        iterations.append((k, x_old, x, error, fx))

        if error < epsilon:
            break
        x_old = x

    return x, iterations

def print_simple_iteration_result(iterations, x0, epsilon):

    print(f"x0 = {x0}, е = {epsilon}")
    print(f"{'k':>3} " 
          f"{'x_k':>15} " 
          f"{'x_{k+1}':>15} " 
          f"{'|ошибка|':>15} " 
          f"{'|f(x)|':>15}")

    for k, x_old, x, error, fx in iterations:
        print(f"{k:>3} " 
              f"{x_old:>15.9f} " 
              f"{x:>15.9f} " 
              f"{error:>15.5e} " 
              f"{abs(fx):>15.5e}")

    root = iterations[-1][2]

    print(f"Корень: {root:.10f}")
    print(f"f(x) = {f(root):.10f}")
    print(f"Невязка |f(x)| = {abs(f(root)):.5e}")

x1, iterations1 = simple_iteration(0.5, 10**(-3))
print_simple_iteration_result(iterations1, 0.5, 10**(-3))

x2, iterations2 = simple_iteration(0.5, 10**(-5))
print_simple_iteration_result(iterations2, 0.5, 10**(-5))

#задание 7
print()
print('задание 7')
print("Проверка условия сходимости |ф'(x)| < 1 на [0.5; 1]")
print(f"{'x':>12} {'|dphi(x)|':>15}")

max_dphi = 0
for x in x_values:
    d = abs(dphi(x))
    if d > max_dphi:
        max_dphi = d

    print(f"{x:>12.6f} {d:>15.6f}")

print(f"максимум |ф'(x)| на [0.5; 1] = {max_dphi:.6f}")

if max_dphi < 1:
    print("условие сходимости простой итерации выполняется")
else:
    print("условие сходимости простой итерации НЕ выполняется")

#проверка через библиотеки
#задание 8
print()
print("Проверка результатов с помощью SciPy")

print("Точность e = 0.001")
root_scipy_bisect_1 = bisect(f, a, b, xtol=10**(-3))
print(f"scipy.optimize.bisect:        x* = {root_scipy_bisect_1:.10f}")

root_scipy_newton_1 = newton(f, 0.5, fprime=df, tol=10**(-3))
print(f"scipy.optimize.newton:        x* = {root_scipy_newton_1:.10f}")

res_scipy_root_1 = root_scalar(f, bracket=[a, b], method='brentq', xtol=10**(-3))
print(f"scipy.optimize.root_scalar:   x* = {res_scipy_root_1.root:.10f}")

print()
print("Точность e = 1e-05")
root_scipy_bisect_2 = bisect(f, a, b, xtol=10**(-5))
print(f"scipy.optimize.bisect:        x* = {root_scipy_bisect_2:.10f}")

root_scipy_newton_2 = newton(f, 0.5, fprime=df, tol=10**(-5))
print(f"scipy.optimize.newton:        x* = {root_scipy_newton_2:.10f}")

res_scipy_root_2 = root_scalar(f, bracket=[a, b], method='brentq', xtol=10**(-5))
print(f"scipy.optimize.root_scalar:   x* = {res_scipy_root_2.root:.10f}")

#таблица сравнения
print()
print("Таблица сравнения")

bisect_1 = bisection(a, b, 10**(-3))
bisect_2 = bisection(a, b, 10**(-5))

chord_1_root, chord_1_iter = chord(a, b, 10**(-3))
chord_2_root, chord_2_iter = chord(a, b, 10**(-5))

newton_05_1_root, newton_05_1_iter = newton_method(0.5, 10**(-3))
newton_05_2_root, newton_05_2_iter = newton_method(0.5, 10**(-5))
newton_10_1_root, newton_10_1_iter = newton_method(1.0, 10**(-3))
newton_10_2_root, newton_10_2_iter = newton_method(1.0, 10**(-5))

simple_1_root, simple_1_iter = simple_iteration(0.5, 10**(-3))
simple_2_root, simple_2_iter = simple_iteration(0.5, 10**(-5))

scipy_vals = {
    "1e-3": (root_scipy_bisect_1, root_scipy_newton_1, res_scipy_root_1.root),
    "1e-5": (root_scipy_bisect_2, root_scipy_newton_2, res_scipy_root_2.root),
}

rows = [
    ("Бисекция",         "1e-3", bisect_1[-1][3],  len(bisect_1),      0, "1e-3"),
    ("Бисекция",         "1e-5", bisect_2[-1][3],  len(bisect_2),      0, "1e-5"),
    ("Хорды",            "1e-3", chord_1_root,     len(chord_1_iter),  0, "1e-3"),
    ("Хорды",            "1e-5", chord_2_root,     len(chord_2_iter),  0, "1e-5"),
    ("Ньютон x0=0.5",    "1e-3", newton_05_1_root, len(newton_05_1_iter), 1, "1e-3"),
    ("Ньютон x0=0.5",    "1e-5", newton_05_2_root, len(newton_05_2_iter), 1, "1e-5"),
    ("Ньютон x0=1.0",    "1e-3", newton_10_1_root, len(newton_10_1_iter), 1, "1e-3"),
    ("Ньютон x0=1.0",    "1e-5", newton_10_2_root, len(newton_10_2_iter), 1, "1e-5"),
    ("Простая итерация", "1e-3", simple_1_root,    len(simple_1_iter), 2, "1e-3"),
    ("Простая итерация", "1e-5", simple_2_root,    len(simple_2_iter), 2, "1e-5"),
]

print(f"{'Метод':<18} {'e':>5} {'x*':>14} {'Итер.':>6} {'|f(x*)|':>11} {'SciPy':>14}")

for name, eps, root, n_iter, scipy_idx, scipy_eps in rows:
    nevyazka = abs(f(root))
    scipy_x = scipy_vals[scipy_eps][scipy_idx]

    print(f"{name:<18} {eps:>5} {root:>14.10f} {n_iter:>6} {nevyazka:>11.3e} {scipy_x:>14.10f}")
