#from requests import Session
import requests,os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#baseurl = 'https://s8.work/'
#baseurl = 'https://xiaojiangzi.bid/'
#gqt1.info
def checkSpecSite(site) :
    baseurl = 'http://'+site
    url = baseurl+'/auth/login'
    payload = {
            'email':'weiqianglord@gmail.com',
            'passwd':'zhang1999',
            'remember_me':1,
            'datatype':'json'
            }
    
    http_proxy = "http://127.0.0.1:1080"
    proxyDict = {
            "http" : http_proxy,
            "https": http_proxy
            }
    s = requests.session()
    try:
        ret = s.post(url,data=payload,proxies=proxyDict)
    except requests.packages.urllib3.exceptions.MaxRetryError as e:
        print("ERROR",repr(e))
    except requests.packages.urllib3.exceptions.RemoteDisconnected as e:
        print("ERROR",repr(e))
    if (site == 'haoss.top'):
        s.headers.update({'referer':baseurl+'/user'})
        baseurl = 'https://'+site
    url = baseurl+'/user/checkin'
    try:
        ret = s.post(url,proxies=proxyDict)
    except:
        print("error in check",ret.text)
    print("checking", site, " ...")
    try:
        print(ret.json())
    except:
        print("unexpected error:",repr(ret))


def checkSite(site) :
    baseurl = 'https://'+site
    url = baseurl+'/auth/login'
    payload = {
            'email':'weiqianglord@gmail.com',
            'passwd':'zhang1999',
            'datatype':'json'
            }
    
    http_proxy = "http://127.0.0.1:1080"
    proxyDict = {
            "http" : http_proxy,
            "https": http_proxy
            }
    s = requests.session()
    try:
        ret = s.post(url,data=payload,proxies=proxyDict)
    except:
        print("error in auth",ret.text)
    url = baseurl+'/user/checkin'
    try:
        ret = s.post(url)
    except:
        print("error in check",ret.text)
    print("checking", site, " ...")
    try:
        print(ret.json())
    except:
        print("unexpected error:",ret.text)

def simCheck(site):
    chromedriver = "d:/bin/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chOpt = Options()
    chOpt.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chOpt)
    baseurl = 'https://'+site;

    driver.get(baseurl+"/auth/login")
    email = driver.find_element_by_name("Email")
    email.send_keys("weiqianglord@gmail.com")
    passwd = driver.find_element_by_name("Password")
    passwd.send_keys("zhang1999")
    btn = driver.find_element_by_id("passwd_login")
    login = btn.find_element_by_id("login")
    driver.implicitly_wait(2)
    user = login.click()

    driver.implicitly_wait(5)
    userProfile = driver.find_element_by_xpath("//a[@href='/user/profile']")
    userProfile.click()

    driver.implicitly_wait(2)
    links = driver.find_element_by_css_selector("a")
    s = links.find_element_by_xpath("//a[@href='#all_sign']")
    s.click()
    try:
        driver.implicitly_wait(2)
        check = driver.find_element_by_id("checkin")
        check.click()
        driver.quit()
    except:
        check = driver.find_element_by_partial_link_text("check")
        print(check.text)

def simCheck1(site):
    chromedriver = "d:/bin/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chOpt = Options()
    chOpt.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chOpt)
    baseurl = 'https://'+site;

    driver.get(baseurl)
    loginBtn = driver.find_element_by_partial_link_text("vpn")
    email = driver.find_element_by_name("Email")
    email.send_keys("weiqianglord@gmail.com")
    passwd = driver.find_element_by_name("Password")
    passwd.send_keys("zhang1999")
    btn = driver.find_element_by_id("passwd_login")
    login = btn.find_element_by_id("login")
    user = login.click()

    driver.implicitly_wait(5)
    userProfile = driver.find_element_by_xpath("//a[@href='/user/profile']")
    userProfile.click()

    driver.implicitly_wait(2)
    links = driver.find_element_by_css_selector("a")
    s = links.find_element_by_xpath("//a[@href='#all_sign']")
    s.click()
    try:
        driver.implicitly_wait(2)
        check = driver.find_element_by_id("checkin")
        driver.implicitly_wait(2)
        check.click()
    except:
        check = driver.find_element_by_partial_link_text("check")
        print(check.text)
sites = ['s8.work','gqt1.info','ssfjc.xyz']
specSites = ['xiaojiangzi.bid','haoss.top']

for s in specSites:
    checkSpecSite(s)

for s in sites:
    checkSite(s)

simCheck("feiyun.us")
