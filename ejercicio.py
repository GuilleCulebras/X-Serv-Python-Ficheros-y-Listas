#!/usr/bin/python3

fd= open('/etc/passwd','r')

lineas= fd.readlines()

lineas[:1] # ['pepepeepepepepe']
lineas[0] # 'pepepeepepepepe'


#for linea in lineas:
#	elementos= linea.split(':')
#	login= elemento[0]
#	shell= elementos[-1]
#	print(login,shell)

for linea in lineas:
	login= linea.split(':')[0]
	shell= linea.split(':')[-1][:-1]#quitamos el \n para que no deje lineas en blanco
	print(login,shell)
