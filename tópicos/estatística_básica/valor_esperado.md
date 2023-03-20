# Valor Esperado (Esperança)

Dada uma v.a. $X$ que pode assumir valores $x_1, x_2, x_3, \dots\ x_n$, o valor esperado de $X$ é

$$E[X] = \sum_{i=1}^{n}{x_iP(X = x_i)}$$

## Exemplo com um dado

|$X$|1|2|3|4|5|6|
|-|-|-|-|-|-|-|
|$P(X)$|$\frac{1}{6}$|$\frac{1}{6}$|$\frac{1}{6}$|$\frac{1}{6}$|$\frac{1}{6}$|$\frac{1}{6}$|

$$X : \{1, 2, 3, 4, 5, 6\} \rightarrow \left\{\frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}, \frac{1}{6}\right\}$$

$$E[X] = \sum_{i=1}^{6}{iP(X=i)}$$

$$E[X] = 1\left(\frac{1}{6} \right) + 2\left(\frac{1}{6} \right) + 3\left(\frac{1}{6} \right) + 4\left(\frac{1}{6} \right) + 5\left(\frac{1}{6} \right) + 6\left(\frac{1}{6} \right)$$

$$E[X] = \left(\frac{1}{6}\right)(1+2+3+4+5+6)$$

$$E[X] = \frac{21}{6} = \frac{7}{2} \approx 3.5$$

## Exemplo com peças

Um fabricante produz peças, tais que 10% delas são defeituosas e 90% são perfeitas. Se uma peça defeituosa for produzida, o fabricante perde R\$ 1,00, enquanto que uma peça não defeituosa lhe dá um lucro de R\$ 5,00. Se $X$ for o lucro líquido, qual é o lucro esperado desse fabricante?

$$X : \{-1, \ 5\} \rightarrow \left\{\frac{1}{10}, \ \frac{9}{10} \right\}$$

$$E[X] = -1 \left(\frac{1}{10}\right) + 5 \left(\frac{9}{10}\right)$$

$$E[X] = \frac{45}{10} -\frac{1}{10} = \frac{44}{10} \approx 4.40$$

## Exemplo com caça-níquel