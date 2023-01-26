import socket

def main():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "10.0.179.123"
    port = 8080

    socket_client.connect((host, port))

    quotes = socket_client.recv(1024)
    print("Random Quotes Of The Day\n %s" % quotes.decode())

    socket_client.close()
    main()