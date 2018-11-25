#!/usr/bin/python3

import socket
import struct

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

try:
    host = socket.gethostbyname('vortex.labs.overthewire.org')
    port = 5842
    s.connect( (host, port) )
    in1 = s.recv(4)
    in2 = s.recv(4)
    in3 = s.recv(4)
    in4 = s.recv(4)

    int1 = struct.unpack('<L', in1)[0]
    int2 = struct.unpack('<L', in2)[0]
    int3 = struct.unpack('<L', in3)[0]
    int4 = struct.unpack('<L', in4)[0]

    s.send( struct.pack('<L', int1+int2+int3+int4) )

    print( str(s.recv(1024).decode()) )

except:
    print("kaboom")

