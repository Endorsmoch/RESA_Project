import re

def parse_cdp_entry(content:str):
    print(1)

def parse_cdp_neighbors(content:str):
    print(2)

def parse_arp(content:str):
    print(3)

def parse_int_brief(content:str):
    print(4)

def parse_version(content:str):
    if not content.strip():
        return 'La salida está vacía'

    if 'C3560' in content:
        return 'Switch'
    elif 'C2900' in content:
        return 'Router'
    else:
        return 'Tipo de equipo no reconocido'