# Análise Combinatória

## Princípio Fundamental da Contagem (PFC)

- Se um evento pode ocorrer em $n_1$ formas diferentes, um segundo evento em $n_2$ formas diferentes, um terceiro evento em $n_3$ formas diferentes e assim por diante, então o número total de maneiras diferentes que os eventos podem ocorrer em sequência é dado por

$$ N = n_1 \times n_2 \times n_3 \times \cdots $$

- Se um evento pode ocorrer em $n_1$ formas diferentes, um segundo evento em $n_2$ formas diferentes, um terceiro evento em $n_3$ formas diferentes e assim por diante, e se a ordem dos eventos for importante, então o número total de maneiras diferentes que os eventos podem ocorrer em sequência é dado por

$$ N = n_1 \times n_2 $$

## Permutação

- **Permutação simples** de $n$ elementos distintos 

$$ P_{n} = n! $$

- **Permutações com repetição** de $n$ elementos distintos, onde $n_i$ é o número de elementos do tipo $i$ 

$$ P_{n_1,n_2,\dots,n_k} = \frac{n!}{n_1! n_2! \dots n_k!} $$

- **Permutação circular** de $n$ elementos distintos 

$$ P_c = \frac{(n-1)!}{2} $$

- **Permutação caótica** de $n$ elementos distintos 

$$ P_{ca} = \left\lfloor \frac{n!}{e} + \frac{1}{2} \right\rfloor $$

## Combinação

- **Combinação simples** de $n$ elementos distintos tomados $r$ a $r$

$$ C_{n,r} = \binom{n}{r} = \frac{n!}{r!(n-r)!} $$

- **Combinações com repetição** de $n$ elementos distintos tomados $r$ a $r$

$$ C_{n+r-1,r} = \binom{n+r-1}{r} = \frac{(n+r-1)!}{r!(n-1)!} $$

## Arranjo

- **Arranjo simples** de $n$ elementos distintos tomados $r$ a $r$

$$ A_{n,r} = \frac{n!}{(n-r)!} $$

- **Arranjo com repetição** de $n$ elementos distintos tomados $r$ a $r$

$$ A_{n}^{r} = n^{r} $$