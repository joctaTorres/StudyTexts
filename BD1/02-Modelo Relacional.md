# Modelo Relacional

## Conceitos Básicos:

+ Aspecto Estrutural:
   + O banco de dados é representado como uma coleção de relações (ou tabelas ou entidade).
+ Aspecto de Integradade:
   + As relações satisfazem certas restrições de integridade.
+ Aspecto de manipulção:
   + ...

O modelo relacional de Dados representa o banco de dados com uma coleção de relações

#### Informalmente:

+ Uma relação se assemelha a uma tabela
+ Cada linha da tabela representa uma coleção de valores de dados relacionados
+ Cada linha de uma tabela representa um fato do mundo real: uma instância de uma entidade ou de relacionamento.
+ O nomes da coluna especificam um dado da instância.

## Terminologia formal:

+ Uma linha é chamada de **_tupla_**
+ O título de coluna é chamado de atributo
+ ...



## Esquema de uma relação

**R(A1, A2, ..., An)** é uma relação _R_ de _n_ atributos _A_;
Cada atributo _A_ é uma "coluna", um papel desempenhando por algun domíno _D_ no esquema da relação _R_.

_Domínio_: Conjunto de valores atômico - indivisíveis.

Exemplo de relação:

Aluno(nome, endereço, telefone)

Dom(...)...

#### Tupla:
Corresponde a uma lista ordenada de valores t=< v1, v2, ..., vn>, onde cada valor _v_ é um elemento do dom(A) ou um valor especial nulo. Uma relação r(R) é um conjunto de _n-tuplas_.

> r(R) = {t1, t2, ..., tn}

#### Grau:

...

![relacoes](https://www.google.com.br/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjhtO3ZruzcAhXOl5AKHZLHDfsQjRx6BAgBEAU&url=https%3A%2F%2Fgeobrainstorms.wordpress.com%2Ftag%2Fbanco-de-dados%2F&psig=AOvVaw0PdIfjU__5kPBFuZQ58qFQ&ust=1534329958805148 )

## Caractérísticas das Relações;

+ Uma relação é um conjunto de tuplas, matematicamente não existe ordenamento entre os elementos de um conjunto

+ Não existem tuplas duplicadas

+ Não existem apontadores

+ Tods os atributos são atômicos, valores compostos

+ valores nulos representam a ausência de valor

#### Interpretação da Relação:

+ O esquema de uma relação é uma afirmação cada tupla é um fato. Uma relação representa fatos sobre as entidades e relacionamentos.

## Chaves:

#### Chaves primárias _- Primary Key (PK)_:

Um conjunto de atributos **únicos** e **não nulos** _(not null -  nn)_ com característica de **minimalidade**, que identificam unicamente uma tupla em uma tabela.

**_OBS.:_ A chave primária é única para uma tabela, porém não precisa necesariamente estar uma coluna apenas, podemos ter uma PK composta por uma ou mais coluna, formando um chave primária única para cada registro tuplas**

#### Chaves estrangeira _- Foreign Key (FK)_:

Um atributo ou uma combinação de atributos, cujos valores aparecem necessariamente na chave primária de uma outra relação ou da mesma relação.

Ou seja, uma _FK_ em uma tabela é uma _PK_ em outra (ou na mesma tabela, em relacionamento unário).

> t1[FK] = t2[PK]

## Restrições de integridade

#### Integridade de Entidade:

Toda tuplas de uma mrelação é unicamente indentificada por um oui mais atributos definidos como _"chave primária"_, cujos valores dos atributos não pode conter valores

#### Integridade Referencial:
...

#### Integridade de Domínio:
...


## Operações de atualização:

#### Inserção (_insert_):

Fornece uma lista de valores dos atributos para umas nova tupla.

> _insert_ <001, "Cecília", "Rua São Paulo", 3000> in _Empregado_

Pode violar:
+ restrição de domíno
   + insere um campo com tipo incompatível ( existem SGDB que converte os tipos)
+ integridade de entidade
   + insert que a tupla tem uma chave primária não válida
+ ingridade referencial
   + inserir uma tupla que possui uma foreign key não válida

#### Exclusão (_delete_):

Elimina uma tupla da relação, utiliza uma condição nos atruibutos para sele.

> _insert_ <001, "Cecília", "Rua São Paulo", 3000> in _Empregado_

Pode violar:
+ ingridade referencial
   + apagar uma tupla que a é FK em uma outra tabela

Opções para violação:
+ Rejeitar a exclusão
+ Exclusão em cascata
   + Tudo que estiver _linkado (todas as tuplas relacionada com a PK sendo deletada)_ à tupla sendo deletada é também apagado.
+ Alterar para _null_


#### Atualização (_update_):

Altera valores de um ou mais atributos numa tupla(s). Especifica uma condição nos atributos para selecionar a tupla a ser modificada.

> _atualize_ o salário da tupla Empregado

...



