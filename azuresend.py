import time
from datetime import datetime
from azure.storage.table import TableService
import os, glob, time, sys, datetime

#initiate the temperature sensor in Parasitic mode
os.system('sudo modprobe w1-gpio pullup=1')
os.system('sudo modprobe w1-therm strong_pullup=1')

#set up the location of the sensor in the system

device_folder = glob.glob('/sys/bus/w1/devices/28*')
device_file = [device_folder[0] + '/w1_slave']


def SendAzure():
        table_service = TableService(account_name='[NAMEHERE]', account_key='[KEYHERE]')
        table_name = 'tempData'
        partition_key = 'central'
        table_service.create_table(table_name, False)

        date = datetime.datetime.now()
        iso_date = date.isoformat()    
        tempRecord = ReadTemp()
        result = ""
        
        if(tempRecord < 70):
                entry = {'PartitionKey': partition_key, 'RowKey': iso_date, 'Temperature': tempRecord}
                table_service.insert_entity(table_name, entry)
                result = "SENT " + str(tempRecord)
        else:
                result = "ERROR " + str(tempRecord)
        return result


def ReadTemp():
        f = open(device_file[0], 'r')
        line = f.readline()
        crc = line.rsplit(' ',1)
        crc = crc[1].replace('\n', '')
        if crc=='YES':
                line = f.readline() 
                temp_list = line.rsplit('t=',1)
                mytemp = float(temp_list[1]) / 1000
                mytemp = round(mytemp, 4)
        else:
                mytemp = 85
                f.close()
        return float(mytemp)

print(SendAzure())
