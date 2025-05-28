import socket, cv2, pickle,struct

def streaming_socket():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_name  = socket.gethostname()
    port = 9999
    socket_address = ('',port)

    server_socket.bind(socket_address)

    server_socket.listen(5)
    print("Écoute sur :",socket_address)

    while True:
        client_socket,addr = server_socket.accept()
        print('Connexion depuis :',addr)
        if client_socket:
            vid = cv2.VideoCapture(0) #1 pour Mac
            vid.set(cv2.CAP_PROP_FRAME_WIDTH, 420) #Réduis la taille de l'image 
            vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 340)
            
            while(vid.isOpened()):
                img,frame = vid.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a
                client_socket.sendall(message)
                