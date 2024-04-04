# HTTPS SSL Configuration

This repository contains bash scripts and HAproxy configuration files for configuring HTTPS SSL termination and enforcing HTTPS traffic on your servers.

## Steps

Follow these steps to configure HTTPS SSL termination and enforce HTTPS traffic:

1. **Task 0: World wide web**: Use the `0-world_wide_web` script to display information about subdomains of a given domain. This script utilizes `dig` and `awk` to fetch DNS records for specified subdomains.

2. **Task 1: HAproxy SSL termination**: Configure HAproxy to handle encrypted traffic and serve it to backend servers. Use the `1-haproxy_ssl_termination` HAproxy configuration file to set up SSL termination. Ensure HAproxy listens on port 443 for encrypted traffic.

3. **Task 2: No loophole in your website traffic**: Configure HAproxy to automatically redirect HTTP traffic to HTTPS. Use the `100-redirect_http_to_https` HAproxy configuration file to enforce HTTPS traffic transparently and return a 301 status code.

## Requirements

- Ubuntu 16.04 LTS
- Bash scripts must be executable
- HAproxy version 1.5 or higher for SSL termination
- HAproxy must listen on port TCP 443 for encrypted traffic

## Author

This project was created by ABDELHAFID MAHMOUDI.
