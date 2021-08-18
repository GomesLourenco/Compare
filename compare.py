import base64
import binascii

def compare_texts(text1,text2,name):
    valid = 1 
    text1_l = list(text1)
    text = list(text2)
    data2 = "".join([str(i) for i in text1_l])
    original_list = []
    for i in data2.split(' '):
        original_list.append(chr(int(i, 2))) 
    del original_list[0:2]
    del original_list[(len(original_list) - 1)]

    part1_errors = 0 
    part2_errors = 0
    

    dat = text[(text.index('#')+20):]
    data = dat[:(text.index('#'))]
    data2 = "".join([str(i) for i in data])
    ascii_list = []
    for i in data2.split(' '):
        try: 
            ascii_list.append(chr(int(i, 2))) 
        except Exception:
            valid = 0 
            pass
    del ascii_list[0:2]
    del ascii_list[(len(ascii_list) - 1)]

    for i in range(len(ascii_list)):
        if ascii_list[i] != original_list[i]:
            part1_errors += 1
        

    string = ''.join(map(str, ascii_list))
    with open(name+'1'+'.png', "wb") as fh:
        try:
            fh.write(base64.decodebytes((string).encode("utf-8")))
        except Exception:
            valid = 0 
            pass

    
    dat = text[(text.index('#')+20):]
    dat[(text.index('#')+20):]
    data2 = dat[:(text.index('#'))]
    data2 = "".join([str(i) for i in data])
    ascii_list = []
    for i in data2.split(' '):
        try: 
            ascii_list.append(chr(int(i, 2))) 
        except Exception:
            valid = 0 
            pass
    del ascii_list[0:2]
    del ascii_list[(len(ascii_list) - 1)]

    for i in range(len(ascii_list)):
        if ascii_list[i] != original_list[i]:
            part2_errors += 1


    string = ''.join(map(str, ascii_list))
    if valid == 1:
        try:
            with open(name+'2'+'.png', "wb") as fh:
                fh.write(base64.decodebytes((string).encode("utf-8")))
            errors = (part1_errors + part2_errors)/2
            print("Average Errors: "+str(errors))
        except Exception:
            pass
    else:
        print(name+" not valid")
            
    
with open("Send/original.txt", 'r') as file1:
    data1 = file1.read().replace('\n', '')

avaialble = ['600M','700M','800M','850M','900M','1000M','1600M','1700M','1900M','2000M','2100M','2300M']
for i in range(len(avaialble)):
    print('Frequency: '+avaialble[i])
    with open(("Receive/"+avaialble[i]+'.txt'), 'r')  as file2:
        data2 = file2.read().replace('\n', '')
    compare_texts(data1,data2,avaialble[i])
    
