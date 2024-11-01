#python code
import sys
if (len(sys.argv) > 2):
    address = 0
    f = open(sys.argv[1], "rb")
    o = open(sys.argv[2], "w")
    o.write("""device CDC3217G
si JTAG
speed 4000
jtagconf -1,-1
connect
halt
w1 0x200aaa,0xAA
w1 0x200555,0x55
w1 0x200aaa,0x80
w1 0x200aaa,0xAA
w1 0x200555,0x55
w1 0x200000,0x30
sleep 2000
""")
    word = f.read(2)
    while(word):
        if (address == 0x10000) or (address == 0x20000) or (address == 0x30000) or (address == 0x40000) or (address == 0x50000) or (address == 0x60000) or (address == 0x70000) or (address == 0x80000) or (address == 0x90000) or (address == 0xA0000) or (address == 0xB0000) or (address == 0xC0000)or (address == 0xD0000) or (address == 0xE0000) or (address == 0xF0000) or (address == 0xF8000) or (address == 0xFA000) or (address == 0xFC000):
            o.write("""w1 0x200aaa,0xAA
w1 0x200555,0x55
w1 0x200aaa,0x80
w1 0x200aaa,0xAA
w1 0x200555,0x55
w1 """)
            o.write(hex(0x200000+address))
            o.write(""",0x30
sleep 2000\n""")
        if (0xffff != (word[0] | (word[1]<<8))):  
            o.write("""w1 0x200aaa,0xAA
w1 0x200555,0x55
w1 0x200aaa,0xA0
w2 """)
            o.write(hex(0x200000+address))
            o.write(",")
            o.write(hex(word[0] | (word[1]<<8)))
            o.write("\n")
        word = f.read(2)
        address = address + 2
    f.close()
    o.close()
else:
    print("Usage: ")
    print(sys.argv[0])
    print("<inputFile.bin> <outFile.jlink>\n")
