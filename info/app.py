from direct_conn import retreat_device_info
from file_conn import retreat_file_info
import sys
import re

def is_ip_add(ip:str):
    ipv4_strc = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_strc = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    if ipv4_strc.match(ip) or ipv6_strc.match(ip):
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print("Introduzca la dirección ip del equipo donde desee comenzar con el escaneo de red")
    else:
        if is_ip_add(sys.argv[1]):
            device_add_to_inspect = []
            retreat_file_info('SW1')
            #print("Ip recivida:", sys.argv[1])
            #retreat_device_info(sys.argv[1])
            # device = {
            #     'device_type': 'cisco_ios',  # Tipo de dispositivo (por ejemplo, Cisco IOS)
            #     'ip': sys.argv[1],         # Dirección IP o nombre de host del equipo
            #     'username': 'cisco',     # Nombre de usuario
            #     'password': 'cisco',  # Contraseña
            #     'port': 22,
            # }
            # print(device['ip'])
            # device['ip'] = '192.168.20.1'
            # print(device['ip'])
        else:
            print("Por favor proporcione una dirección ip, válida")
