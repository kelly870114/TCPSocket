#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# client
from socket import *
import os

serverName = input('What is the server address?')
serverPort = 12002
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Socket', clientSocket.fileno(), 'opened to server', serverName, ':', serverPort)

msg = ""
while msg != "exit":
  msg = input("What to send to the server: ")
  clientSocket.send(str.encode(msg))
  if(msg == "exit"):
    break
  response = clientSocket.recv(1024)
  print('Server says:', bytes.decode(response))


clientSocket.close()