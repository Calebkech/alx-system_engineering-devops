# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](2-secured_and_monitored_web_infrastructure.drawio.png)

## Description

This web infrastructure comprises three servers, ensuring security, monitoring, and encrypted traffic transmission.

## Specifics About This Infrastructure

- **Firewall Purpose**: The firewalls serve to shield the network, particularly the web servers, from unauthorized and unwanted users. Acting as intermediaries between the internal and external networks, they block incoming traffic matching specified criteria.

- **SSL Certificate Purpose**: SSL certificates encrypt traffic between the web servers and external networks, mitigating risks of man-in-the-middle attacks (MITM) and network sniffing. This encryption ensures privacy, integrity, and authenticates server identities.

- **Monitoring Clients Purpose**: Monitoring clients are instrumental in observing and analyzing server performance and network health. They track server operations, assess overall health, and promptly alert administrators to deviations from expected performance. These clients automatically test server accessibility, measure response times, and flag errors such as corrupt or missing files, security vulnerabilities, or other operational issues.

## Issues With This Infrastructure

- **SSL Termination**: Terminating SSL at the load balancer level leaves traffic between the load balancer and web servers unencrypted, potentially exposing sensitive data during internal transmission.

- **MySQL Server Scalability**: The presence of a single MySQL server poses scalability challenges and introduces a single point of failure for the entire web infrastructure.

- **Homogeneous Server Components**: All servers hosting identical components contend for resources like CPU, memory, and I/O, leading to potential performance degradation. Moreover, this setup lacks scalability and complicates troubleshooting by obscuring the source of performance issues.
