# Integrais

## Definição de integral

A integral de uma função $f(x)$ em um intervalo $[a, b]$ pode ser definida como a área abaixo da curva $y = f(x)$ entre $x = a$ e $x = b$. A integral é denotada por:

$$\int_a^b f(x)dx$$

A integral é calculada dividindo a área sob a curva em um número finito de retângulos e tomando o limite quando o número de retângulos se aproxima do infinito. Isso é conhecido como a soma de Riemann.

## Definição de integral utilizando a soma de Riemann

A definição de integral usando a soma de Riemann é dada pela seguinte expressão:

$$\int_a^b f(x)dx = \lim_{n\rightarrow \infty}\sum_{i=1}^n f(x_i^*) \Delta x$$

onde $x_i^*$ é um ponto dentro do $i$-ésimo subintervalo $[x_{i-1}, x_i]$, $\Delta x = \frac{b-a}{n}$ é o comprimento de cada subintervalo e $n$ é o número de subintervalos. A expressão acima é a soma de Riemann da função $f(x)$ em relação ao intervalo $[a, b]$.