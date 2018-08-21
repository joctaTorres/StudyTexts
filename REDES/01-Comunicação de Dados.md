# Teoria da Comunicação de Dados:

## Elementos Básicos da Comunicação:

1. Mensagem
    - Informação sendo transmitida.
2. Transmissor
    - Dispositivo que eniva a mensagem.
3. Meio
    - Caminho físico onde trafega a mensagem.
4. Receptor
    - Dispositivo que recebe a mensagem.
5. Protocolo
    - Regras da Comunicação

## Tipos de Transmissão

### Simplex:

A comunicação é unidirecional. O receptor sórecebe e o transmissor só transmite.

### Half-Duplex:

Comunicação bidirecional, com um canal apenas. Cada dispositivo *ou **recebe** ou **transmite***. Mas não ao mesmo tempo.

### Full-Duplex:

Comunicação bidirecional. Os dispositivos podem ***enviar** e **receber*** simultaneamente.

## Conceito de Redes:

Conjunto de dispositivos interligados de maneira a trocarem informações e compartilharem recursos.

### *Local Area Network (LAN)*:

Interligação de dispositivos com distâncias relativamente pequenas.

### *Metropolitan Area Network (MAN)*:

Rede metropolitana qe interliga redes locais de uma região.

### *Wide Area Network (WAN)*:

Interligação de dispositivos com distância superior a região metropolitana (rede geograficamente distribuída).

## Estrutura da Rede


### Borda da Rede:

São os sistemas finais (cliente) - ou *hosts* - que estão nas extremidades da rede. Utilizam o modelo Cliente/Servidor (fazendo requisição aos servidores), ou *peer-2-peer*.

### Núcleo da Rede:

É formado pela malha de roteadores interconectados, responsável por interligar ree entre si, formando a inter-redes ou *internet*.

## Abordagens à Transmissão de Dados na Rede

####  Conceito elementar - O que é Comutação:

Um processo de comutação é aquele que reserva e libera recursos de uma rede para sua utilização:

> A função da comutação em uma rede de comunicação se refere à alocação dos recursos da rede para possibilitar a transmissão de dados pelos diversos dispositivos conectados.


Nos primórdios da telefonia, por exemplo, a conexão para uma ligação telefônica era feita pelo telefonista que conectava um cabo aos soquetes de entrada e saída em um painel manualmente. Porém hoje esse processo é automatizado pelo equipamento de comutação.

#### Conceito elementar - O que é Multiplexação:

Multiplexação é uma técnica utilizada para permitir que mais de uma mensagem ocupe o mesmo meio de transporte. Ela é usada tanto em redes de computadores, em linhas telefônicas e no envio de telegramas. Se não fosse por esta técnica, as redes seriam coisas muito mais caras e possivelmente tecnologias como os aparelhos de telefones e celulares nunca teriam se popularizado.

O desenvolvimento de técnicas de multiplexação foi um dos principais fatores que levaram ao barateamento dos celulares nos últimos anos.

A grande vantagem da multiplexação é permitir que muitos nós se comuniquem simultaneamente pelo mesmo meio. A desvantagem é que é preciso posteriormente filtrar os sinais enviados para conseguir identificar a mensagem de cada usuário. O aparelho ou programa que realiza a multiplexação chama-se multiplexador. O aparelho ou programa que faz a filtragem das informações enviadas chama-se demultiplexador.

### Existem duas abordagens para a transferência de dados:

1. Comutação de Circuito.
    - Taxa constante de transmissão.
    - Usa um canal dedicado para cada conexão. Não há compartilhamento de recursos.
    - Há estabelecimento de recursos fim-a-fim
    - Recursos fim-a-fim são reservados por "chamada".
2. Comutação de Pacotes.
    - Dados enviados em blocos.
    - Fluxo de dados fim-a-fim é dividido em pacotes.
    - Há compartilhamento de recursos.
    - Há demanda por recursos

### Comutação por Circuito:

O equipamento de comutação procura um caminho físico desde o dispositivo transmissor até dispositivo receptor. Esse caminho pode conter trechos de fibra óptica ou de micro-ondas, mas a ideia básica funciona: quando a conexão é estabelecida, haverá um caminho dedicado entre as extremidades até que a ligação termine. Nesse tipo de comutação, há a garantia da taxa de transmissão, e a informação de voz chegará na mesma ordem desde o transmissor até o receptor.

Uma das propriedades mais importantes na comutação de circuitos é a necessidade de **estabelecer esse caminho fim a fim antes que qualquer informação seja enviada**.

Na comutação de circuitos há também a reserva de largura de banda entre as extremidades, fazendo com que a informação percorra o mesmo caminho e chegue na mesma ordem.

Mas se houver a reserva para um circuito de um determinado usuário, e ela não for usada, (o dispositivo para de enviar dados, mesmo que momentâneamente, por exemplo), a largura de banda desse circuito será desperdiçada. A reserva exclusiva de largura de banda para o circuito faz o sistema ineficiente, porque dificilmente os dispositivos trocam informações durante 100% do tempo em que ficam conectados. Sempre haverá tempos ociosos que não podem ser aproveitados, e a largura de banda só será liberada para outros fins quando um dos terminais encerrar a comunicação.

A comutação de circuito dedicado pode ser composto por:
...