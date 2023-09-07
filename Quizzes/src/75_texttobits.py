class pizza():
    def text_to_bits(text:str):
        temp, binary = "",""
        for i in text:
            i=ord(i)
            while i>0:
                temp=str(i%2)+temp
                i=i//2
            if len(temp)<8:
                temp=("0"*(8-len(temp)))+temp
            #output+=temp[::-1]
            binary+=temp+" "
            temp=""
        return binary

print(pizza.text_to_bits(text="Hello World!"))