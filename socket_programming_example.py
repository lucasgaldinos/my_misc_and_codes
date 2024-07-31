# https://www.geeksforgeeks.org/socket-programming-python/
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 80

ip = socket.gethostbyname('www.google.com')
print(ip)

s.connect((ip, port))
