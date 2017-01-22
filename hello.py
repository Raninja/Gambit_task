
import binascii
import struct

def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def main():

    #Read the registers and put them into a dict
    lines = open('input.txt','rt').readlines()
    register_dict = {int(l.split(':')[0]): int(l.split(':')[1]) for l in lines[1:]}
   
   
    input_list = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),(35,36),(37,38),(39,40),(41,42),(43,44),(45,46),(47,48),(49,50),(51,),(53,55),(56,),(59,),(60,),(61,),(62,),(72,),(77,78),(79,80),(81,82),(83,84),(85,86),(87,88),(89,90),(92,),(93,),(94,),(96,),(97,98),(99,100)]

    #register_ops = {}

    #Thanks, http://stackoverflow.com/questions/24289180/how-to-convert-a-hex-string-into-an-unpacked-ieee-754-format-number !
    
    def two_registers_into_float(register_1, register_2):

        #registers into hex strings
        hex_1 = hex(int(register_2))[2:]
        hex_2 = hex(int(register_1))[2:]
        #print(hex_1)
        #String concat
        the_hex = hex_1 + hex_2
        #Unpack, no way to explain this except magic
        return struct.unpack('>f', binascii.unhexlify(the_hex))[0]

    def two_registers_into_long(register_1, register_2):

        #registers into hex strings
        hex_1 = hex(int(register_2))[2:]
        hex_2 = hex(int(register_1))[2:]
        #String concat
        the_hex = hex_1 + hex_2
        #print(len(the_hex))  
        if len(the_hex) == (8):      
        #Unpack, no way how it is happening. but result verified
            return struct.unpack('>l', binascii.unhexlify(the_hex))[0]
        else:
            return int(the_hex)
   
    def one_register_into_int(register):
        bin_string = bin(register)
        #Last four bits, the 2 in the end means that its using binary, why? I dont know.
        return int(bin_string[4:],2)
    
    def one_register_into_integer(register):
        bin_string = bin(register)
        return int(bin_string,2)

    def one_register_into_bcd(register):
        bin_string = bin(register)
        return int(bin_string,2)

    def two_registers_into_bcd(register_1, register_2):
        hex_1 = hex(int(register_2))[2:]
        hex_2 = hex(int(register_1))[2:]
        #String concat
        the_hex = hex_1 + hex_2
        return int(the_hex,16)

    #Let's add our functions in the dict. 

    #Thanks https://wiki.python.org/moin/BitManipulation   

      
    #Iterate the input_list
    for t in input_list:

#Function calls for converting register inout values into INTEGER
        if t == (92,):         
            register_value = register_dict[92]
            decoding = one_register_into_int(register_value)
            print (t, decoding)
        elif t == (59,):
            register_value = register_dict[59]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (60,):
            register_value = register_dict[60]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (61,):
            register_value = register_dict[61]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (62,):
            register_value = register_dict[62]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (93,):
            register_value = register_dict[93]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (94,):
            register_value = register_dict[94]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
        elif t == (96,):
            register_value = register_dict[96]
            decoding = one_register_into_integer(register_value)
            print (t, decoding)
 #Function calls for converting register input values into Binary code decimal

        elif t == (51,):
            register_value = register_dict[51]
            decoding = one_register_into_bcd(register_value)
            print (t, decoding)
        elif t == (56,):
            register_value = register_dict[56]
            decoding = one_register_into_bcd(register_value)
            print (t, decoding)
        elif t == (53,55):
            register_value_1 = register_dict[53]
            register_value_2 = register_dict[55]
            decoding = two_registers_into_bcd(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (49,50):
            register_value_1 = register_dict[49]
            register_value_2 = register_dict[50]
            decoding = two_registers_into_bcd(register_value_1, register_value_2)
            print (t, decoding)        
   
#Function calls for converting register input values into LONG        
        elif t == (21,22):
            register_value_1 = register_dict[21]
            register_value_2 = register_dict[22]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (9,10):
            register_value_1 = register_dict[9]
            register_value_2 = register_dict[10]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (13,14):
            register_value_1 = register_dict[13]
            register_value_2 = register_dict[14]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (17,18):
            register_value_1 = register_dict[17]
            register_value_2 = register_dict[18]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (25,26):
            register_value_1 = register_dict[25]
            register_value_2 = register_dict[26]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (29,30):
            register_value_1 = register_dict[29]
            register_value_2 = register_dict[30]
            decoding = two_registers_into_long(register_value_1, register_value_2)
            print (t, decoding)

#Function calls for converting register input values into REAL4 format       
        elif t == (1,2):
            register_value_1 = register_dict[1]
            register_value_2 = register_dict[2]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (3,4):
            register_value_1 = register_dict[3]
            register_value_2 = register_dict[4]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (5,6):
            register_value_1 = register_dict[5]
            register_value_2 = register_dict[6]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (7,8):
            register_value_1 = register_dict[7]
            register_value_2 = register_dict[8]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (11,12):
            register_value_1 = register_dict[11]
            register_value_2 = register_dict[12]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (19,20):
            register_value_1 = register_dict[19]
            register_value_2 = register_dict[20]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding) 
        elif t == (23,24):
            register_value_1 = register_dict[23]
            register_value_2 = register_dict[24]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (31,32):
            register_value_1 = register_dict[31]
            register_value_2 = register_dict[32]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (35,36):
            register_value_1 = register_dict[35]
            register_value_2 = register_dict[36]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding) 
        elif t == (33,34):
            register_value_1 = register_dict[33]
            register_value_2 = register_dict[34]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (37,38):
            register_value_1 = register_dict[37]
            register_value_2 = register_dict[38]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (39,40):
            register_value_1 = register_dict[39]
            register_value_2 = register_dict[40]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (41,42):
            register_value_1 = register_dict[41]
            register_value_2 = register_dict[42]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (43,44):
            register_value_1 = register_dict[43]
            register_value_2 = register_dict[44]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (45,46):
            register_value_1 = register_dict[43]
            register_value_2 = register_dict[44]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)
        elif t == (47,48):
            register_value_1 = register_dict[47]
            register_value_2 = register_dict[48]
            decoding = two_registers_into_float(register_value_1, register_value_2)
            print (t, decoding)


main()
