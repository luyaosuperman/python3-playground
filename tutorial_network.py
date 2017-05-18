import socket
#s=[]

for i in range(5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1',22))
    #s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    print(s)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname('aurora-test.cluster-cquwj4tlhao5.ap-southeast-2.rds.amazonaws.com'))
result = sock.connect_ex(('aurora-test.cluster-cquwj4tlhao5.ap-southeast-2.rds.amazonaws.com',3306))
if result == 0:
   print("Port is open")
else:
   print("Port is not open")


print("-----------")
import urllib.request

httpbin = "httpbin.org/"

site_dict = {"good-site"  : "google.com",
             "bad-site"   : "non-exist.com",
             "wrong-url"  : "google.com/sdfsdf",
             "ip"         : httpbin + "ip",
             "user-agent" : httpbin + "user-agent",
            }

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')


for desc,url in site_dict.items():
    print("======> now testing {0} : {1}".format(desc,url))
    req = urllib.request.Request('http://{0}'.format(url), data=None, headers=headers)
    try:
        print("inside try")
        response = urllib.request.urlopen(req)
        html = response.read()
        print(html[:50])
        print(response.getcode())
        print(response.info().items())
    except urllib.error.HTTPError as e:
        print("inside except 1")
        print(e.code)
        print(e.read()[:50])
    except urllib.error.URLError as e:
        print("inside except 2")
        print(e.reason)
    

#    with urllib.request.urlopen('http://{0}/'.format(url)) as response:
#        html = response.read()
#        print(html[:100])
#        print(response.getcode())
   
