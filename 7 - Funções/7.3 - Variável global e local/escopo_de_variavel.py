# Variável global
x = 50

def f():
    # Variável local
    x = 20
    print(x)

print(x)  # 50
f()       # 20
print(x)  # 50