import socket
from platform import system
from scapy.all import *

TAB_1 = '\t'
TAB_2 = '\t\t'

runningOS = system()

HOST = '192.168.1.1'  
PORT = 1111  

def main():
    global clientSocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Trying to connect to the server...')
    try:
        clientSocket.connect((HOST, PORT))  
        print(f'[INFO] You are connected to: {HOST} in port: {PORT}.')
        welcomeMessage = clientSocket.recv(1024)  
        print(welcomeMessage.decode())
    except socket.error as error:
        exit(
            f'[ERROR] Connecting to the server failed:\n\033[31m{error}\033[0m')


if __name__ == '__main__':
    main()
    
