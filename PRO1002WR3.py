#Work Requirement 3 - Simple socket task and short reflection

#Task: Use the socket module to resolve a hostname into an IP address & print a short greeting together with the resolved IP
#Benytter eksempelet i Module 5.4 for å løse oppgaven

import socket #import of socket library, for reference: https://docs.python.org/3/library/socket.html#functions

HOST = 'localhost'
PORT = 12345
ADRESS = (HOST, PORT)

def hostnametoIP():
    ip_address = socket.gethostbyname(HOST) #Translate a host name to IPv4 address format (description from library)
    print(ip_address)
hostnametoIP()

