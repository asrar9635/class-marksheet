# class-marksheet
import numpy as np
import pandas as pd
ms = {'NAME OF THE STUDENTS':['ABDUL','BASHEER','DANISH','DASTAGIR','EJAZ','FARHAN','FAHAD','FAHIM','FAZEEL','HAKEEM',
                            'IRFAN','JABIR','MAAZ','NADEEM','RAFI','RAHEEM','SHARIQUE','ZAID','ZAIN'],'DEPARTMENT':['BCA','BCA','BCA','B.com'
               ,'BBA','BCA','B.com','BSC-cs','BCA','BCA','B.com','BBA','BSC.MATH','BSC-cs','B.com','B.com','BCA','BCA','B.com'],
      'REGISTER NO':['HCU23J01','HCU23J08','HCU23J09','HCA23A20','HCU23K34','HCU23J23','HCA23A38','HCU23C12','HCU23J14','HCU23J49','HCA23A36',
                     'HCA23B14','HCA23K25','HCU23N45','HCA23B49','HCA23D54','HCU23K31','HCU23J34','HCA23A58']
,'ATTENDENCE %':['70%','89%','88%','66%','53%','45%','50%','76%','90%','23%','20%', '78%','67%','100%','10%','34%','86%','89%','12%'],
     'GENDER':['MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE','MALE'],
'TOTAL MARK':[340,450,500,470,300,570,489,534,600,359,368,332,675,745,236,565,787,789,346],'RESULT':['PASS','PASS','PASS','PASS','PASS','PASS','PASS',
                                                                                                     'PASS','PASS','PASS','PASS','PASS','PASS','PASS','FAIL','PASS','PASS','PASS','PASS']}  

ok = pd.DataFrame(ms)
ok
                                                                                                     
