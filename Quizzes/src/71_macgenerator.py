import random

class Mac_address():
    def generate_mac_address(self, N:int):
        chars = "0123456789ABCDEF"
        address_list, mac, i = [],"", 0
        while i<N:
            for j in range(12):
                mac+=chars[random.randint(0,15)]
                if j%2==1:
                    mac+=":"
                if mac in address_list == False:
                    address_list.append(mac)
                    i+=1
                mac=""
        return address_list
    #dxfgchjvbkjhgfdghjkjhgfhjkjhg

test = Mac_address()
print(test.generate_mac_address(1))