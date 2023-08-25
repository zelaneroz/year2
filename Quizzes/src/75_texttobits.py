class pizza():
    def text_to_bits(text:str):
        temp, output = "",""
        for i in text:
            i=ord(i)
            while i>0:
                temp=str(i%2)+temp
                i=i//2
            temp+=" "
            if len(temp)!=8:
                temp+="0"*(8-len(temp))
            #output+=temp[::-1] Only works in Python so always make algorithms that can work in any lang.
            output+=temp
        return output

print(pizza.text_to_bits(text="Hello"))