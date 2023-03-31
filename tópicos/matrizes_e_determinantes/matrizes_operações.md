## Operações com matrizes

$$
A = \begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
\end{pmatrix}
$$

**Soma**

Soma de duas matrizes $A + B$. É necessário que ambas matrizes tenham as mesmas dimensões $m \times n$

$$
A + B =
\begin{pmatrix}
a_{11} + b_{11} & a_{12} + b_{12} \\
a_{21} + b_{21} & a_{22} + b_{22}
\end{pmatrix}
$$

**Subtração**

Subtração de duas matrizes $A - B$. É necessário que ambas matrizes tenham as mesmas dimensões $m \times n$

$$
A - B =
\begin{pmatrix}
a_{11} - b_{11} & a_{12} - b_{12} \\
a_{21} - b_{21} & a_{22} - b_{22}
\end{pmatrix}
$$

**Multiplicação por escalar**

A multiplicação de uma matriz $A$ por um escalar $k$ é uma matriz $B$ de dimensões $m \times n$ dada por:

$$
kA =
\begin{pmatrix}
ka_{11} & ka_{12} \\
ka_{21} & ka_{22}
\end{pmatrix}
$$

**Multiplicação de matrizes**

Condições para multiplicar duas matrizes:
- O nº de linhas da primeira deve ser igual ao número de colunas da segunda (ou vice-versa);
- A matriz resultante $C$ terá as dimensões

$$A_{m \times n} B_{n \times p} = C_{m \times p}$$

Utilizando as matrizes $A$ e $B$

$$
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
b_{31} & b_{32} \\
\end{pmatrix}
$$

A multiplicação será

$$
AB =
\begin{pmatrix}
c_{11} & c_{12} \\
c_{21} & c_{22} \\
\end{pmatrix}
$$

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$

$$
AB =
\begin{pmatrix}
\sum_{k=1}^{n} a_{1k} b_{k1} + \sum_{k=1}^{n} a_{1k} b_{k2} \\
\sum_{k=1}^{n} a_{2k} b_{k1} + \sum_{k=1}^{n} a_{2k} b_{k2}
\end{pmatrix}
$$

$$
AB =
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \\
a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22}
\end{pmatrix}
$$

## Exemplos das operações

$$
A = \begin{pmatrix}
2 & 3 \\
0 & 1 \\
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
2 & 0 \\
3 & 5 \\
\end{pmatrix}
$$

- **Soma**

$$
A + B =
\begin{pmatrix}
2 + 2 & 3 + 0 \\
0 + 3 & 1 + 5
\end{pmatrix}
$$

$$
A + B =
\begin{pmatrix}
4 & 3 \\
3 & 6
\end{pmatrix}
$$

- **Subtração**

$$
A - B =
\begin{pmatrix}
2 - 2 & 3 - 0 \\
0 - 3 & 1 - 5
\end{pmatrix}
$$

$$
A - B =
\begin{pmatrix}
0 & 3 \\
-3 & -4
\end{pmatrix}
$$

- **Multiplicação por escalar**

$$k = 3$$

$$
kA = \begin{pmatrix}
2k & 3k \\
0k & 1k \\
\end{pmatrix}
$$

$$
kA = \begin{pmatrix}
2(3) & 3(3) \\
0 & 3 \\
\end{pmatrix}
$$

$$
kA = \begin{pmatrix}
6 & 9 \\
0 & 3 \\
\end{pmatrix}
$$

- **Multiplicação de matrizes**
$$
A = \begin{pmatrix}
2 & 3 & 1 \\
0 & 1 & 2 \\
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
2 & 0 \\
1 & -1 \\
3 & 5 \\
\end{pmatrix}
$$

$$
AB =
\begin{pmatrix}
(2 \cdot 2) + (3 \cdot 1) + (1 \cdot 3) & (2 \cdot 0) + (3 \cdot -1) + (1 \cdot 5) \\
(0 \cdot 2) + (1 \cdot 1) + (2 \cdot 3) & (0 \cdot 0) + (1 \cdot -1) + (2 \cdot 5)
\end{pmatrix}
$$

$$
AB =
\begin{pmatrix}
(4 + 3 + 3) & (0 + (-3) + 5) \\
(0 + 1 + 6) & (0 + (-1) + 10)
\end{pmatrix}
$$

$$
AB =
\begin{pmatrix}
10 & 2 \\
7 & 9
\end{pmatrix}
$$

## Generalizando as operações
- **Soma e subtração**
$$
A + B =
\begin{pmatrix}
a_{11} \pm b_{11} & a_{12} \pm b_{12} & \cdots & a_{1n} \pm b_{1n} \\
a_{21} \pm b_{21} & a_{22} \pm b_{22} & \cdots & a_{2n} \pm b_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} \pm b_{m1} & a_{m2} \pm b_{m2} & \cdots & a_{mn} \pm b_{mn}
\end{pmatrix}
$$

- **Multiplicação por escalar**
$$
kA =
\begin{pmatrix}
ka_{11} & ka_{12} & \cdots & ka_{1n} \\
ka_{21} & ka_{22} & \cdots & ka_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
ka_{m1} & ka_{m2} & \cdots & ka_{mn}
\end{pmatrix}
$$

- **Multiplicação de matrizes**
$$
AB =
\begin{pmatrix}
c_{11} & c_{12} & \cdots & c_{1p} \\
c_{21} & c_{22} & \cdots & c_{2p} \\
\vdots & \vdots & \ddots & \vdots \\
c_{m1} & c_{m2} & \cdots & c_{mp}
\end{pmatrix}
$$

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
$$