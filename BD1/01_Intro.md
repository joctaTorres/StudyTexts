# Introdução

Os Bancos de dados surgem como iniciativa de ***organização de dados***. BDs são construídos utlizando estrutura de dados. Dessa forma os programas podem ter acesso aos dados de maneira uniforme.
Um _BD_ é projetado, construído e povoado com dados que possuem um objetivo específico.
Os bancos relacionais são estruturados em forma de tabela.

## Características dos Bancos de Dados:
- Armazenamento estruturado,
- Acesso rápido,
- Resposta rápiuda
- Buscas rápidas,
- Conter grande volume de informação (gb, tb...)
- Disponibilidade em rede
- Leitura não sequencial

Além de recursos de segurança:
- Consegue controlar acesso
- Ter usuários com diferentes níveis de acesso e permissões
- Não permite a entrada de dados inconsistentes

## Vantagens na Utilização de BD:

+ Persistência das estruturas dos dados e procedimento
+ Controle de redundância / consistência
+ Compartilhamento
+ Restrição de segurança
+ Suporte a transação
+ Utilização de regras de restrição de integridade
+ Independência de Dados
+ Capacidade de recuperação e cópias
+ Múltiplas interfaces para usuários


## Conceitos Importantes de Banco de Dados:

1. Redundância:
   * Ocorre quando um mesmo dado é armazenado em mais de uma área do banco de dados (ou há backup de dados).

2. Consistência

3. Integridade:
   * Diz respeito ao nível de confiança/credibilidade das informações do banco de dados.
   * Regras de restrição..

4. Restrições de segurança:
   * A restrição de segurança diz respeito a permissão de acesso, por determinados usuários, a determinadas..

## Histórico

+  1980 - 1983:
   + SQL Definido como padrão ANSI

SQL Ansi é uma padrão que é utilizado como base como construção de outras linguagens, então chamadas de _SQL-Based_

## Como funciona o SQL

## SGBD

Sistema de Gerenciamento de Banco de Dados é um conjunto de programas que permite acessar diferentes bancos de dados organizados sob um mesmo servidor de dados.

> "Seu principal objetivo é retirar da aplicação cliente a responsabilidade de gerenciar o acesso, a persistência, a manipulação e a organização dos dados. O SGBD disponibiliza uma interface para que seus clientes possam incluir, alterar ou consultar dados previamente armazenados. Em bancos de dados relacionais a interface é constituída pelas APIs (Application Programming Interface) ou drivers do SGBD, que executam comandos na linguagem SQL"


### Capacidades do SGBD

+ Definição de Dados
+ Manipulação de Dados
+ Segurança e Integridade
+ Utilitários para Salvar, Recuperar e Reorganizar
+ Controle de Concorrência
+ Catálogo/Otimizador
+ Desempenho

## Quem usa SGBD

+ Analista DBA:
   + Projeta a estrutura do BD - nomes de tabelas, nome dos campos, tamanho dos campos, valores válidos, relacionamento entre tabelas.
   + Estabelecer que usuários podem acessar quais informações
   + Criar e Manter os Objetos do BD
   + Fazer carga de dados
   + Gerenciar, salvar, recuperar dados
   + Monitorar o desempenho do SGBD
   + Não necessariamente está relacionado _apenas a BD_, pode ser também ser responsável por manter os servidores (quanto de Ram, quanto de CPU) um serviço que roda no servidor.


# Linguagem de Acesso Estruturada (SQL)

SQL  é composta por:
- Data Dafinition Language - DDL:
   - Difine esquemas
   - Exemplos:
       - _create_
       - _alter_
       - _drop_
- Data Manpulation Language - DML:
   - Manipula esquemas
   - Exemplos:
       - _insert_
       - _update_
       - _select_
       - _delete_
- Data Control Language - DCL:
   - Assegura esquemas
   - Exemplos:
       - _grant_
       - _revoke_
- Data Transaction Language - DTL (ou Transaction Control Languag):
   - Gerenciar as mudanças feitas por instruções DML
   - Exemplos:
       - _begin transaction_
       - _end transaction_
       - _commit_
       - _rollback_






