# Scaled Up Web Infrastructure

![Image of a scaled up web infrastructure](3-scale_up.drawio.png)

## Description

This scaled-up web infrastructure builds upon the architecture described [previously](2-secured_and_monitored_web_infrastructure.md). In this iteration, all Single Points of Failure (SPOFs) have been eliminated, and each major component (web server, application server, and database servers) has been relocated to individual GNU/Linux servers. SSL protection is not terminated at the load balancer, and each server's network is fortified with a firewall while being actively monitored.

## Specifics About This Infrastructure

- **Firewall Implementation**: A firewall has been installed between each server, enhancing security by thwarting unwanted and unauthorized access attempts across the network.

## Issues With This Infrastructure

- **High Maintenance Costs**: The decentralization of major components onto separate servers entails increased maintenance costs. Procuring additional servers escalates upfront expenses, while the expanded server infrastructure incurs elevated electricity consumption, leading to heightened operational costs. Consequently, a portion of the company's budget would need to be allocated towards server acquisition and ongoing electricity expenses to sustain the expanded infrastructure.
