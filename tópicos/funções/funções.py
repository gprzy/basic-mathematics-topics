from math import log10

funcao_afim = lambda x, a=2, b=3: a*x + b
funcao_quadratica = lambda x, a=1, b=2, c=3: a*x**2 - b*x + c
funcao_cubica = lambda x, a=1, b=2, c=3, d=2: a*x**3 - b*x**2 + c*x + d
funcao_logaritmica = lambda x: log10(x)
funcao_exponencial = lambda x, a=2: a**x
funcao_modular = lambda x: abs(x)
funcao_par = lambda x, f: f(x) == f(-x)
funcao_impar = lambda x, f: f(x) == -f(-x)
funcao_composta = lambda x, f, g: f(g(x))

print('função linear com x = 4; y =', funcao_afim(4))
print('função quadrática com x = 2; y =', funcao_quadratica(2))
print('função cúbica com x = 2; y =', funcao_cubica(2))
print('função logarítmica com x = 1003; y =', funcao_logaritmica(1003))
print('função exponencial com x = 4; y =', funcao_exponencial(4))
print('função modular com x = -4; y =', funcao_modular(-4))
print('função f(x) = 5x - 6 é par?', funcao_par(4, lambda x: 5*x - 6))
print('função f(x) = -5x + 6 é ímpar?', funcao_impar(4, lambda x: -5*x + 6))

print('função composta de f(x) = 2x + 2 e g(x) = x² - 3 em x = 4; y =',
    funcao_composta(
        x=4,
        f=lambda x: 2*x + 2,
        g=lambda x: x**2 - 3
    )
)
