from pycomm3 import LogixDriver
with LogixDriver('192.168.58.2') as drive:
   plc = drive
   print(plc)
