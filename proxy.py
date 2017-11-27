#!/usr/bin/python3

#created by Nityananda Gohain 
#27/10/17

#run it as sudo

#This files takes the location as input and writes the proxy authentication

def writeToFile(location):
	filepointer = open(location,"w")
	filepointer.write('Acquire::http::proxy "http://{0}:{1}@{2}:{3}/";\n'.format(username,password,proxy,port))
	filepointer.write('Acquire::https::proxy  "https://{0}:{1}@{2}:{3}/";\n'.format(username,password,proxy,port))
	filepointer.write('Acquire::ftp::proxy  "ftp://{0}:{1}@{2}:{3}/";\n'.format(username,password,proxy,port))
	filepointer.write('Acquire::socks::proxy  "socks://{0}:{1}@{2}:{3}/";\n'.format(username,password,proxy,port))
	filepointer.close()


if __name__ == "__main__":
	proxy = input("Enter proxy : ")
	port  = input("Enter port : ")
	username = input("Enter uername : ")
	password = input("Enter password : ")
	writeToFile("/etc/apt/apt.conf")
