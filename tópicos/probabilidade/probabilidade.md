# Probabilidade

## Definição
A probabilidade de um evento $E$, denotada por $P(E)$ é um número no intervalo $[0,1]$, sendo

$$P(E) = \frac{n(E)}{n(S)}$$

Onde

- $n(E)$ é o número de ocorrências do evento de interesse;
- $n(S)$ é o tamanho do espaço amostral;

## Consequências da definição

- **Evento complementar**

$$ P(\bar{A}) = 1 - P(A) $$

## Exclusividade de eventos

**Eventos mutuamente exclusivos**

Eventos mutuamente exclusivos são eventos que não podem ocorrer ao mesmo tempo. Ou seja, a ocorrência de um evento exclui a possibilidade de o outro evento ocorrer. Se dois eventos são mutuamente exclusivos, então

$$P(A \cup B) = P(A) + P(B)$$
$$P(A \cap B) = 0$$

- **Exemplo 1: eventos mutuamente exclusivos**

    Por exemplo, ao jogar uma moeda, o evento "obter cara" e o evento "obter coroa" são mutuamente exclusivos, pois não podem ocorrer ao mesmo tempo.

**Eventos não mutuamente exclusivos**

Eventos não mutuamente exclusivos são eventos que podem ocorrer ao mesmo tempo. Ou seja, a ocorrência de um evento não exclui a possibilidade de o outro evento ocorrer, sendo

$$ P(A \cup B) \ne P(A) + P(B) $$
$$P(A \cap B) \ne 0$$

- **Exemplo 2: eventos não mutuamente exclusivos**

    Por exemplo, ao lançar um dado, os eventos "obter um número par" e "obter um número maior que 4" não são mutuamente exclusivos, pois é possível obter um número que seja par e maior que 4 ao mesmo tempo.

## Dependência e Independência

**Eventos independentes**

Dois eventos são independentes se a ocorrência de um evento não afeta a probabilidade do outro evento ocorrer. Formalmente, dois eventos A e B são independentes se e somente se a probabilidade da ocorrência conjunta de $A$ e $B$ é o produto das probabilidades individuais de $A$ e $B$

$$ P(A \cap B) = P(A) \cdot P(B) $$
$$ P(B|A) = P(B) $$
$$ P(A|B) = P(A) $$

- **Exemplo 1: eventos independentes**

    Por exemplo, suponha que você jogue uma moeda e role um dado. As probabilidades de obter cara na moeda e um número ímpar no dado são independentes, pois a ocorrência de cara na moeda não afeta a probabilidade de um número ímpar no dado e vice-versa.

**Eventos dependentes**

Eventos dependentes são aqueles em que a ocorrência de um evento afeta a probabilidade de o outro evento ocorrer. Dois eventos A e B são dependentes se a probabilidade da ocorrência conjunta de A e B não é o produto das probabilidades individuais de A e B. Nesse caso, a probabilidade de B é condicionada pela ocorrência ou não de A.

$$ P(A \cap B) \ne P(A) \cdot P(B) $$
$$ P(B|A) \neq P(B) $$
$$ P(A|B) \neq P(A) $$

- **Exemplo 2: eventos dependentes**

    Por exemplo, suponha que você retire uma carta de um baralho e, sem substituí-la, retire outra carta. A probabilidade de obter um Ás na segunda carta depende da carta que foi retirada na primeira vez. Se você retirou um Ás na primeira vez, a probabilidade de obter outro Ás na segunda carta é menor do que se você não tivesse retirado um Ás na primeira vez. Nesse caso, os eventos são dependentes.

## Probabilidade condicional

A probabilidade condicional ocorre em **eventos dependentes**. A probabilidade condicional de dois eventos é dada por:

$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$
$$ P(B|A) = \frac{P(A \cap B)}{P(A)} $$

## Teorema de Bayes

O Teorema de Bayes estabelece uma relação entre as probabilidades condicionais de dois eventos

$$P(A|B) = \frac{P(A|B) \cdot P(B)}{P(B)}$$
$$P(B|A) = \frac{P(B|A) \cdot P(A)}{P(A)}$$

Onde

- $P(A|B)$ é a probabilidade de $A$ ocorrer dado que $B$ ocorreu;
- $P(B|A)$ é a probabilidade de $B$ ocorrer dado que $A$ ocorreu;
- $P(A)$ e $P(B)$ são as probabilidades de $A$ e $B$, respectivamente;

## Eventos mutuamente exclusivos

### União de eventos

- **União de dois eventos independentes ou dependentes**

$$P(A \cup B) = P(A) + P(B)$$

### Intersecção de eventos

- **Intersecção de dois eventos independentes ou dependentes**

    A interseção dos eventos é impossível, pois eles não podem ocorrer simultaneamente.

## Eventos não mutuamente exclusivos

### União de eventos

- **União de dois eventos independentes**

$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$

- **União de dois eventos dependentes**

    A união entre dois eventos dependentes e mutuamente exclusivos é impossível, pois eles não podem ocorrer simultaneamente.

### Intersecção de eventos

- **Intersecção de dois eventos independentes**

$$P(A \cap B) = P(A) \cdot P(B)$$

- **Intersecção de dois eventos dependentes**

$$P(A \cap B) = P(A|B) \cdot P(B)$$

## Organização por dependência/independência de eventos

- **Eventos dependentes**;
    - Eventos mutuamente exclusivos;
        - União;
        - Intersecção;
    - Eventos não mutuamente exclusivos;
        - União;
        - Intersecção;
- **Eventos independentes**;
    - Eventos mutuamente exclusivos;
        - União;
        - Intersecção;
    - Eventos não mutuamente exclusivos;
        - União;
        - Intersecção;

## Organização por exclusividade de eventos

- **Eventos mutuamente exclusivos**;
    - Eventos independentes;
        - União;
        - Intersecção;
    - Eventos dependentes;
        - União;
        - Intersecção;
- **Eventos não mutuamente exclusivos**;
    - Eventos independentes;
        - União;
        - Intersecção;
    - Eventos dependentes;
        - União;
        - Intersecção;