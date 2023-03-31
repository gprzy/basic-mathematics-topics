# Matrizes

## Definição

Uma matriz é uma tabela que dispõe os elementos em linhase colunas.

**Exemplos básicos**

$$
A = \begin{bmatrix}
3 & 1  \\
0 & -4 \\
\end{bmatrix}
$$

Ou então

$$
A = \begin{pmatrix}
3 & 1  \\
0 & -4 \\
\end{pmatrix}
$$

## Ordem de uma matriz

Uma matriz com $m$ linhas e $n$ colunas é possui ordem $m \times n$ e é representada da seguinte forma

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} \\
\end{bmatrix}
$$

## Classificação de matrizes

- **Matriz unitária**
$$A = \begin{bmatrix}3\end{bmatrix}$$

- **Matriz linha**
$$A = \begin{pmatrix}0 & 5 & 7\end{pmatrix}$$

- **Matriz coluna**
$$A = \begin{pmatrix}2 \\ -3\end{pmatrix}$$

- **Matriz retangular**
$$
A = \begin{bmatrix}
2 & 3 & 10 \\
0 & -5 & 7 \\
\end{bmatrix}
$$

- **Matriz quadrada**
$$
A = \begin{pmatrix}
2 & 3 & 10 \\
5 & -4 & 5 \\
7 & 8 & 6 \\
\end{pmatrix}
$$

## Diagonais de uma matriz

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

- **Diagonal principal**
$$
A = \begin{pmatrix}
a_{11} &        &        \\
       & a_{22} &        \\
       &        & a_{33} \\
\end{pmatrix}
$$

- **Diagonal secundária**
$$
A = \begin{pmatrix}
       &        & a_{13} \\
       & a_{22} &        \\
a_{31} &        &        \\
\end{pmatrix}
$$

## Traço de uma matriz quadrada
É a soma dos elementos da diagonal principal.

## Lei de formação de matrizes

**Exemplo 1: lei de formação**
$$A = (a_{ij})_{2 \times 3}$$
$$A = a_{ij} = 2i + 3j$$

$$
A = \begin{pmatrix}
5 & 8 & 11 \\
7 & 10 & 13 \\
\end{pmatrix}
$$

**Exemplo 2: lei de formação com condicional**
$$B = (b_{ij})_{3 \times 3}$$

$$
b_{ij} = \begin{cases}
i + j & \text{ se } i = j \\
i^j & \text{ se } i \ne j
\end{cases}
$$

$$
A = \begin{pmatrix}
2 & 1 & 1 \\
2 & 4 & 8 \\
3 & 9 & 6 \\
\end{pmatrix}
$$

## Matriz transposta
A transposta de uma matriz corresponde à inversão de suas linhas e colunas.

**Exemplo 3: matriz transposta**
$$
A = \begin{pmatrix}
2 & 1 & 3 \\
0 & 5 & 7 \\
\end{pmatrix}
$$

$$
A^T = \begin{pmatrix}
2 & 0 \\
1 & 5 \\
3 & 7 \\
\end{pmatrix}
$$

## Matriz simétrica
É a matriz quadrada que é igual a sua transposta,

$$A = A^T$$

**Exemplo 4: matriz simétrica**

$$
A = \begin{pmatrix}
3 & 1 & 2 \\
1 & 4 & 3 \\
2 & 3 & 5 \\
\end{pmatrix}
$$

## Matriz antisimétrica
É a matriz que satisfaz

$$A^T = -A$$

**Exemplo 5: matriz antisimétrica**

$$
A = \begin{pmatrix}
0 & 3 \\
-3 & 0 \\
\end{pmatrix}
$$

$$
A^T = \begin{pmatrix}
0 & -3 \\
3 & 0 \\
\end{pmatrix}
$$

$$
-A = \begin{pmatrix}
0 & -3 \\
3 & 0 \\
\end{pmatrix}
$$

$$\therefore A^T = -A$$

## Igualdade de matrizes
Duas matrizes são iguais se todos os seus elementos forem iguais.

## Matriz identidade

**Exemplos básicos**

$$
I = \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

$$
I = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

## Matriz inversa
Seja $A$ uma matriz quadrada, sua inversa será $A^{-1}$, tal que

$$A^{-1}A = I$$

**Exemplo 6: matriz inversa**

Determine, caso exista, a matriz inversa de

$$
A = \begin{pmatrix}
2 & 0 \\
4 & -3 \\
\end{pmatrix}
$$

Matriz inversa desconhecida

$$
A^{-1} = \begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}
$$

Deve-se satisfazer a igualdade

$$
\begin{pmatrix}
2 & 0 \\
4 & -3 \\
\end{pmatrix}

\times

\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}

= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

$$
\begin{pmatrix}
2a + 0c & 2b + 0d \\
4a - 3c & 4b - 3d \\
\end{pmatrix}

= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

$$
\begin{pmatrix}
2a & 2b \\
4a - 3c & 4b - 3d \\
\end{pmatrix}

= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

Encontrando $a$

$$2a = 1$$
$$a = \frac{1}{2}$$

Encontrando $b$

$$2b = 0$$
$$b = 0$$

Substituindo

$$
\begin{pmatrix}
2 \left( \frac{1}{2} \right) & 2(0) \\
4\left( \frac{1}{2} \right) - 3c & 4(0) - 3d \\
\end{pmatrix}

= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

$$
\begin{pmatrix}
1 & 0 \\
2 - 3c & -3d \\
\end{pmatrix}

= \begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$

Encontrando $c$

$$2 - 3c = 0$$
$$c = \frac{-2}{-3}$$
$$c = \frac{2}{3}$$

Encontrando $d$

$$-3d = 1$$
$$d = -\frac{1}{3}$$

Portanto, a matriz inversa $A^{-1}$ é

$$
A^{-1} = \begin{pmatrix}
1/2 & 0 \\
2/3 & -1/3 \\
\end{pmatrix}
$$