from file_reader import read_file
from content_parser import *

def retreat_file_info(device_id: str):
    folder_name = 'InfoDevices/'
    show_arp = device_id+'_show_arp.txt'
    show_cdp_entry = device_id+'_show_cdp_entry.txt'
    show_cdp_neighbors = device_id+'_show_cdp_neighbors.txt'
    show_ip_int_brief = device_id+'_show_ip_int_brief.txt'
    show_version = device_id+'_show_version.txt'
    
    arp = read_file(folder_name+show_arp)
    cdp_entry = read_file(folder_name+show_cdp_entry)
    cdp_neighbors = read_file(folder_name+show_cdp_neighbors)
    int_brief = read_file(folder_name+show_ip_int_brief)
    version = read_file(folder_name+show_version)

    parse_arp(arp)
    neighbors = parse_cdp_entry(cdp_entry)
    parse_cdp_neighbors(cdp_neighbors)
    parse_int_brief(int_brief)
    device_type = parse_version(version)
    


