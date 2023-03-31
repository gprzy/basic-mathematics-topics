# Matrizes

## Definição

Uma matriz é uma tabela retangular de números ou expressões, chamados de elementos da matriz.

Uma matriz com $m$ linhas e $n$ colunas é chamada de matriz $m \times n$ e é representada da seguinte forma:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} \\
\end{bmatrix}
$$

## Operações com matrizes

**Soma**

A soma de duas matrizes $A$ e $B$, ambas de dimensões $m \times n$, é uma matriz $C$ de dimensões $m \times n$ dada por:

$$
A + B =
\begin{bmatrix}
a_{11} + b_{11} & a_{12} + b_{12} & \cdots & a_{1n} + b_{1n} \\
a_{21} + b_{21} & a_{22} + b_{22} & \cdots & a_{2n} + b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} + b_{m1} & a_{m2} + b_{m2} & \cdots & a_{mn} + b_{mn}
\end{bmatrix}
$$

**Subtração**

A subtração de duas matrizes $A$ e $B$, ambas de dimensões $m \times n$, é uma matriz $C$ de dimensões $m \times n$ dada por:

$$
A - B =
\begin{bmatrix}
a_{11} - b_{11} & a_{12} - b_{12} & \cdots & a_{1n} - b_{1n} \\
a_{21} - b_{21} & a_{22} - b_{22} & \cdots & a_{2n} - b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} - b_{m1} & a_{m2} - b_{m2} & \cdots & a_{mn} - b_{mn}
\end{bmatrix}
$$

**Multiplicação por escalar**

A multiplicação de uma matriz $A$ por um escalar $k$ é uma matriz $B$ de dimensões $m \times n$ dada por:

$$
kA =
\begin{bmatrix}
ka_{11} & ka_{12} & \cdots & ka_{1n} \\
ka_{21} & ka_{22} & \cdots & ka_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
ka_{m1} & ka_{m2} & \cdots & ka_{mn}
\end{bmatrix}
$$

**Multiplicação de matrizes**

A multiplicação de uma matriz $A$ de dimensões $m \times n$ por uma matriz $B$ de dimensões $n \times p$ é uma matriz $C$ de dimensões $m \times p$ dada por:

$$
AB =
\begin{bmatrix}
c_{11} & c_{12} & \cdots & c_{1p} \\
c_{21} & c_{22} & \cdots & c_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
c_{m1} & c_{m2} & \cdots & c_{mp}
\end{bmatrix}
$$

em que

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$
