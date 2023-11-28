import json

def print_arp_json(table):
    lines = table.strip().split('\n')
    arp_entries = []

    for row in lines[1:]:
        values = row.split()
        if len(values) == 6:  # Asegúrate de que haya suficientes columnas para evitar errores
            arp_entry = {
                "Protocol": values[0],
                "Address": values[1],
                "Age (min)": values[2],
                "Hardware Addr": values[3],
                "Type": values[4],
                "Interface": values[5]
            }
            arp_entries.append(arp_entry)

    arp_table_json = {"arp_table": arp_entries}

    with open("/files/arp_table.json", "w") as json_file:
        json.dump(arp_table_json, json_file, indent=4)


def print_ospf_neighbor_json(table):
    return

def write_output_to_txt(output):
    with open("/files/ospf_neighbor_output.txt", "w") as file:
        file.write(output)