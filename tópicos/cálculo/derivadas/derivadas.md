# Derivadas

## Definição de derivadas por limites
$$m = \lim_{h \rightarrow 0}{\frac{f(x+h) - f(x)}{h}}$$

$$f'(x) = \lim_{h \rightarrow 0}{\frac{f(x+h) - f(x)}{h}}$$

**Exemplo 1: encontrando a derivada utilizando limites**

Encontrar a inclinação $m$ da reta tangente (derivada) de $f(x) = x^2 - 2x + 1$ em um ponto genérico $(x,y)$

- Partindo da definição de derivada através de limites

$$m = \lim_{h \rightarrow 0}{\frac{f(x+h) - f(x)}{h}}$$

- Substituindo pela função $f(x) = x^2 - 2x + 1$

$$m = \lim_{h \rightarrow 0}{\frac{((x+h)^2 - 2(x+h) + 1) - (x^2 - 2x + 1)}{h}}$$

$$m = \lim_{h \rightarrow 0}{\frac{(x^2 + 2xh + h^2) + (-2x - 2h + 1) - (x^2 - 2x + 1)}{h}}$$

$$m = \lim_{h \rightarrow 0}{\frac{h(2x + h - 2)}{h}}$$

$$m = \lim_{h \rightarrow 0}{(2x + h - 2)}$$

$$m = 2x + (0) - 2$$

$$m = 2x - 2$$

A inclinação $m$ da reta tangente de $f(x) = x^2 - 2x + 1$ em um ponto genérico $(x,y)$ é expressa pela função $m(x) = 2x - 2$.