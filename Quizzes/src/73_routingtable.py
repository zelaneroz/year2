def check_mac(mac_add:str):
    if len(mac_add)==17:
        return True

#if mac in routing_table, output the ip
#if mac not in routing_table, create new ip and output it.
#make sure new ip is not in existing ip

def routing_table_manager(mac_add:str):
    table={} #[[mac,ip],[mac,ip]]
    if check_mac(mac_add):
       if mac_add.


