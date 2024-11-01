PyGuard: Firewall em Python
PyGuard é um firewall básico desenvolvido em Python que permite a filtragem de pacotes IP com base em IPs e portas bloqueadas. Este projeto utiliza a biblioteca scapy para capturar e processar pacotes de rede, proporcionando uma camada adicional de segurança através da configuração de regras personalizadas.

Recursos
Filtragem de pacotes baseada em IPs e portas bloqueadas
Monitoração e bloqueio em tempo real de pacotes indesejados
Logs de atividades de bloqueio e permissões para auditoria
Pré-requisitos
Python 3.x
Biblioteca scapy
Instale a biblioteca scapy com:

bash
Copiar código
pip install scapy
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seuusuario/pyguard-firewall.git
cd pyguard-firewall
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Estrutura do Projeto
arduino
Copiar código
pyguard-firewall/
├── main.py                # Ponto de entrada do projeto
├── firewall/
│   ├── __init__.py        # Inicializador do pacote
│   ├── app.py             # Lógica principal do firewall
│   └── config.py          # Configurações de IPs e portas bloqueadas
└── requirements.txt       # Dependências do projeto
main.py: Inicia o firewall.
firewall/app.py: Contém as regras do firewall e lógica de captura de pacotes.
firewall/config.py: Define os IPs e portas bloqueadas.
Como Usar
Abra um terminal e navegue até a pasta do projeto.

Execute o comando:

bash
Copiar código
python main.py
Isso iniciará o firewall. Ele irá monitorar o tráfego de rede e bloquear pacotes com base nas regras definidas.

Configuração
No arquivo firewall/config.py, você pode configurar os IPs e portas que deseja bloquear:

python
Copiar código
# Configurações de IPs e portas bloqueadas
blocked_ips = ["192.168.1.10", "10.0.0.5"]
blocked_ports = [80, 443]
