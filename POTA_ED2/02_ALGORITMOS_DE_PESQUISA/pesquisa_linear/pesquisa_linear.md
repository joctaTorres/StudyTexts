
# Pesquisa Linear

Costuma-se usar o termo busca linear ou pesquisa linear (ou ainda busca sequencial) para expressar um tipo de pesquisa em vetores ou listas de modo sequencial. Ou seja, a busca ocorre elemento por elemento.

Como a busca é feita elemento a elemento, em um vetor não ordenado, a função do tempo em relação ao número de elementos é linear, ou seja, cresce proporcionalmente. No melhor caso, o elemento a ser buscado é encontrado logo na primeira tentativa da busca. No pior caso, o elemento a ser buscado encontra-se na última posição e são feitas N comparações, sendo N o número total de elementos. No caso médio, o elemento é encontrado após (N+1)/2 comparações. O algoritmo de busca linear é um algoritmo O(n).

> Para um vetor ordenado, essa não é a pesquisa a pesquisa linear não é eficiente. A pesquisa (ou busca) binária, por exemplo, é um tipo de pesquisa que apresenta melhor performance para esse casos.