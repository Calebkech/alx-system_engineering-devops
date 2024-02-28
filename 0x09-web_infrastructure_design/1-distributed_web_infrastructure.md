# Distributed Web Infrastructure

![Image of a distributed web infrastructure](1-distributed_web_infrastructure.drawio.png)

## Description

This distributed web infrastructure aims to alleviate traffic on the primary server by distributing a portion of the load to a replica server, facilitated by a load balancer responsible for balancing the workload between the primary and replica servers.

## Infrastructure Specifics

- **Load Balancer Distribution Algorithm**: The HAProxy load balancer is configured with the *Round Robin* distribution algorithm. This algorithm cycles through each server behind the load balancer based on their weights, ensuring a balanced distribution of processing time. It offers flexibility with dynamic adjustment of server weights.
  
- **Load-Balancer Enabled Setup**: The HAProxy load balancer implements an *Active-Passive* setup. Unlike an *Active-Active* setup which evenly distributes workloads across all nodes, an *Active-Passive* setup designates certain nodes as passive or on standby. The load balancer directs traffic primarily to the active node, with passive nodes ready to take over if the active node fails.

- **Database Primary-Replica Cluster Operation**: In a *Primary-Replica* (*Master-Slave*) cluster setup, one server serves as the *Primary* and another as the *Replica*. The *Primary* handles both read and write requests, while the *Replica* only manages read requests. Data synchronization occurs whenever the *Primary* executes a write operation.

- **Application Node Distinctic
