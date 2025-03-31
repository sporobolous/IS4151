import socket



def client():
	
	try:
		
		host = socket.gethostname()
		port = 8888

		s = socket.socket()
		s.connect((host, port))

		message = input('-> ')
		
		while message != 'q':
			s.send(message.encode('utf-8'))
			data = s.recv(1024).decode('utf-8')
			print('Received from server: ' + data)
			message = input('==> ')		
	
	except KeyboardInterrupt:		
		
		print('Program terminated!')
	
	finally:
		
		s.close()



if __name__ == '__main__':
	client()