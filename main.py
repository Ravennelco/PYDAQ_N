import nidaqmx
import time 
from openpyxl import Workbook
'''
task = nidaqmx.Task()
task.ao_channels.add_ao_voltage_chan('Dev2/ao0','mychanel',0,5)
task.start()

value = 2
task.write(value)
task.stop()
task.close()
'''
wb = Workbook()
ws = wb.active
    

task = nidaqmx.Task()
task2 = nidaqmx.Task()
task.ai_channels.add_ai_voltage_chan('Dev1/ai0',min_val= 0, max_val = 5)
task.ai_channels.add_ai_voltage_chan('Dev1/ai1',min_val= 0, max_val = 5)
task.ai_channels.add_ai_voltage_chan('Dev1/ai2',min_val= 0, max_val = 6)
task2.ao_channels.add_ao_voltage_chan('Dev1/ao1','mychanel',0,6)
#task.write(value)
#time.sleep(2)
value2 = 0
value = [0,0,0]
for count in range(1,10001,1):
    #value = value + 0.03
    time.sleep(0.1)
    #print(count)
    value = task.read()
    task2.write(value[2]+0.07)
    print(value[2]+0.07)
    #celdaI = f'A{count}'
    #celdaD = f'B{count}'
    #ws[celdaI] = value[0]
    #ws[celdaD] = value[1]
wb.save('Datos.xlsx')

#value = 0.5
#task.write(value)
task.stop()
task.close()

