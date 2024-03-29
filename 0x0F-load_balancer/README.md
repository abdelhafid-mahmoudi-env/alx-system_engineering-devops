# Project: 0x0F Load Balancer

**0x0F. Load balancer**
- **DevOps**
- **SysAdmin**
- **Weight: 1**
- Project will start Mar 28, 2024 4:00 AM, must end by Apr 2, 2024 5:00 AM
- Checker will be released at Mar 29, 2024 10:00 AM
- An auto review will be launched at the deadline

## Background Context
In this project, we aim to improve our web stack by introducing redundancy for our web servers. This ensures our infrastructure is more reliable and capable of handling increased traffic. Specifically, we will double the number of web servers and set up a load balancer to distribute traffic efficiently.

You have been given 2 additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

## Tasks

### 0. Double the number of webservers (mandatory)
Configure `web-02` to be identical to `web-01` using Bash scripts. Add a custom Nginx response header (`X-Served-By`) to track which web server handles HTTP requests.

Requirements:
- Configure Nginx to include a custom header on `web-01` and `web-02`.
- The custom HTTP header must be `X-Served-By`.
- The value of the custom HTTP header must be the hostname of the server Nginx is running on.
- Write `0-custom_http_response_header` to configure a new Ubuntu machine accordingly.

### 1. Install your load balancer (mandatory)
Install and configure HAproxy on `lb-01` server to distribute traffic to `web-01` and `web-02` using a round-robin algorithm.

Requirements:
- Configure HAproxy to send traffic to `web-01` and `web-02`.
- Distribute requests using a round-robin algorithm.
- Ensure HAproxy can be managed via an init script.
- Ensure servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.

## Resources
Read or watch:
- Introduction to load-balancing and HAproxy
- HTTP header
- Debian/Ubuntu HAProxy packages

## General Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A README.md file at the root of the folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing

## Repo Information
- GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- Directory: 0x0F-load_balancer
- File: 0-custom_http_response_header, 1-install_load_balancer

## Copyright
Copyright © 2024 ALX. All rights reserved.
