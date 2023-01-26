import socket

def fahrenheit_conversion(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    return celsius

    socketaddr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketaddr.bind(('127.0.0.1', 8080))
    socketaddr.listen(1)

    print("Listening on from client..")

    while True:
        connection, address = socketaddr.accept()
        print("Connection Successful")

        tempf = connection.recv(1024).decode()
        tempf = float(tempf)
        tempc = fahrenheit_conversion(tempc)

        connection.send(str(tempc).encode())
        connection.close()
     
