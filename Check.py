################################################################
# Author : WASU 
# GitHub : BHATWASUXWD
# Coder   : PATA NHI KON BHEN KA LODA HX
# You Have No Permission To Copy Any Codes From This Script
# Coping Others Code Will Not Make You a Coder
# But You're Welcomed To Take Any Knowledge From This Script
################################################################

import time, sys, os, re
import requests


def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.03)

def logopsb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.001)

def logo():
    os.system("clear")
    logopsb("\033[92m  ____          _____     _              \n / ___| ___ _ _|_   _|__ | | _____ _ __  \n| |  _ / _ \ '_ \| |/ _ \| |/ / _ \ '_ \ \n| |_| |  __/ | | | | (_) |   <  __/ | | |\n \____|\___|_| |_|_|\___/|_|\_\___|_| |_|\n                                         ")
    logopsb("\033[3;90m			A Product Of WASU TRICKER\033[0;92m")
    time.sleep(0.6)
    logopsb("\033[34m\n|****************************************************|\n|\033[3m Author   : WASU TRICKER                               \033[0;34m|\n|\033[3m Tool     : Facebook Token Generator                \033[0;34m|\n|\033[3m Version  : 1.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/ERIIC-3XO/	     \033[0;34m|\n|\033[3m Coded By : ERIIC EXO      		     	     \033[0;34m|\n******************************************************")
    time.sleep(0.8)
    


def logout():
    psb("\n\033[92m    [*] Thanks For Using Our Tool...")
    psb("    [*] For More Tools, Visit :")
    psb("\n\t[https://www.facebook.com/profile.php?id=100001302286495]\n")
    sys.exit()

def real_time():
    from time import time
    return str(time()).split('.')[0]

def convert(data):
    cookie_data = (
            "datr="+data["datr"]
        )+";"+(
            "c_user="+data["c_user"]
        )+";"+(
            "fr="+data["fr"]
        )+";"+(
            "xs="+data["xs"] )
    return cookie_data
    
    
def user_agent():
            if os.path.exists(".agent"):
                data = open(".agent", "r").read()
            else:
                psb("\033[92m\n    [*] Go To Your Browser, Copy your UserAgent and Past Here...")
                os.system("xdg-open https://chat.whatsapp.com/I3mZhhOKSas2lW9MjoIoDe")
                time.sleep(1)
                data = input("\n    [*] Enter Your User Agent:> \033[37m")
                file = open(".agent", "w")
                file.write(data)
                file.close()
            return data


###Email_Login###
def email_login():
    agent  = user_agent()
    user = input("\033[92m\n    [*] Enter Your Number/Email:> \033[37m")
    pw = input("\033[92m\n    [*] Enter Your Password:> \033[37m")
    while (len(pw) < 6):
        psb("\n\033[91m    [*] Please Check Your Password and Enter Again...")
        pw = input("\033[92m\n    [*] Enter Your Password:> \033[37m")
    time.sleep(0.6)
    logo()
    try:
        head = {
            'Host' : 'm.facebook.com',
                'cache-control' : 'max-age=0',
            'upgrade-insecure-requests' : '1',
                'user-agent' : agent,
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-mode' : 'navigate',
                'sec-fetch-user' : '?1',
            'sec-fetch-dest' : 'document',
                'accept-encoding' : 'gzip, deflate',
            'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        try:
            r = ses.get("https://m.facebook.com/", headers = head).text.encode('utf-8')
        except:
            r = ses.get("https://m.facebook.com/", headers = head).text
        head2 = {
            'Host' : 'm.facebook.com',
                'user-agent' : agent,
            'content-type' : 'application/x-www-form-urlencoded',
                'x-fb-lsd' : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            'accept' : '*/*',
                'origin' : 'https://m.facebook.com',
            'sec-fetch-site' : 'same-origin',
                'sec-fetch-mode' : 'cors',
            'sec-fetch-dest' : 'empty',
                'referer' : 'https://m.facebook.com/',
            'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        payload = {
            "fb_dtsg" : re.search('{"token":"(.*?)"', str(r)).group(1),
                "lsd" : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
                "m_ts" : re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
            "li" : re.search('name="li" value="(.*?)"', str(r)).group(1),
                "try_number" : "0",
            "unrecognized_tries" : "0",
                "prefill_contact_point" : user,
            "prefill_source" : "browser_dropdown",
                "prefill_type" : "contact_point",
            "first_prefill_source" : "browser_dropdown",
                "first_prefill_type" : "contact_point",
            "had_cp_prefilled" : True,
                "had_password_prefilled" : False,
            "is_smart_lock" : False,
                "bi_xrwh" : "0",
            "__dyn" : "",
                "__csr" : "",
            "__req" : "2",
                "__a" : "",
            "__user" : "0",
                "email" : user,
            "encpass" : "#PWD_BROWSER:0:"+real_time()+":"+pw
        }
        ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers = head2, data = payload)
        cookie = ses.cookies.get_dict()
        if 'c_user' in (cookie):
            head = {
                'Host' : 'business.facebook.com',
                    'cache-control' : 'max-age=0',
                'upgrade-insecure-requests' : '1',
                    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'content-type' : 'text/html; charset=utf-8',
                'accept-encoding' : 'gzip, deflate',
                    'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }    
            r = ses.get(urls, headers = head)
            p = re.search('(EAAG\w+)', r.text)
            token = p.group(1)
            print("\n\033[92m    [*] Cookie:> \033[37m"+convert(cookie))
            print("\n\033[92m    [*] Token:> \033[37m"+token)
            logout()
        elif "checkpoint" in (cookie):
            psb("\n\033[91m    [*] Your ID is In Checkpoint!!\033[37m")
        else:
            psb("\n\033[91m    [*] Your Email or Password is Wrong!!\033[37m")
    except AttributeError:
        psb("\n\033[91m    [*] Your Email or Password is Wrong!!\033[37m")


###Cookie_Login###
def cookie_login():
    cookies = input("\n\033[92m    [*] Enter Your Cookie:> \033[37m")
    time.sleep(0.6)
    logo()
    try:
        head = {
            'Host' : 'business.facebook.com',
                'cache-control' : 'max-age=0',
            'upgrade-insecure-requests' : '1',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type' : 'text/html; charset=utf-8',
            'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie' : cookies
        }         
        r = ses.get(urls, headers = head)
        p = re.search('(EAAG\w+)', r.text)
        token = p.group(1)
        print("\033[92m\n    [*] Token:> \033[37m"+token)
        logout()
    except (AttributeError, requests.exceptions.TooManyRedirects):
        psb("\n\033[91m    [*] Cookie Expired!!\033[37m")




def main():
    logo()
    psb("\n\033[92m    [*] Choose Your Login Method :")
    print("\n    [01] Login With Email")
    print("    [02] Login With Cookie")
    print("    [##] Exit")
    op = input("\033[92m\n    [*] Enter Your Choice:> \033[37m").replace("0", "").replace("##", "")
    while not op in ["1", "2", "#"]:
        psb("\n\033[91m    [*] Choose a Correct Option!!")
        op = input("\033[92m\n    [*] Enter Your Choice:> \033[37m").replace("0", "").replace("##", "")
        
    if (op == "1"):
        email_login()
        k = input("\033[92m\n    [*] Press Enter To Go Back...")
    elif (op == "2"):
        cookie_login()
        k = input("\033[92m\n    [*] Press Enter To Go Back...")
    elif (op == "#"):
        logout()
        
        

if __name__ == '__main__':
    ses = requests.Session()
    urls="https://business.facebook.com/business_locations"
    while True:
        main()
