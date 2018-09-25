# Camadas de protocolo e seus modelos de serviço

Até o momento a _Internet_ pode parecer um sistema extremamente complexo. Exitem muitas aplicações, protocolos, vários tipos de roteadores, enlaces, sistemas finais etc, etc. Apesar dessa complexidade, podemos organizar a arquitetura da Internet em camadas para podermo estuda-la melhor.

Cada camada quando combinada com as camadas abaixo dela implementam um serviço. Um camada contribui para o sistema ao todo da seguinte maneira:
1. Realiza uma ação própria da camada
2. Usa o serviço da camada abaixo.

Estamos interessados nos **serviços** que uma camada oferece à camada acima - a isso chamamos de **modelo de serviço** de uma camada.

. For example, the services provided by layer n may
include reliable delivery of messages from one edge of the network to the other.
This might be implemented by using an unreliable edge-to-edge message delivery
service of layer n ⫺ 1, and adding layer n functionality to detect and retransmit
lost messages.

Uma arquitetura em camada nos permite discutir e analisar uma parte bem definida e específica de um sistema maior e mais complexo. Essa característica modular das camadas é muito valiosa pois possibilita flexibilidade de implementação para o serviço provido em cada camada. Desde que cada camada forneça o mesmo serviço para a camada superior a ela e utilize os mesmos servios da camada abaixo dela, o resto da arquitetura não precisa mudar em nada, mesmo que a implementação da camada em questão mude. Mudar a implementação de um serviço é diferente de mudar o serviço em si.

A layer can be implemented in software, in hardware, or in a combination of the two. 

IMAGEM DAS CAMADAS AQUI

Application-layer protocols—such as HTTP and SMTP—are almost always implemented in software in the end systems; so are transport-layer protocols.
Because the physical layer and data link layers are responsible for handling commu-
nication over a specific link, they are typically implemented in a network interface
card (for example, Ethernet or WiFi interface cards) associated with a given link.
The network layer is often a mixed implementation of hardware and software.

When taken together, the protocols of the various layers are called the protocol stack. The Internet protocol stack consists of five layers: the physical,link, network, transport, and application layers, as shown in the Figure above.


Let's take a top-down approach, first covering the application layer and then proceeding downward.

## Application Layer

The application layer is where network applications and their application-layer protocols reside. The application layer includes many protocols, such as the HTTP protocol (which provides for Web document request and transfer), SMTP (which provides for the transfer of e-mail messages), and FTP (which provides for the transfer of files between two end systems).
We’ll see that certain network functions, such as the translation of human-friendly names for Internet end systems like www.ietf.org to a 32-bit network address, are also done with the help of a specific application-layer protocol, namely, the domain name system (DNS).

An application-layer protocol is distributed over multiple end systems, with the application in one end system using the protocol to exchange packets of information with the application in another end system. We’ll refer to this packet of information at the application layer as a **message**.

## Transport Layer

The Internet’s transport layer transports application-layer messages between application endpoints.
In the Internet there are two transport protocols, TCP and UDP, either of which can transport application-layer messages. As we've explained before, TCP provides a connection-oriented service to its applications. This service includes guaranteed delivery of application-layer messages to the destination and flow control (that is, sender/receiver speed matching). TCP also breaks long messages into shorter segments and provides a congestion-control mechanism, so that a source throttles its transmission rate when the network is congested. The UDP protocol provides a connectionless service to its applications. This is a no-frills service that provides no reliability, no flow control, and no congestion control. In this book, we’ll refer to a transport-layer packet as a **segment**.

## Network Layer

The Internet’s network layer is responsible for moving network-layer packets known as datagrams from one host to another.
The Internet transport-layer protocol (TCP or UDP) in a source host passes a transport-layer segment and a destination address to the network layer. The network layer then provides the service of delivering the segment to the transport layer in the destination host.
The network layer includes the celebrated IP Protocol, which defines the fields in the datagram as well as how the end systems and routers act on these
fields. There is only one IP protocol, and all Internet components that have a network layer must run the IP protocol.
The Internet’s network layer also contains routing protocols that determine the routes that datagrams take between sources and destinations. The Internet has many routing protocols. The Internet is a network of networks, and within a network, the network administrator
can run any routing protocol desired. Although the network layer contains both the IP protocol and numerous routing protocols, it is often simply referred to as the IP layer, reflecting the fact that IP is the glue that binds the Internet together.

# Link Layer

The Internet’s network layer routes a datagram through a series of routers between the source and destination. To move a packet from one node (host or router) to the next node in the route, the network layer relies on the services of the link layer.
In particular, at each node, the network layer passes the datagram down to the link layer, which delivers the datagram to the next node along the route.
At this next node, the link layer passes the datagram up to the network layer. The services provided by the link layer depend on the specific link-layer protocol that is employed over the link. For example, some link-layer protocols provide reliable delivery, from transmitting node, over one link, to receiving node. Note that this reliable delivery service is different from the reliable delivery service of TCP, which provides reliable delivery from one end system to another. Examples of link-layer protocols include Ethernet, WiFi, and the cable access network’s DOCSIS protocol. As datagrams typically need to traverse several links to travel from source to destination, a datagram may be handled by different link-layer protocols at different links along its route.
For example, a datagram may be handled by Ethernet on one link and by PPP on the next link. The network layer will receive a different service from each of the different link-layer protocols. We’ll refer to the link-layer packets as frames. In summary, the job of the link layer is to move entire frames from one network element to an adjacent network element.

# Physical Layer

While the job of the link layer is to move frames, the job of the physical layer is to move the individual bits within the frame from one node to the next. The protocols in this layer are again link dependent and further depend on the actual transmission medium of the link (for example, twisted-pair copper wire, single-mode fiber optics). For example, Ethernet has many physical-layer protocols: one for twisted-pair copper wire, another for coaxial cable, another for fiber, and so on. In each case, a bit is moved across the link in a different way.
