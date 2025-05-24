import socket, cv2, pickle,struct


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = ('',port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
    client_socket,addr = server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_socket:
        vid = cv2.VideoCapture(0) #1 pour Mac
        #vid.set(cv2.CAP_PROP_FRAME_WIDTH, 320) #Réduis la taille de l'image (très éfficace)
        #vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        
        while(vid.isOpened()):
            print('Stream')
            img,frame = vid.read()
            #a = pickle.dumps(frame)
            _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            a = buffer.tobytes()
            message = struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_socket.close()