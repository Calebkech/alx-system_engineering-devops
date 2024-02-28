# Simple Web Stack

![Image of a simple web stack](0-simple_web_stack.drawio.png)

## Description

The simple web infrastructure presented here hosts a website accessible via `www.foobar.com`. Notably, there are no firewalls or SSL certificates safeguarding the server's network. Each component, including the database and application server, must share the server's CPU, RAM, and SSD resources.

## Infrastructure Specifics

- **Server Definition**: A server refers to computer hardware or software providing services to other computers, often termed as *clients*.

- **Domain Name Role**: Domain names offer human-friendly aliases for IP Addresses, simplifying recognition and recall. For instance, `www.wikipedia.org` is more intuitive than `91.198.174.192`. Domain name mapping is executed in the Domain Name System (DNS).

- **DNS Record Type for `www.foobar.com`**: `www.foobar.com` employs an **A record**. Verification can be done via `dig www.foobar.com`. Note: results may vary, but the infrastructure in this context utilizes an **A** record.
  *Address Mapping Record (A Record)*: Also known as a DNS host record, it stores a hostname and its corresponding IPv4 address.

- **Web Server Role**: The web server, whether in software or hardware form, accepts HTTP or HTTPS requests and furnishes requested content or error messages.

- **Application Server Role**: This server installs, operates, and hosts applications and associated services, facilitating the hosting and delivery of high-end consumer or business applications.

- **Database Role**: Databases maintain organized information accessible for management and updates.

- **Server-Client Communication Medium**: Communication between the server and client occurs via the internet network, utilizing the TCP/IP protocol suite.

## Infrastructure Issues

- **Single Point of Failure (SPOF)**: The infrastructure features multiple SPOFs, such as the potential downtime if the MySQL database server experiences issues, resulting in the entire site being inaccessible.

- **Downtime During Maintenance**: Maintenance tasks necessitate component shutdowns or server halts, leading to website downtime due to the single-server setup.

- **Scalability Challenges**: Scaling this infrastructure is problematic due to its reliance on a single server housing all essential components. With increased incoming traffic, resource depletion or sluggish performance becomes imminent.
