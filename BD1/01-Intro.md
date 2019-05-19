# Introdução a Banco de Dados

Os Bancos de dados surgem como iniciativa de ***organização de dados***. BDs são construídos utlizando estrutura de dados. Dessa forma os programas podem ter acesso aos dados de maneira uniforme.
Um _BD_ é projetado, construído e povoado com dados que possuem um objetivo específico.

Nesta matéria, estaremos mais focados nos bancos relacionais, que são estruturados em tabelas. Mas vamos explorar e falar sobre os outro tipos de bancos.

## Por que usamos bancos de dados?

Vamos ver em breve tudo sobre a história dos bancos de dados e como (especialmente o modelo relacional) eles se tornaram tão importantes, bem estabelecidos e sobretudo úteis para o mercado e para a humanidade. 

> Hoje, os bancos de dados estão em toda parte, e são muito importantes. O efeito deles em nossas vidas diárias é enorme e nem nos damos conta. De aplicativos climáticos, aos filmes que você assiste on-line, ao banco que cuida do seu dinheiro, ao governo com todas suas informações (e de todos que você conhece), os bancos de dados são responsáveis por muitos dos serviços que utilizamos diariamente.


### Características dos Bancos de Dados:

+ Armazenamento estruturado,
+ Acesso rápido,
+ Resposta rápiuda
+ Buscas rápidas,
+ Conter grande volume de informação (_gb_, _tb_...)
+ Disponibilidade em rede
+ Leitura não sequencial
+ Além de recursos de segurança:
    - Consegue controlar acesso
    - Ter usuários com diferentes níveis de acesso e permissões
    - Não permite a entrada de dados inconsistentes


### Vantagens na Utilização de BD:

+ Persistência das estruturas dos dados e procedimento
+ Controle de redundância / consistência / integridade
+ Compartilhamento
+ Restrição de segurança
+ Suporte a transação
+ Independência de Dados
+ Capacidade de recuperação e cópias
+ Múltiplas interfaces para usuários


### Alguns conceitos Importantes de Banco de Dados:

1. Redundância:
   * Ocorre quando um mesmo dado é armazenado em mais de uma área do banco de dados (ou há backup de dados).

2. Consistência:
    * Implica que o _BD_ não utiliza (isso é, opera ou transaciona) dados que conflitam com outros. Se um processo deixa a base de dados em um estado incorreto, o procedimento é abortado prar manter a consistência e é reportado um erro.

3. Integridade:
   * Em bancos de dados existe o conceito de _integridade relacional_, que diz respeito ao nível de exatidão e consistência dos dados no BD. Para garantir a integridade, a base de dados possue um série de regras de restrição.
   * **_Regras de restrição de integridade_**: A integridade dos dados é tratada nas bases de dados através de uma série de regras. Existem vários tipos de restrições de integridade, como: _Restrição de Chave, Domínio, Integridade de vazio, referencial, da coluna_, entre outras, que serão abordadas posteriormente...

4. Restrições de segurança:
   * A restrição de segurança diz respeito a permissão de acesso, por determinados usuários, a determinadas informaões contidas no banco.
   * Isso permite a atribuição de previlégios, que disponibilizam ao usuário final somente as informações que este precisa ou tem direito de acesso.


***


## Um pouco sobre a história dos bancos de dados

As origens do banco de dados remetem às bibliotecas, governos, empresas e registros médicos antes mesmo de computadores serem inventados. Quando as pessoas perceberam que precisavam ter os meios para armazenar e manter arquivos e dados, eles estavam tentando encontrar maneiras de armazenar, indexar e recuperar dados.
Com a emergência dos computadores, o mundo do banco de dados mudou rapidamente, tornando-o fácil, econômico a tarefa demorada para coletar e manter o banco de dados.

O primeiro Sistema Gerenciador de Banco de Dados (SGBD) comercial surgiu no final de 1960 com base nos primitivos sistemas de arquivos disponíveis na época, os quais não controlavam o acesso concorrente por vários usuários ou processos.
Os SGBDs evoluíram desses sistemas de arquivos de armazenamento em disco, criando novas estruturas de dados com o objetivo de armazenar informações.
Com o tempo, os SGBD’s passaram a utilizar diferentes formas de representação, ou modelos de dados, para descrever a estrutura das informações contidas em seus bancos de dados. Atualmente, os seguintes modelos de dados são normalmente utilizados pelos SGBD’s: modelo hierárquico, modelo em redes, modelo relacional (amplamente usado) e o modelo orientado a objetos. 

O modelo de **banco de dados relacional** foi concebido por _Edgar F. Codd_ em 1970 com o artigo '_A Relational Model of Data for Large Shared Data Banks_', que descreve o procedimento relacional para organizar dados. Esse modelo foi diferente de tudo na sua época. O modelo de Codd foi baseado em ramos da matemática como teoria de conjuntos e lógica de primeira ordem, que garantiam que os dados estivessem sendo armazenados com um mínimo de redundância. Suas ideias mudaram a maneira como as pessoas pensavam sobre bancos de dados. 

No modelo de Relacional, o esquema do banco de dados, ou organização lógica, é desconectado do armazenamento de informações físicas, e isso se tornou o princípio padrão para sistemas de banco de dados.

Antes do trabalho de Codd, a maioria dos bancos tinham seus dados organizados hierarquicamente. Esse arranjo tornava necessário iniciar uma pesquisa nas categorias gerais e, em seguida, pesquisar por meio de categorias progressivamente menores. A abordagem relacional permitia que os usuários armazenassem dados de uma maneira mais organizada e eficiente usando tabelas bidimensionais (ou como Codd os chamava de “relações”). Esta nova abordagem criou com sucesso estruturas de banco de dados que agilizaram a eficiência dos computadores.

Em 1976, enquanto trabalhava no MIT, Peter Chen publicou um artigo '_The Entity-Relationship Model-Toward a Unified View of Data_' introduzindo “modelagem de entidade / relacionamento”, mais comumente conhecido hoje como “modelagem de dados”. Esta abordagem representava estruturas de dados graficamente. O **Modelo entidade relacionamento** (ou somente modelo ER), modelo tornou possível para os engenheiros se concentrarem na aplicação de dados em vez da estrutura lógica da tabela. Dois anos depois, a Oracle anunciou o primeiro sistema de gerenciamento de banco de dados relacional (RDBMS) projetado para negócios.

> A comunidade empresarial rapidamente reconheceu as vantagens dos insights de Edgar F. Codd e Peter Chen. Os novos projetos de estrutura de dados eram notavelmente mais rápidos, mais flexíveis e mais estáveis que as estruturas de programa. Além disso, suas percepções provocaram uma mudança cultural na comunidade de programação de computadores.

### O famoso SQL - Structured Query Language

A abordagem relacional de Codd resultou na SQL (Structured Query Language), tornando-se a linguagem de consulta padrão nos anos 80. Os bancos de dados relacionais tornaram-se bastante populares e impulsionaram o mercado de bancos de dados, causando, por sua vez, uma grande perda de popularidade para modelos hierárquicos de bancos de dados.

O SQL foi desenvolvido originalmente no início dos anos 70 nos laboratórios da IBM em San Jose, dentro do projeto _System R_, que tinha por objet0ivo demonstrar a viabilidade da implementação do modelo relacional proposto por Codd. O nome original da linguagem era SEQUEL, acrônimo para "_Structured English Query Language_", vindo daí o fato de, até hoje, a sigla, em inglês, ser comumente pronunciada "síquel". 

Ela se diferencia de outras linguagens de consulta a banco de dados no sentido em que uma consulta SQL especifica a forma do resultado e não o caminho para chegar a ele. Ela é uma linguagem declarativa em oposição a outras linguagens procedurais. Isto reduz o ciclo de aprendizado daqueles que se iniciam na linguagem.

#### SQL Definido como padrão ANSI
Rapidamente surgiram vários "dialectos" desenvolvidos por outras empresas. Essa expansão levou à necessidade de ser criado e adaptado um padrão para a linguagem. Esta tarefa foi realizada pela American National Standards Institute (ANSI) em 1986 e ISO em 1987.
SQL Ansi é um padrão que é utilizado como base como construção de outras linguagens, então chamadas de _SQL-Based_


> Em meados da década de 1990, o uso da Internet promoveu um crescimento significativo na indústria de bancos de dados e na venda geral de computadores. Logo organizações e empresas descobriram que a informação em si é valiosa para a empresa. Bancos de dados arquitetonicamente projetados e Gerenciamento de Dados se tornou algo muito importante. Nos anos 90, os títulos “administrador de dados” e “administrador de banco de dados” começaram a aparecer.

***


## Modelos de Dados

Os modelos de dados (ou modelos de banco de dados) é o termo que se refere a estrutura de dados utilizada pelo banco para guardar e manter seus dados.
> De fato o modelo de dados ou estrutura de dados de um banco define  

### Modelo Hierárquico
O modelo hierárquico foi o primeiro a ser reconhecido como um modelo de dados. Seu desenvolvimento somente foi possível devido à consolidação dos discos de armazenamento endereçáveis, pois esses discos possibilitaram a exploração de sua estrutura de
endereçamento físico para viabilizar a representação hierárquica das informações.
  + Nesse modelo de dados, os dados são estruturados em hierarquias ou árvores.
    - Os nós das hierarquias contêm ocorrências de registros (por simplicidade os nós são simplesmente chamados de registros).
    - Onde cada registro é uma coleção de campos (atributos), cada campo contendo apenas uma informação.
    - O registro da hierarquia que precede a outros é o registro-pai, os outros são chamados de registros-filhos (assim como o conceito de nós filhos e pais em árvores).
  + Uma ligação é uma associação entre dois registros.
    - Por exemplo: em uma dada base de dados comercial, uma encomenda (i.e. registro) é possuída por um único cliente.
  + Cada registro possue apenas um pai.
  + O relacionamento entre um registro-pai e vários registros-filhos possui cardinalidade _1:N_.

Os dados organizados segundo este modelo podem ser acessados segundo uma seqüência hierárquica com uma navegação do topo para as folhas e da esquerda para a direita. Um registro pode estar associado a vários (tipo?) registros diferentes, desde que seja replicado.
A replicação possui duas grandes desvantagens: pode causar inconsistência de dados quando houver atualização e o desperdício de espaço é inevitável.

A ideia por trás dos modelos de bancos de dados hierárquicos é útil para um determinado tipo de armazenamento de dados, mas não é extremamente versátil. Este modelo está limitado a usos muito específicos. Por exemplo, quando cada pessoa individual de uma empresa pode se reportar a um determinado departamento, o departamento pode ser usado como um registro pai e os funcionários individuais representarão registros secundários, cada um deles vinculado a esse registro pai único em uma estrutura hierárquica.

O sistema comercial mais divulgado no modelo hierárquico foi o _Information Management System_ (IMS) da IBM. 
Grande parte das restrições e consistências de dados estava contida dentro dos programas escritos para as aplicações. Era necessário escrever programas na ordem para acessar o banco de dados.

Um diagrama de estrutura de árvore descreve o esquema de um banco de dados hierárquico. Tal diagrama consiste em dois componentes básicos: Caixas, as quais correspondem aos tipos de registros e Linhas, que correspondem às ligações entre os tipos de registros.

![Modelo Hierarquico](/BD1/imgBd/hierarchical-model.svg)

### Modelo em Rede

O modelo em redes surgiu como uma extensão ao modelo hierárquico, eliminando o conceito de hierarquia e permitindo que um mesmo registro estivesse envolvido em várias associações.

+ O modelo hierárquico, permite relações muitas para muitas _M:N_ entre registros vinculados.
    - Isso quer dizer que diferente do modelo hierarquico, um registro pode ter um ou muitos registro-pai(s).

O gerenciador Data Base Task Group (DBTG) da CODASYL (Committee on Data Systems and Languages) estabeleceu uma norma para este modelo de banco de dados, com linguagem própria para definição e manipulação de dados. Os dados tinham uma forma limitada de independência física. A única garantia era que o sistema deveria recuperar os dados para as aplicações como se eles estivessem armazenados na maneira indicada nos esquemas. Os geradores de relatórios da CODASYL também definiram sintaxes para dois aspectos chaves dos sistemas gerenciadores de dados: concorrência e segurança. O mecanismo de segurança fornecia uma facilidade na qual parte do banco de dados (ou área) pudesse ser bloqueada para prevenir acessos simultâneos, quando necessário. A sintaxe da segurança permitia que uma senha fosse associada a cada objeto descrito no esquema. Ao contrário do Modelo Hierárquico, em que qualquer acesso aos dados passa pela raiz, o modelo em rede possibilita acesso a qualquer nó da rede sem passar pela raiz. No Modelo em Rede o sistema comercial mais divulgado é o CAIDMS da Computer Associates. O diagrama para representar os conceitos do modelo em redes consiste em dois componentes básicos: Caixas, que correspondem aos registros e Linhas, que correspondem às associações.

![Modelo em Rede](/BD1/imgBd/network-model.svg)


> Estes dois modelos: Hierárquico e Rede são Orientados a Registros, isto é, qualquer acesso à base de dados – inserção, consulta, alteração ou remoção – é feito em um registro de cada vez. 

### Modelo Relacional

O modelo relacional apareceu devido às seguintes necessidades: aumentar a independência de dados nos sistemas gerenciadores de banco de dados; prover um conjunto de funções apoiadas em álgebra relacional para armazenamento e recuperação de dados; permitir processamento dedicado. 
O modelo relacional, que tem como base a teoria dos conjuntos e álgebra relacional, foi resultado de um estudo teórico realizado por Codd.

O Modelo relacional revelou-se ser o mais flexível e adequado ao solucionar os vários problemas que se colocam no nível da concepção e implementação da base de dados. 
+ A estrutura fundamental do modelo relacional é a **relação** (ou **_tabela_**).
+ Uma relação é constituída por um ou mais **atributos** (campos ou **_colunas_**) que traduzem o tipo de dados a armazenar.
+ O tipo de um atributo (coluna) é chamado de **domínio**
+ Cada instância do esquema é chamada de **tupla** (**_registro_** ou linha).

O modelo relacional não tem caminhos pré-definidos para se fazer acesso aos dados como nos modelos que o precederam. O modelo relacional implementa estruturas de dados organizadas em relações. Porém, para trabalhar com essas tabelas, algumas **restrições** precisaram ser impostas para evitar aspectos indesejáveis, como repetição de informação, incapacidade de representar parte da informação, perda ou incosistência de informação. Veremos mais sobre restrições em breve, por agora, basta entender as restrições como regras do modelo relacional que mantêm os dados consistentes e íntegros.

![Modelo Relacional](/BD1/imgBd/relational-model.svg)

### Modelo Orientado a Objetos

Os bancos de dados orientados a objeto começaram a se tornar comercialmente viáveis em meados de 1980. A motivação para seu surgimento está em função dos limites de armazenamento e representação semântica impostas no modelo relacional.
Alguns exemplos são os sistemas de informações geográficas (SIG), os sistemas CAD e CAM, que são mais facilmente construídos usando tipos complexos de dados. 
A habilidade para criar os tipos de dados necessários é uma característica das linguagens de programação orientadas a objetos. Contudo, estes sistemas necessitam guardar representações das estruturas de dados que utilizam no armazenamento permanente.

A estrutura padrão para os bancos de dados orientados a objetos foi feita pelo Object Database Management Group (ODMG). Esse grupo é formado por representantes dos principais fabricantes de banco de dados orientados a objeto disponíveis comercialmente. Membros do grupo têm o compromisso de incorporar o padrão em seus produtos.

O termo Modelo Orientado a Objetos é usado para documentar o padrão que contém a descrição geral das facilidades de um conjunto de linguagens de programação orientadas a objetos e a biblioteca de classes que pode formar a base para o Sistema de Banco de Dados.

> Quando os bancos de dados orientados a objetos foram introduzidos, algumas das falhas perceptíveis do modelo relacional pareceram ter sido solucionadas com esta tecnologia e acreditava-se que tais bancos de dados ganhariam grande parcela do mercado. Hoje, porém, acredita-se que os Bancos de Dados Orientados a Objetos serão usados em aplicações especializadas, enquanto os sistemas relacionais continuarão a sustentar os negócios tradicionais, onde as estruturas de dados baseadas em relações são suficientes.

O diagrama de classes UML serve geralmente como o esquema para o modelo de dados orientado a objetos.

![Modelo orientado a objetos](/BD1/imgBd/object-oriented-model.svg)



Existem também diversos outros modelos de banco de dados. Vale apenas pesquisar mais sobre eles também :)

***


## Sistema de Gerenciamento de Banco de Dados (SGBD)

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






