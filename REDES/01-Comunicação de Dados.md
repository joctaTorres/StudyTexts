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


![Elementos Básicos da Comuicação](https://raw.githubusercontent.com/joctaTorres/StudyTexts/jocta/redes/REDES/imgRedes/01comuicacao_de_dados/elementos_basicos.jpg?token=AagbtAGTpZ6Wl4ZK7xCx7Kr5G1XXFNdJks5bsOc4wA%3D%3D)


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

Cada roteador (_switch_) possue multiplos links conectados a ele. Para cada link de saída, o roteador possue um _buffer de saída_ (também chamada de _fila de saída_), que armazena os pacotes que o roteador está pronto para enviar naquele link. O buffer de saída tem um grande importância para a comutação de pacotes.

Se um pacote que acabou de chegar no roteador precisa ser transmitido em um link de saída porém este link está ocupado transmitindo outro pacote, o pacote que acabou de chegar irá esperar no buffer de saída.

Por isso, além dos atrasos de entrada _store-and-forward_ os pacotes sofrem atrasos no buffer de saída. Esses atrasos variam dependendo do nível de congestionamento da rede.

Como o tamanho do buffer é finito, um pacote novo pode encontrar a fila completamente cheia com outros pacotes esperando para serem enviados. Neste caso, ocorre perda de pacote - o pacote mais recente ou algum da fila é descartado. 

#### Um pouco sobre IP, camadas de rede, de transporte, datagramas e transmissão de pacotes fim-a-fim:

Em breve estudaremos as diferentes camadas da rede. Porém, podemos adiantar um pouco do que vamos ver sobre esse tópico para falarmos sobre os pacotes e como eles são transmitidos fim a fim (e de quebra aprendemos alguns conceitos fundamentais).

Cada camada da rede possue uma unidade de dado - PDU - específica.

> Protocol Data Unit ou em Português Unidade de Dados de Protocolo em telecomunicações descreve um bloco de dados que é transmitido entre duas instâncias da mesma camada. Cada camada recebe a PDU da camada superior como um bloco de dados, adiciona seus cabeçalhos (e em alguns casos, rodapés) de controle, criando a sua própria PDU, num processo chamado de encapsulamento.


**Vamos começar entendendo o IP e o datagrama:**

Quando falamos IP e Datagrama, estamos descrevendo a **camada de rede**, que é a camada responsável pelo encaminhamento de pacotes, incluindo o roteamento através de roteadores intermediários até os sistemas finais destinatários.

+ **Internet Protocol (IP)**: O protocolo de Internet IP - é o principal protocolo de comunicação usado para envio de pacotes pela internet. O IP tem a tarefa de entregar pacotes de host a host (fim-a-fim) baseado em um endereço IP e em rótulos com algumas informações no cabeçalho do pacotes. Para isso, o esse protocolo estabeleçe um estrutura de pacote que encapsula o dado que deve ser transmitido.

> O _Internet Protocol_ é responsável pelo endereçamento de sistemas finais, encapsulamento de pacotes (em o que chamamos de datagrama) e roteamento desses datagramas do sistema-final transmissor até o sistema-final receptor através de uma ou mais redes de IP. Por isso, e com essa finalidade, esse protocolo define um formato de pacote e provê o sistema de endereçamento.

Um Datagrama é "uma entidade de dados completa e independente que contém informações suficientes para ser roteada da origem ao destino sem precisar confiar em trocas anteriores entre essa fonte, a máquina de destino e a rede de transporte". Um datagrama é uma unidade de transferência básica associada a uma rede de comutação de pacotes.

Cada datagrama possue cabeçalho e carga. O cabeçalho IP inclue dados como endereço IP fonte e endereço IP de destino entre outros metadados necessários para roteamento e entrega do datagrama. Já a carga, é efetivamente o dado a ser transmitido. Esse método de aninhar o pacote com um cabeçalho é o que chamamos de encapsulamento. 

> O termo datagrama é tido como sinonimo de pacote. Porém o termo datagrama é comumente reservado para pacotes utilizados por serviços de transporte não confiável, que não conseguem notificar o remetente se a transmissão falhou. Enquanto o termo pacote é usado para qualquer pacote utilizando ou não um serviço de transporte seguro.


Agora que sabemos sobre a camada de rede e datagramas, vamos entender a **camada de transporte**:

A **camada de transporte** provê uma comunicação lógica entre os hosts. A camada de transporte funciona acima da camada de rede para estabelecer um conexão entre os hosts. Para fazer isso, os pacote saem do host remetente em segmentos que passam pela camada de redes (como datagramas) até o destino. O sistema final destinatário então, finalmente remonta os segmentos na mensagem.

Entenda que a **camada de rede** apenas entrega um datagrama de um host a outro, já a camada de transporte utiliza a tecnologia da camada de rede para ligar o hosts processo a processo, ou seja, ampliando o serviço provido pela camada de redes. Para isso a camada de transporte utiliza o conceito de portas (que falaremos em breve).

> Então, para resumir, os protocolos da camada de transporte, fornecem comunicação/conexão sobre - através - de uma camada de rede subjacente.

Existem vários protocolos que podem ser utilizados pela camada de transporte, mas De maneira geral, os protocolos da camada de transporte oferecem serviços  **orientado a conexão** e serviços **não orientado a conexão**:

> Podemos resumir:
> - O serviço orientado a conexão garante que os dados sejam entregues aos destinatários em ordem e completos.
> - O serviço não orientado a conexão não garante essa entrega.
 
 
Os dois principais **protocolos da camada de transporte** são:

**Protocolo UDP - Não Orientado a Conexão:**  A ideia central do protocolo é receber os dados de um processo e entregar ao processo de destino. Não leva em consideração o congestionamento da rede, ou uma entrega confiável dos dados. Neste tipo serviço não existe apresentação entre os sistemas finais. Quando um dos lados de uma aplicação quer enviar pacotes ao outro, ela simplesmente os envia. Como não há apresentação os pacotes podem ser remetidos mais rapidamente, mais também não há confirmações de entrega. A grande vantagem do UDP em relação ao TCP (outro protocolo da camada de transporte) está na velocidade de transmissão, relevando a confiabilidade na entrega dos pacotes. Nas aplicações onde velocidade é mais importante do que a ordem em que os pacotes são recebidos, como jogos, vídeos e músicas, o UDP é preferível.

**Protocolo TCP - Serviço Orientado a Conexão:** O protocolo TCP é outro protocolo utilizado pela camada de transporte. A idéia central deste protocolo é prover confiabilidade no transporte dos dados, não deixando de lado o tráfego na rede (controle de congestionamento). A grande vantagem do TCP em relação ao UDP está na confiabilidade em que os dados são entregues ao remetente. Este protocolo provê mecanismos que garantem que todos os dados repassados a camada de aplicação não estão corrompidos. Desta forma um host A pode enviar um arquivo ao host B tendo a certeza de que o arquivo, caso seja entregue á camada de aplicação do host B, está íntegro. O cliente e o servidor (que residem em diferentes sistemas finais) enviam pacotes de controle um para o outro antes de transmitirem os dados reais. Esse procedimento de apresentação alerta o cliente e o servidor, fazendo com que eles se preparem para um "rajada" de pacotes.
Uma vez que o procedimento de apresentação tenha terminado, diz – se que uma conexão foi estabelecida entre os dois sistemas finais. Mais os dois sistemas finais estão conectados de maneira muito tênue, por isso a terminologia ‘Orientado a Conexão’.

> Note que o Serviço Orientado a Conexão é implementado na camada de transporte na borda da rede, nos sistemas finais. Apenas os sistemas finais ficam cientes dessa conexão, os comutadores de pacotes ficam completamente alheio a ela. Os comutadores de pacotes não armazenam nenhum dado ou informação a respeito da comunicação.

Por isso, se diz que o TCP é orientado a conexão, isto é, um host estabelece uma conexão com outro host, de forma que um pode enviar dados para o outro em modo full duplex. O TCP, portanto, provê transferência confiável de dados entre processos rodando em sistemas finais. A comunicação entre os dois aplicativos se dá como se eles estivessem fisicamente interligados por um cabo, embora ambos possam estar a milhares de quilômetro de distância um do outro.

    Resumindo:

    1. Os pacotes que tanto falamos acima recebem o nome de datagrama na **camada de rede**. Os datagramas têm as informações para transmitir pacotes de um host a outro.

    2. Os protocolos da camada de transporte (TCP ou UDP) do host transmissor passam um segmento e um endereço de destino para a camada de rede (como você passa uma carta para o serviço postal com um endereço de destino). A camada de rede, então provê o serviço de entrega do pacote (que ela enxerga como datagrama) para o a camada de transporte do host receptor.


***

#### Circuitos Virtuais e Redes de datagrama

Como já sabemos, a _camada de **transporte**_ pode fornecer serviços **orientado _ou_ não orientado à conexão** entre dois _processos_ em máquinas diferentes atráves da rede. 

De maneira similar, a _camada de **rede**_ pode oferecer serviços **orientado _ou_ não orientado à conexão** entre dois sistemas finais. Os serviços **orientado _e_ não orientado à conexão** oferecidos pela _camada de **rede**_ são, em alguns aspectos, análogos aos serviços oferecidos pela _camada de **transporte**_, por exemplo:
- O serviço orientado à conexão da camada de rede começa com um _handshake_ entre os os host
- O serviço não orientado à conexão da camada de rede não possue nenhum procedimento preliminar entre os os host.
Apesar dessas similaridades, existem diferenças:
- Esses serviços são host-a-host providos pela _camada de rede_ para a _camada de transporte_.
    - Enquanto os serviços da camada de transporte são processo-a-processo.
- As implementações do serviço orientado a conexões na camada de transporte e na camada de rede são diferentes.
    - O serviço orientado à conexão da camada de transporte é implementado na borda da rede, nos sistemas finais; o serviço de conexão da camada de rede é implementado nos roteadores do núcleo da rede, bem como nos sistemas finais.

Em todas as principais arquiteturas de redes de computadores até hoje (Internet, ATM, frame relay, etc), a _camada de rede_ provê serviço orientado à conexão host-a-host **_ou_**  serviço não orientado à conexão host-a-host, mas não ambos.

Redes de computadores que fornecem apenas serviço orientado a conexão na camada de rede são chamadas _virtual-circuit (VC) networks_ ou **Redes de circuitos virtuais**. Já as redes que fornecem apenas serviço não orientado a conexão
na camada de rede são chamados de **redes de datagrama**

As redes de circuito virtual e de datagrama são duas classes fundamentais de redes de computadores. Eles usam informações muito diferentes ao tomar suas decisões de encaminhamento.
