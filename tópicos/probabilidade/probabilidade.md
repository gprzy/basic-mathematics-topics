# Probabilidade

- A probabilidade de um evento $A$, denotada por $P(A)$, é um número no intervalo $[0,1]$ que indica a chance de que o evento ocorra.

- A probabilidade do evento complementar de $A$, denotada por $P(\bar{A})$, é dada por:

$$ P(\bar{A}) = 1 - P(A) $$

- A probabilidade da união de dois eventos $A$ e $B$, denotada por $P(A \cup B)$, é dada por:

$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

- Dois eventos são ditos mutuamente exclusivos se eles não podem ocorrer simultaneamente. Se $A$ e $B$ são mutuamente exclusivos, então:

$$ P(A \cup B) = P(A) + P(B) $$

- Dois eventos são independentes se a ocorrência de um evento não afeta a probabilidade do outro evento ocorrer. Se $A$ e $B$ são independentes, então:

$$ P(A \cap B) = P(A) \cdot P(B) $$

## Dependência e Independência

- A probabilidade condicional do evento $B$ dado que o evento $A$ ocorreu, denotada por $P(B|A)$, é dada por:

$$ P(B|A) = \frac{P(A \cap B)}{P(A)} $$

- Dois eventos $A$ e $B$ são dependentes se a probabilidade de $B$ ocorrer é afetada pela ocorrência ou não de $A$. Se $A$ e $B$ são dependentes, então:

$$ P(B|A) \neq P(B) $$