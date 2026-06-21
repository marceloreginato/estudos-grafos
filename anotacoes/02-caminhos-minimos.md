# Caminhos mínimos

### Algoritimo Dijkstra

Resolve o problema de caminhos mais curtos de única origem em um grafo ponderado G(V, E), todos os pesos são não negativos. O algoritmo mantém um conjunto S de vértices com pesos finais desde a origem s já computados.

- Lista de vértices não visitados
- Tabela de distâncias da fonte:
    - 0 para a fonte
    - infinito para todos os outros
- Enquanto existirem vértices não visitados:
    - Escolher o vértice não visitado com menor distância na tabela
    - Marcar esse vértice como visitado
    - Para cada vizinho dele:
        - Calcular distância alternativa (distância atual + peso da aresta)
        - Se essa distância for menor que a registrada na tabela:
        - Atualizar a tabela de distâncias

Complexidade: **O(|E| + |V| log |V|)**

### Algoritimo Caminhos mínimos de fonte única em grafos acíclicos dirigidos

Relaxa-se as arestas de acordo com uma ordenação topológica.

- Criar uma tabela de distâncias:
    - 0 para o vértice de origem
    - infinito para todos os outros
- Obter uma ordenação topológica dos vértices
- Para cada vértice na ordem topológica:
    - Para cada aresta que sai desse vértice:
        - Se a distância do vértice atual + peso da aresta for menor que a distância do destino:
            - Atualizar a distância do destino (relaxamento)
    
Complexidade: **O(V + E)**

### Algoritmo Bellman-Ford

Resolve caminhos mínimos de fonte única no caso geral (arestas podem ser negativas). Devolve um valor booleano indicando se existe ou não um ciclo negativo que pode ser alcançado da fonte, se o ciclo negativo não existir produz o caminho mínimo.

- Criar uma tabela de distâncias:
  - 0 para o vértice de origem
  - infinito para todos os outros vértices
- Repetir |V| - 1 vezes:
  - Percorrer todas as arestas do grafo
  - Calcular a distância alternativa (distância atual + peso da aresta)
  - Se a nova distância for menor que a registrada:
    - Atualizar a tabela de distâncias
- Percorrer todas as arestas mais uma vez:
  - Se ainda for possível diminuir alguma distância:
    - Existe um ciclo de peso negativo acessível a partir da origem

Complexidade: **O(|V| * |E|)**