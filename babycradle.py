
import sys
import glob
import serial
import pyttsx3


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# In[2]:


ports=serial_ports()
print(ports)
if len(ports)>0:
    portname=ports[0]
else:
    print("No Devices Connected")


# In[3]:


import time
import serial
import pymysql


# db = pymysql.connect("localhost","root","","line_detection" )
ser = serial.Serial()

ser.port = portname

ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

try:
    if ser.isOpen():
        ser.close()
except:
    print("error")
try: 
    ser.open()
except Exception:
#     print ("error open serial port: " + str(e))
    exit()
   


# In[4]:


import pymysql
# def savedata(sql):
#     db = pymysql.connect(host='localhost',user="root",password="",database="line_detection" )
#     c = db.cursor()
#     c.execute(sql)
#     db.commit()
#     c.close()
#     db.close()
    
# def getvalues(sql):
#     db = pymysql.connect(host='localhost',user="root",password="",database="line_detection" )
#     c = db.cursor()
#     c.execute(sql)
#     val=c.fetchall()
#     ret=""
#     if len(val)>0:
#         ret="Error"
#     else:
#         ret="ok"
#     print(val)
#     db.commit()
#     c.close()
#     db.close()
#     return ret


# In[ ]:


from datetime import datetime
import requests
if ser.isOpen():
    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output 
        numOfLines = 0
        outp=""
        ap=1
        cnt=0
        
        while True:
            try:
                svalues=ser.readline().decode('utf-8').rstrip()
                #print(svalues)
                if svalues!="":
                    print(svalues)
                    dat=datetime.now()
                    dt=dat.strftime("%Y-%m-%d")
                    tm=dat.strftime("%H:%M")
                    va=svalues.split(':')
                    #print('hello')
                    print(va[3])
                    try:
                        iva=float(va[3].strip())
                        if iva<260:
                            #print("hello")
                            url = "https://www.fast2sms.com/dev/bulkV2"

                            payload = "message=Wetness detected&language=english&route=q&numbers=9747087491"
                            headers = {
                                'authorization': "bBQMFiU6AKGScRCnsEZ2DYmL1zNxoq4rtOvy3fhTJe5kX9lawpxuBqAekHn7sWEYP8L1Z2dSJ5pc3fwT",
                                'Content-Type': "application/x-www-form-urlencoded",
                                'Cache-Control': "no-cache",
                            }
                            
                            response = requests.request("POST", url, data=payload, headers=headers)
                            
                            print(response.text)
                    except Exception as ex:
                        print(ex)
                        pass
                    if 'Sound' in svalues:
                        print('Motion detected')
                        

                        url = "https://www.fast2sms.com/dev/bulkV2"

                        payload = "message=Baby Crying&language=english&route=q&numbers=9747087491"
                        headers = {
                            'authorization': "bBQMFiU6AKGScRCnsEZ2DYmL1zNxoq4rtOvy3fhTJe5kX9lawpxuBqAekHn7sWEYP8L1Z2dSJ5pc3fwT",
                            'Content-Type': "application/x-www-form-urlencoded",
                            'Cache-Control': "no-cache",
                        }
                        
                        response = requests.request("POST", url, data=payload, headers=headers)
                        print(response.text)
                        

                        
                    '''
                    if 'wet' in svalues:
                        
                    '''
                     
                    
            except Exception as e:
                print("except")
                print(e)
                pass
        ser.close()
    except Exception:
        print ("error communicating...: " + str(e1))
else:
    print ("cannot open serial port ")

