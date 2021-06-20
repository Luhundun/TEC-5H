import binascii
import re


# 元组[1]需要reserve
asmhub = [ ('00' ,'01001000000000000000000000000000') ,('01' ,'00000110000000000100000000000011') ,
           ('02' ,'00000011000001000111000000000001') ,('03' ,'00000010110000000000000000000000') ,
           ('04' ,'00000101000000000100000000000011') ,('05' ,'00000100110001000000000000000000') ,
           ('06' ,'00000111000010000000000000000001') ,('07' ,'00000001000001000101001000000000') ,
           ('08' ,'00001111001000000100000000000000') ,('09' ,'00000100100001000100000000000000') ,
           ('0A' ,'00000010100000000100000000000000') ,('0B' ,'00011101100001000100000000000000') ,
           ('0C' ,'00000001100001000100000000000000') ,('0D' ,'00001110000011000000000000000001') ,
           ('0E' ,'00011101000001000100010000000000') ,('0F' ,'10010000000010001000000000000000') ,
           ('10' ,'00100000000000000000001100000000') ,('11' ,'00100001000000000000001100000000') ,
           ('12' ,'00100010000000000000001100000000') ,('13' ,'00100011100000000101000100000000') ,
           ('14' ,'00100100100000000101000000000000') ,('15' ,'11001111001100000000000000000000') ,
           ('16' ,'00100110001100001011010000000000') ,('17' ,'00001111001101000101000000000000') ,
           ('18' ,'00101000001110001000000000000000') ,('19' ,'00101001001110001000000000000000') ,
           ('1A' ,'00000000000000000000000000000000') ,('1B' ,'00000000000000000000000000000000') ,
           ('1C' ,'00000000000000000000000000000000') ,('1D' ,'00001101000000000100000000000011') ,
           ('1E' ,'00001111001101000000000000000000') ,('1F' ,'00001111001000000101000000000000') ,
           ('20' ,'00001111001100000110010010010000') ,('21' ,'00001111001100000110010001100100') ,
           ('22' ,'00001111001100000110010010111000') ,('23' ,'00001111001100000110000000000011') ,
           ('24' ,'00001111001100000111010000000001') ,('25' ,'00000000000000000000000000000000') ,
           ('26' ,'00001111001100000000000000000000') ,('27' ,'00000000000000000000000000000000') ,
           ('28' ,'00111000000000100110000100000000') ,('29' ,'00111000000000010110000100000000') ,
           ('2A' ,'00000000000000000000000000000000') ,('2B' ,'00000000000000000000000000000000') ,
           ('2C' ,'00000000000000000000000000000000') ,('2D' ,'00000000000000000000000000000000') ,
           ('2E' ,'00000000000000000000000000000000') ,('38' ,'00001111001100000010010000000000') ]
asmdict={}


def makehub():      #提取asm中的代码，格式不同可能导致此函数出错
    with open("CM0.asm") as f1:
        list1 = f1.read()
        list1_key=re.findall(r"(\S+)H",list1)
        list1_value=re.findall(r"(\d\d+)B",list1)
        for key,value in zip(list1_key,list1_value):
            if key not in asmdict:
                asmdict[key]=value
        f1.close()
    with open("CM1.asm") as f2:
        list2 = f2.read()
        list2_key=re.findall(r"(\S+)H",list2)
        list2_value=re.findall(r"(\d\d+)B",list2)
        for key,value in zip(list2_key,list2_value):
            if key in asmdict:
                asmdict[key]+=value
        f2.close()
    with open("CM2.asm") as f3:
        list3 = f3.read()
        list3_key=re.findall(r"(\S+)H",list3)
        list3_value=re.findall(r"(\d\d+)B",list3)
        for key,value in zip(list3_key,list3_value):
            if key in asmdict:
                asmdict[key]+=value
        f3.close()
    with open("CM3.asm") as f4:
        list4 = f4.read()
        list4_key=re.findall(r"(\S+)H",list4)
        list4_value=re.findall(r"(\d\d+)B",list4)
        for key,value in zip(list4_key,list4_value):
            if key in asmdict:
                asmdict[key]+=value
        f4.close()
    for i in range(0,47):
        stri = str('{:02X}'.format(i))
        if stri not in asmdict:
            asmdict[stri] ='0'*32
    asmhub=sorted(asmdict.items())
    print(asmhub)

def makehex():
    #for asm in asmhub:
    with open("0.hex",'w') as t:
        for asm in asmhub:
            check = 1 + list(bytearray.fromhex(asm[0]))[0]+int('0b'+asm[1][0:8],2)
            dd = 0x100-check%0x100
            hexline = ":0100"+asm[0]+"00"+str('{:02X}'.format(int('0b'+asm[1][0:8],2)))+str('{:02X}'.format(dd))
            t.writelines(hexline)
            t.writelines('\n')
        t.writelines(":00000001FF\n")
        t.close()
    with open("8.hex",'w') as t:
        for asm in asmhub:
            check = 1 + list(bytearray.fromhex(asm[0]))[0]+int('0b'+asm[1][8:16],2)
            dd = 0x100-check%0x100
            hexline = ":0100"+asm[0]+"00"+str('{:02X}'.format(int('0b'+asm[1][8:16],2)))+str('{:02X}'.format(dd))
            t.writelines(hexline)
            t.writelines('\n')
        t.writelines(":00000001FF\n")
        t.close()
    with open("16.hex",'w') as t:
        for asm in asmhub:
            check = 1 + list(bytearray.fromhex(asm[0]))[0]+int('0b'+asm[1][16:24],2)
            dd = 0x100-check%0x100
            hexline = ":0100"+asm[0]+"00"+str('{:02X}'.format(int('0b'+asm[1][16:24],2)))+str('{:02X}'.format(dd))
            t.writelines(hexline)
            t.writelines('\n')
        t.writelines(":00000001FF\n")
        t.close()
    with open("24.hex",'w') as t:
        for asm in asmhub:
            check = 1 + list(bytearray.fromhex(asm[0]))[0]+int('0b'+asm[1][24:32],2)
            dd = 0x100-check%0x100
            hexline = ":0100"+asm[0]+"00"+str('{:02X}'.format(int('0b'+asm[1][24:32],2)))+str('{:02X}'.format(dd))
            t.writelines(hexline)
            t.writelines('\n')
        t.writelines(":00000001FF\n")
        t.close()
    pass

if __name__ =="__main__":

    makehub()
    makehex()