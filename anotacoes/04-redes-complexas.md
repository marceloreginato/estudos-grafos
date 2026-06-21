# Redes Complexas

## 1. Transição de Grafos para Redes Complexas
* **Limitações dos Grafos Clássicos:** Tradicionalmente, grafos codificam relacionamentos entre pares de objetos (vértices e arestas). No entanto, com a evolução da coleta e armazenamento de dados, surgiram sistemas reais de larga escala (redes sociais, biológicas, mapeamento web).
* **Redes Complexas:** São definidas como grafos de **larga escala** com **topologia não trivial**. A simples análise de propriedades básicas não é suficiente para descrevê-las, exigindo ferramentas estatísticas e dinâmicas acopladas à Teoria dos Grafos.
* **Interdisciplinaridade:** É uma área altamente multidisciplinar fundamentada na Matemática (Teoria dos Grafos), Computação (Algoritmos e Estruturas de Dados) e Física (Mecânica Estatística).

## 2. Tipos Principais de Redes de Larga Escala
* **Redes Sociais:** Os vértices representam indivíduos ou atores, e as arestas denotam relações sociais (ex: amizade, e-mail, coautoria científica).
* **Redes de Informação/Conhecimento:** Os nós armazenam informações e as arestas associam essas informações (ex: redes de citação de artigos, páginas da Web com links, redes de palavras).
* **Redes Tecnológicas:** Redes construídas pelo homem (geralmente físicas, com objetos e relacionamentos concretos) com o objetivo de transportar algo (ex: malha aérea, rede de energia elétrica, internet de roteadores, transporte metroferroviário).
* **Redes Biológicas:** Representam interações dentro de sistemas biológicos (ex: redes de interação de proteínas, redes neurais através de sinais elétricos, redes metabólicas).

## 3. Modelos Teóricos de Redes 

### A. Rede Aleatória 
* **Definição:** Modelo desenvolvido por Paul Erdös e Alfréd Rényi que considera a conexão entre cada par de nós com igual probabilidade $p$.
* **Homogeneidade:** Gera uma rede estatisticamente homogênea; é muito incomum encontrar vértices com concentração de ligações (grau) muito alta ou muito baixa.
* **Grau Esperado:** O grau médio $\langle k\rangle$ de um vértice qualquer é definido pela equação:
  $$\langle k\rangle = p(N - 1)$$
  *(onde $N$ é o número total de vértices)*.
* **Distribuição de Graus:** Ao considerar valores altos para $N$ e conectividade média fixa, a distribuição de ligações aproxima-se do **modelo de Poisson**.

### B. Rede Mundo Pequeno
* **Características Topológicas:** Watts e Strogatz (1998) observaram que as redes reais apresentam propriedades híbridas entre redes regulares e aleatórias:
  1. **Alto agrupamento local (coeficiente de aglomeração):** Efeito de vizinhança típico de redes regulares, porém com alguns vértices distantes conectados (conexões fora da vizinhança). 
  2. **Curtas distâncias médias:** Caminhos mínimos pequenos entre os vértices, típico de redes aleatórias.
* **O Modelo:** Funciona como um grafo intermediário com um parâmetro de aleatoriedade $p$. Para $p=0$, o grafo representa uma rede regular pura; para $p=1$, tem-se um grafo aleatório puro. O efeito Mundo Pequeno surge no aumento da aleatoriedade ($0 < p < 1$).

### C. Rede Livre de Escala
* **Definição:** Caracteriza-se por uma grande quantidade de vértices com poucas ligações e alguns poucos vértices com grau muito superior à média.
* **Distribuição de Graus:** Segue uma **Lei de Potência** ($P(k) \sim k^{-\gamma}$), o que gera uma distribuição com **cauda longa**.
* **Hubs:** São os vértices altamente conectados que sustentam a topologia da rede.
* **Propriedades de Resiliência:**
  * **Altamente Tolerante a Falhas:** A rede não deixa de funcionar totalmente caso alguns nós aleatórios falhem (pois a maioria tem poucas conexões).
  * **Altamente Vulnerável a Ataques:** A rede pode colapsar ou "parar" se os *hubs* forem alvos de ataques direcionados e deixarem de funcionar.

## 4. Conceito Adicional
* **Rede Bipartida:** Modelo de rede que possui dois tipos distintos de vértices. Uma regra topológica fundamental é que **não são permitidas ligações entre vértices do mesmo tipo** (ex: rede de usuários e filmes, onde usuários se conectam apenas a filmes e vice-versa).