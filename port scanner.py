import socket

target = input("enter target ip or website: ")
print("Scanning " + target + "...")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port " , port , " is open!")
    s.close()
    
