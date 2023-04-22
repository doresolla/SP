import http.client
import re
import socket
import uuid

h_name = socket.gethostname()
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
print("IP address: " + str(conn.getresponse().read()))
print("Host Name:" + h_name)
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))
