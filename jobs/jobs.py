from audioop import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from datetime import datetime
from mon.models import MasterThreshold, Temperature_Data, Temperature_Trend
import numpy as np

def get_data():

    slave = 1
    reg = 1000     #address 31001
    ln = 1
    a=Temperature_Data.objects.get()
    b=Temperature_Trend()

    # Modbus TCP
    client=ModbusClient(host='10.10.10.254',port=502)
    
    # Modbus RTU 
    # client = ModbusClient(method='rtu', port='COM5', timeout=1, stopbits = 1, bytesize = 8, parity = 'E', baudrate = 19200)
   
    if client.connect() :
        result = client.read_input_registers(reg,ln,unit=slave)
        client.close()
        print(result.getRegister(0),"C")
        a.temperature=float(result.getRegister(0))
        a.save()
        b.temperature=float(result.getRegister(0))
        b.save()
        return
    else:
        print("Disconnected")
        a.temperature=-0
        b.temperature=-0
        a.save()
        b.save()
        return




    

#Input Register
#CH1 = 31001
#CH2 = 31007
#CH3 = 31013
#CH4 = 31019
