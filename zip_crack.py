import zipfile
import getopt
import sys
import threading
def usage():
    print('******************************************************')
    print('Crack the zip file, use args: -f :zip file name, -d dic name')
    print('e.g.  zip_crack.exe -f 1.zip -d dic.txt')
    print('******************************************************')
def crack(file_name,crack_dic,file_gue):
    kv = crack_dic.readlines()
    end_num = kv[-1]
    print(end_num)
    for i in kv:          
        print('[+]try passwd:'+i)                                  
        if i.strip('\n') == end_num.strip('\n'):                    
            try:
                file_gue.extractall(pwd = i.strip('\n').encode('utf-8'))
                print('[*]Successfully crack, passwd is '+i) 
                break
            except:
                print('[*]Crack fail, please change your dic')  
                sys.exit()
        try:         
            file_gue.extractall(pwd = i.strip('\n').encode('utf-8'))
            print('[*]Successfully crack, passwd is '+i)
            break
        except:
            pass
    crack_dic.close()
def main():
    file_name = ''
    dic_name = ''    
    try:
        opts,args = getopt.getopt(sys.argv[1:],'f:d:')
        for a,b in opts:
            if a == '-f':
                file_name = b
            if a == '-d':
                dic_name = b
        crack_dic = open(dic_name,'r')   
    except:
        usage()
        sys.exit()   
    file_gue = zipfile.ZipFile(file_name)
    t = threading.Thread(target = crack(file_name,crack_dic,file_gue))
    t.start()
main()