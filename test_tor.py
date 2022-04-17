# import a
from a import *
if __name__ == '__main__':
    
    setup()
    B3M_setTor(0,-700)
    time.sleep(2)
    reData = B3M_Write_CMD(0x00, 0x02, 0x28)
    
