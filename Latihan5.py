import socket
def convert_integer():
    data = 1234
    #32-bit
    print ("original: %s ==> Long Host Byte Order: %s, Network byte order: %s"
           %(data, socket.ntohl(data), socket.htonl(data)))
    #16-bit
    print ("original: %s ==> Short Host Byte Order: %s, Network byte order: %s"
           %(data, socket.ntohl(data), socket.htonl(data)))
    

if __name__ == '__main__':
        convert_integer()