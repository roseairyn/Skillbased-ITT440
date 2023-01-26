import socket

socketaddr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketaddr.connect(('127.0.0.1', 8080))

print("Fahrenheit Conversion!")

tempf = input("Please enter the temperature in the Fahrenheit: ")
socketaddr.send(tempf.encode())
tempc = socketaddr.recv(1024)
tempc = float(tempc.decode())
print("The result of temperature in Celsius: ", tempc)

socketaddr.close()
