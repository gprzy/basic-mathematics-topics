# Determinantes

O determinante de uma matriz quadrada $A$ de dimensão $n$ é denotado por $|A|$ ou $\det(A)$.

## Matriz $2 \times 2$

Para uma matriz $A$ de dimensão $2 \times 2$, o determinante é dado por:

$$
\det(A) = \begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = a_{11}a_{22} - a_{12}a_{21}
$$

## Matriz $3 \times 3$

Para uma matriz $A$ de dimensão $3 \times 3$, o determinante é dado por:

$$
\det(A) = \begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix} = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}
$$

## Propriedades

Algumas propriedades dos determinantes são:

- O determinante de uma matriz é igual ao determinante de sua transposta: $\det(A) = \det(A^T)$.
- Se uma matriz tem duas linhas ou colunas iguais, seu determinante é zero.
- Se uma matriz tem uma linha ou coluna que é uma combinação linear das outras linhas ou colunas, seu determinante é zero.
- Se trocarmos duas linhas ou colunas de uma matriz, o determinante muda de sinal: $\det(A) = -\det(A')$, onde $A'$ é a matriz obtida a partir de $A$ pela troca de duas linhas ou colunas.
- Se multiplicarmos uma linha ou coluna de uma matriz por um escalar $k$, o determinante é multiplicado por $k$: $\det(kA) = k^n \det(A)$, onde $n$ é a dimensão da matriz. 

## Regra de Cramer

A regra de Cramer é um método para resolver sistemas de equações lineares usando determinantes. Para um sistema de $n$ equações e $n$ variáveis, com matriz dos coeficientes $A$ e vetor das constantes $b$, a solução é dada por:

$$
x_i = \frac{\det(A_i)}{\det(A)}, \quad i = 1, 2, \ldots, n
$$

em que $A_i$ é a matriz obtida a partir de $A$ substituindo a $i$-ésima coluna por $b$.