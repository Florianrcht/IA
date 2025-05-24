import threading
from streaming_sender import streaming_socket
from servo import servo_function

if __name__ == '__main__':
    stream_thread = threading.Thread(target=streaming_socket)
    stream_thread.start()

    servo_function()
