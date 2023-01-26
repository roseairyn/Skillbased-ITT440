import socket
import threading
import random

quotes_word = ["An I tell myself, a moon will rise from my darkness. -Mahmoud Darwish",
                "History laughs at both the victim and the aggressor. -Mahmoud Darwish", 
                "I love you in a way i wish some would love me. -Mahmoud Darwish",
                "Eventhough everything we say or write, there are still things in the heart that are too big to be said. -Mahmoud Darwish",
                "You wont ever find the same person twice, not even in the same person. -Mahmoud Darwish"]

def client_input(socket_client):
    quotes = random.choice(quotes_word)
    socket_client.sendall(quotes.encode())
    socket_client.close()

def main():
    host = "10.0.179.123"
    port = 8080

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind((host, port))

    socket_server.listen()
    print("Listening on %s:%d for the request" % (host, port))

    while True:
        client, address = socket_server.accept()
        print("Connection Successful from %s" % str(address))

        client_handler = threading.Thread(target=client_input, args=(client,))
        client_handler.start()
        main()
