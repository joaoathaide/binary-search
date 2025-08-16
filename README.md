# 🔎 Busca binária

Este repositório contém uma implementação simples do algoritmo **Busca Binária (Binary Search)** em Python.  

A busca binária é um algoritmo eficiente para encontrar um valor dentro de uma lista **ordenada**.  
A cada iteração, o algoritmo divide a lista ao meio e descarta a metade que não contém o elemento buscado, reduzindo drasticamente o número de comparações necessárias.

- **Complexidade de tempo:** `O(log n)`  
- **Pré-requisito:** a lista deve estar **ordenada**

Exemplo de uso:

```python
list = [0, 1, 2, 3, 4, 5, 6, 14, 18, 30, 54]
item = 54

result = binary_search(list, item)
print(result)  # retorna o índice do item ou None se não encontrado
