from scapy.all import sniff, IP, TCP
from .config import blocked_ips, blocked_ports

def firewall_rules(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        # Verifica se o IP de origem ou destino está bloqueado
        if ip_src in blocked_ips or ip_dst in blocked_ips:
            print(f"Pacote bloqueado de/para IP: {ip_src} <-> {ip_dst}")
            return False

        # Verifica se o pacote é TCP e se a porta de origem ou destino está bloqueada
        if packet.haslayer(TCP):
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
            if port_src in blocked_ports or port_dst in blocked_ports:
                print(f"Pacote bloqueado nas portas: {port_src} <-> {port_dst}")
                return False

        # Se o pacote não foi bloqueado, permite-o
        print(f"Pacote permitido: {ip_src} <-> {ip_dst}")
        return True

def start_firewall():
    print("Firewall ativo... (Pressione Ctrl+C para parar)")
    sniff(prn=firewall_rules, store=0)
