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


![Elementos Básicos da Comuicação](StudyTexts/REDES/imgRedes/01comuicacao_de_dados/elementos_basicos.jpg)


## Tipos de Transmissão

### Simplex:

A comunicação é unidirecional. O receptor só recebe e o transmissor só transmite.


### Half-Duplex:

Comunicação bidirecional, com um canal apenas. Cada dispositivo *ou **recebe** ou **transmite***. Mas não ao mesmo tempo.


### Full-Duplex:

Comunicação bidirecional. Os dispositivos podem ***enviar** e **receber*** simultaneamente.

***

## Conceito de Redes:

Conjunto de dispositivos interligados de maneira a trocarem informações e compartilharem recursos.

### *Local Area Network (LAN)*:

Interligação de dispositivos com distâncias relativamente pequenas.


### *Metropolitan Area Network (MAN)*:

Rede metropolitana qe interliga redes locais de uma região.


### *Wide Area Network (WAN)*:

Interligação de dispositivos com distância superior a região metropolitana (rede geograficamente distribuída).

***

## Estrutura da Rede

### Links:
Existem também os links de comunicação, que são definidos quando é estabelicida ou preestabelecida comunicação entre os sistemas, dentre as formas que são conectados temos:

* **Links de difusão**: Canal de comunicação que fala com inúmeros canais na rede e o envio de pacote ocorre de forma direta com o endereço porém passa por outros endereços antes de chegar a seu destino. Na transmissão por difusão, quando um host A envia uma mensagem a um host B, todos os outros hosts da rede receberão a mensagem, mas apenas o host B irá interpretá-la e respondê-la. (Numa sala você chama “Carlos venha aqui por favor”, todos vão ouvir mas só carlos vai atender)

* **Links ponto a ponto** : Na transmissão ponto a ponto, quando o host A manda a mensagem para o host B, apenas B irá recebê-la e todos os outros hosts da rede não recebem a mensagem.

### Borda da Rede:

São os sistemas finais (cliente) - ou *hosts* - que estão nas extremidades da rede. Utilizam o modelo Cliente/Servidor (fazendo requisição aos servidores), ou *peer-2-peer*.

### Núcleo da Rede:

É formado pela malha de roteadores interconectados, responsável por interligar ree entre si, formando a inter-redes ou *internet*.

***

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

O equipamento de comutação procura um caminho físico desde o dispositivo transmissor até dispositivo receptor. Esse caminho pode conter trechos de fibra óptica ou de micro-ondas, mas a ideia básica funciona: quando a conexão é estabelecida, haverá um caminho dedicado entre as extremidades até que a ligação termine. Nesse tipo de comutação, há a garantia da taxa de transmissão, e a informação de voz chegará na mesma ordem desde o transmissor até o receptor. Com a comutação de circuitos, os bits simplesmente fluem pelo fio (meio) de modo contínuo.

Uma das propriedades mais importantes na comutação de circuitos é a necessidade de **estabelecer esse caminho fim a fim antes que qualquer informação seja enviada**.

Na comutação de circuitos há também a reserva de largura de banda entre as extremidades, fazendo com que a informação percorra o mesmo caminho e chegue na mesma ordem.

Mas se houver a reserva para um circuito de um determinado usuário, e ela não for usada, (o dispositivo para de enviar dados, mesmo que momentâneamente, por exemplo), a largura de banda desse circuito será desperdiçada. A reserva exclusiva de largura de banda para o circuito faz o sistema ineficiente, porque dificilmente os dispositivos trocam informações durante 100% do tempo em que ficam conectados. Sempre haverá tempos ociosos que não podem ser aproveitados, e a largura de banda só será liberada para outros fins quando um dos terminais encerrar a comunicação.

A comutação de circuito dedicado pode ter dois tipos de multiplexação:

#### Frequency-Division Multiplexing (***FDM***):

    - Reserva de uma banda de frequência para cada conexão.
    - Cada circuito dispõe continuamente de um fração da largura de banda
    
    > A transmissão de rádio AM ilustra a FDM. O espectro alocado é de cerca de 1 MHz, aproximadamente 500 a 1500 kHz. Diferentes frequências são alocadas a diferentes canais lógicos (estações), cada um operando em uma parte do espectro, com a separação entre canais grande o bastante para impedir interferência.


    
#### Time-Division Multiplexing (***TDM***):
    - Tempo dividido em quadros de duração física.
    - Cada quadro é dividio em números fixos de compartilhamentos (chamados slots).
    - Cada circuito dispõem de toda a largura de banda durante um breve intervalo de tempo.
    - Os usuários se alternam (em um padrão de rodízio).
    
    > A TDM é bastante usada como parte das redes de telefone e celular. Para evitar um ponto de confusão, vamos esclarecer que isso é muito diferente da multiplexação estatística por divisão de tempo, ou STDM (Statistical Time Division Multiplexing).
    
  ### Comutação de Pacotes:
  
Esse procedimento é diferente da comutação de circuitos, em que o resultado do estabelecimento da conexão dedicada e a reserva de largura de banda desde o transmissor até o receptor. Com essa tecnologia, os pacotes são enviados assim que estão disponíveis. Não é preciso estabelecer um caminho dedicado com antecedência.
  
  > Transmissão store-and-foward: se baseia no sistema postal. Cada mensagem (carta) carrega o endereço de destino completo e cada uma delas é roteada pelos nós intermediários através do sistema, independentemente de todas as outras. Existem diferentes nomes para mensagens em diferentes contextos; um pacote é uma mensagem na camada de rede. Quando os nós intermediários recebem uma mensagem completa antes de enviá-la para o próximo nó, isso é chamado transmissão store-and-forward. O atraso de acumular um pacote na memória do roteador antes que ele seja enviado para o próximo roteador excede o da comutação de circuitos.
  
Fica a critério dos roteadores usar a transmissão ***_store-and-forward_*** para enviar cada pacote em seu caminho ao destino por conta própria. Todos os dados no circuito seguem esse caminho. Fazer todos os pacotes seguirem o mesmo caminho significa que eles não poderão chegar fora de ordem. Porém, com a comutação de pacotes, não há nenhum caminho fixo e, assim,
diferentes pacotes podem seguir caminhos distintos, dependendo das condições da rede no momento em que eles são enviados. Portanto, eles podem chegar fora de ordem.

As redes de comutação de pacotes impõem um limite superior sobre o tamanho dos pacotes. Isso garante que nenhum usuário poderá monopolizar qualquer linha de transmissão por muito tempo. Isso também reduz o atraso, pois o primeiro pacote de uma mensagem longa pode ser encaminhado antes que o segundo tenha chegado por completo. 
   
Se muitos pacotes forem enviados ao mesmo tempo, isso gera atraso de enfileiramento e o congestionamento. Por outro
lado, não existe perigo de obter um sinal de ocupado e não conseguir usar a rede.


#### Multiplexação Estatística (STDM):

Multiplexação estatística é o modelo predominante de transporte de pacotes na internet. Ele difere da multiplexação por divisão temporal (TDM) e da multiplexação por divisão de frequência (FDM).

Cada roteador possue multiplos links conectados a ele. Para cada link de saída, o roteador possue um _buffer de saída_ (também chamada de _fila de saída_), que armazena os pacotes que o roteador está pronto para enviar naquele link. O buffer de saída tem um grande importância para a comutação de pacotes.

Se um pacote que acabou de chegar no roteador precisa ser transmitido em um link de saída porém este link está ocupado transmitindo outro pacote, o pacote que acabou de chegar irá esperar no buffer de saída.

Por isso, além dos atrasos de entrada _store-and-forward_ os pacotes sofrem atrasos no buffer de saída. Esses atrasos variam dependendo do nível de congestionamento da rede.

Como o tamanho do buffer é finito, um pacote novo pode encontrar a fila completamente cheia com outros pacotes esperando para serem enviados. Neste caso, ocorre perda de pacote - o pacote mais recente ou algum da fila é descartado. 
