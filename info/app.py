from netmiko import ConnectHandler
from printers import print_arp_json
from printers import write_output_to_txt
from db_connection import create_device_record
import sys
import re

def is_ip_add(ip:str):
    ipv4_strc = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_strc = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    if ipv4_strc.match(ip) or ipv6_strc.match(ip):
        return True
    else:
        return False

def set_own_ip_array(output:str):
    regex = r'(Fast|Gigabit)Ethernet\S+\s+(\S+)\s+YES\s+\S+\s+up\s+'
    matches = re.findall(regex, output)
    for match in matches:
        own_ips.append(match[1])

def set_inspectionable_devices(output:str):
    regex = r'Internet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+([0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\s+ARPA\s+(Fast|Gigabit)Ethernet'
    matches = re.findall(regex, output)
    for match in matches:
        if match[0] not in own_ips:
            neighbor_devices.append((match[0], match[1]))

def retreat_device_info(ip:str):
    ssh_client = None
    device = {
        'device_type': 'cisco_ios',  # Tipo de dispositivo (por ejemplo, Cisco IOS)
        'ip': ip,         # Dirección IP o nombre de host del equipo
        'username': 'cisco',     # Nombre de usuario
        'password': 'cisco',  # Contraseña
        'port': 22,
    }
    try:
        # Conectar al equipo utilizando Netmiko
        ssh_client = ConnectHandler(**device_json)

        # Ejecutar comandos en el dispositivo
        ip_int_brief_command = 'show ip interface brief'
        arp_command = 'show arp'
        show_version_command = 'show inventory'
        ospf_neighbor_command = 'show ip ospf neighbor'

        ip_brief_output = ssh_client.send_command(ip_int_brief_command)

        #Determinar las propias IP del equipo para no consultarlas
        set_own_ip_array(ip_brief_output)

        arp_output = ssh_client.send_command(arp_command)
        #Determinar los equipos a inspeccionar y ponerlos en un arreglo de IP vecinas. Luego de cada visita, colocarlas en un arreglo
        #con las IP ya consultadas y eliminarlo de las que hacen falta por visitar. 
        set_inspectionable_devices(arp_output)

        #A partir de aquí hasta el 'except' no tiene sentido porque pudiera volver a llamarse a la misma función para que haga la 
        #búsqueda correspondiente. Lo hice en su momento comprobando que se pudiera conectar a los equipos en "cadena".
        new_device = {
            'device_type': 'cisco_ios',  # Tipo de dispositivo (por ejemplo, Cisco IOS)
            'ip': neighbor_devices[0][0],         # Dirección IP o nombre de host del equipo
            'username': 'cisco',     # Nombre de usuario
            'password': 'cisco',  # Contraseña
            'port': 22, 
        }

        ssh_client = ConnectHandler(**new_device)
        version_output = ssh_client.send_command(show_version_command)
        print(version_output)
        
        #output = ssh_client.send_command(ospf_neighbor_command)
        #write_output_to_txt(output)
        #print_arp_json(output)

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Cerrar la conexión SSH
        if ssh_client is not None:
            ssh_client.disconnect()

if __name__ == '__main__':
    if len(sys.argv) < 2: 
        print("Introduzca la dirección ip del equipo donde desee comenzar con el escaneo de red")
    else:
        if is_ip_add(sys.argv[1]):
            device_add_to_inspect = []
            #print("Ip recivida:", sys.argv[1])
            #retreat_device_info(sys.argv[1])
            device = {
                'device_type': 'cisco_ios',  # Tipo de dispositivo (por ejemplo, Cisco IOS)
                'ip': sys.argv[1],         # Dirección IP o nombre de host del equipo
                'username': 'cisco',     # Nombre de usuario
                'password': 'cisco',  # Contraseña
                'port': 22,
            }
            print(device['ip'])
            device['ip'] = '192.168.20.1'
            print(device['ip'])
        else:
            print("Por favor proporcione una dirección ip, válida")
