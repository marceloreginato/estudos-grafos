# Fluxo máximo

No problema do fluxo máximo em uma rede, deseja-se calcular a maior taxa pela qual pode-se enviar materiais de uma fonte s até um sorvedouro t, sem infringir restrições de capacidades da rede.

Uma rede de fluxo G(V,E) é um grafo dirigido, sem laço, no qual (u,v) tem uma capacidade não negativa, c(u,v) > 0. Ou seja, a capacidade de todas as arestas é positiva

Vértices não acumulam material (conservação do fluxo) e se existe uma aresta (u,v) impomos que não existe (v,u).

## Propriedades

- Se (u,v) não pertence a E, então c(u,v) = 0
- Para todo v em V, existe um caminho de s para v e de v para t (s = fonte e t = sumidouro)
- Para todo u,v pertencentes a V, 0 <= f(u,v) <= c(u,v)
- f(u,v) é o fluxo que passa por aquela aresta
- O fluxo de entrada é igual ao de saída (conservação do fluxo) em vértices que não sejam fonte ou sumidouro

## Caminho aumentador

É um caminho da fonte (s) ao sorvedouro (t) na rede residual Gf.

A **rede residual** será definida por:

cf(u,v) = c(u,v) - f(u,v)

Onde cf(u,v) = capacidade residual

Para um caminho p:

cf(p) = min{cf(u,v) : (u,v) pertencente a p}

Esse é o valor do gargalo do caminho, o fluxo só pode ser aumentado pelo valor do gargalo, esse aumento só ocorre nas arestas pertencentes ao caminho e o algoritmo termina quando não existe mais caminho aumentador.

## Corte e Teorema do Fluxo Máximo-Corte Mínimo

Um corte (S, T) divide os vértices em dois conjuntos de maneira que s pertence a S e t pertence a T. A capacidade do corte é a soma das capacidades das arestas que vão de S para T.

### Teorema do Fluxo Máximo-Corte Mínimo

O teorema diz que o fluxo máximo é igual a capacidade do corte mínimo

## Algoritmo de Ford-Fulkerson


- Fluxo = 0 em todas as arestas
- Usa a rede residual (inicial = capacidades)
    - Enquanto existe caminho aumentador s -> t
    - Encontre um caminho de s até t
    - Só pode usar arestas com capacidade > 0 (residual)
    - Pegue a menor capacidade do caminho
    - Subtrai esse valor nas arestas do caminho
    - Soma nas arestas reversas
    - repete

