import random
class ipv6():
    def ipv6machine(N:int):
        hex, ip,temp,final,i="0123456789ABCDEF","","",[],0
        while i<N:
            for j in range(4):
                for k in range(4):
                    temp+=hex[random.randint(0,15)]
                    if k==3:
                        temp+=":"
                    ip+=temp
                    temp=""
            i+=1

            if ip not in final:
                final.append(ip)
            else:
                i-=1
        return final

print(ipv6.ipv6machine(3))