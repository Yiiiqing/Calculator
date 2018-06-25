#!/usr/bin/env python3.6
#coding:utf8

"""
Author:       Yiqing
Filename:     calculator_final.py
Date:         Jun 22, 2018
Description:

"""
import math
from jupyter_client.kernelspecapp import raw_input

''' default socket timeout '''
DEFAULT_TIMEOUT = 2.0

SERVER_ADDRESS = (HOST, PORT) = '', 12000
RPN = False
#Mode = raw_input('''Please select one mode:\n Infix/RPN'
#default mode is Infix\npress the button "R" for RPN.''').upper()
#if (Mode == 'R'):
#    RPN = True
#    print('switch to RPN mode')
#else:
#   RPN = False
print('''this calculator has two mode: Infix / RPN \n while running press "r" to switch. \n ======================================\nWarning: default mode is Infix,must start with Infix\n======================================''')
    
a = '0'
b = '0'
opr = 0
enter = False
length = 8
stateA_r = True
stateB_r = False
stateC_i = False
stateR_i = False
stateAC_i = False
stateA_i = False
stateS = False


def isint(a):
    if(math.floor(a) - a == 0):
        a = int(a)
    else:
        pass
    return a
while True: 
    raw = raw_input('Enter a key:')
    if (RPN == True):
        #raw = raw_input('Enter a key:')
        #stateA
        if (raw.isdigit() and stateA_r == True):
            if(a =='0'):
                a = raw
            else:
                a = str(a) + raw
            len_ = length - len(a)
            print('|'+len_*"_"+'{}|'.format(a),1)
            stateA_r = True
        else:    
            #stateB
            if (raw.upper() == 'ENTER'):
                enter = True
                stateA_r = False
                print('|'+len_*"_"+'{}|'.format(a),2)
            else:
                pass
            #stateC
            if (stateA_r == False and enter == True):
                if (raw.isdigit()):
                    if(b =='0'):
                        b = raw
                    else:
                        b = b + raw
                    len_ = length - len(b)
                    print('|'+len_*"_"+'{}|'.format(b),3)
                    stateB_r = True
        if (stateB_r == True):
            if ( raw =='+' or
                 raw =='-' or 
                 raw =='*' or 
                 raw =='/'or
                 raw =='='):
                if(raw =='+'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ + b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),4)
                    b = '0'
                    stateB_r = False
                if(raw =='-'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ - b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),5)
                    b = '0'
                    stateB_r = False
                if(raw =='*'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ * b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),6)
                    b = '0'
                    stateB_r = False
                if(raw =='/'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ / b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),7)
                    b = '0'
                    stateB_r = False
        if (raw.upper() == 'R'):
            if(RPN == True):
                print('switch to Infix mode')
                b = opr = '0'
                RPN =False
                stateS = True
                print('|'+len_*"_"+'{}|'.format(a),8)
            else:
                pass
    else:
             
        '''stateA'''
        #raw = raw_input('Enter a key:')
        if (opr == 0 or stateAC_i ==True):
            if (raw.isdigit()):
                if(stateAC_i == True):
                    a ='0'
                if(a =='0'):
                    a = raw
                else:
                    a = a+raw
                len_ = length - len(a)
            #decimal
            if (raw == '.'):
                if(a == '0'):
                    a = float(0)
                else:
                    a = a+raw               
            else:
                pass
            print('|'+len_*"_"+'{}|'.format(a),9)
            stateA_i = True    
        #stateB
        if ( raw =='+' or
             raw =='-' or 
             raw =='*' or 
             raw =='/'or
             raw =='='):
            #print(stateC)
            if(stateC_i == True or opr =='=' or stateS == True):
                if(opr =='=' and stateAC_i ==False):
                    print('|'+len_*"_"+'{}|'.format(a),10)
                else:
                    pass
                
                if (opr =='+'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ + b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),11)
                    b = '0'
                    stateR_i = True
                if (opr =='-'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ - b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),12)
                    b = '0'
                    stateR_i = True
                if (opr =='*'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ * b_,'.6f'))
                    a = isint(a)               
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),13)
                    b = '0'
                    stateR_i = True
                if (opr =='/'):
                    a_ = float(a)
                    b_ = float(b)
                    a = float(format(a_ / b_,'.6f'))
                    a = isint(a)
                    len_ = length - len(str(a))
                    print('|'+len_*"_"+'{}|'.format(a),14)
                    b = '0'
                    stateR_i = True          
            if(stateA_i == True or stateS == True):   
                opr = raw
                if(stateS == True):
                    print('|'+len_*"_"+'{}|'.format(a),15)
                #print('Operator!')
                #b = a
            #stateC 
        if (raw.isdigit() and opr!=0):
            if (stateAC_i==False):
                if(b =='0'):
                    b = raw
                else:
                    #if(len(str(b))==1):
                    #    b = str(b)+raw
                    if(len(str(b))>=1):
                        #b = float(b)
                        if(str(b)[-1]!='0'):
                            b = str(b)+raw
                        else:
                            if(str(b)[-1] == '0'):
                                b = str(b)+raw
                            else:
                                b = str(b)[:-1]+raw
                len_b = length - len(b)
                #if(b!='0' and raw =='0'):
                #    b = str(b)+raw
                print('|'+len_b*"_"+'{}|'.format(b),16)
        if (raw == '.' and opr !=0):
            if(b == '0'):
                b = str(float(0))[:-1]
            else:
                b = b+raw
            len_b = length - len(str(b))   
            print('|'+len_b*"_"+'{}|'.format(b),17)
        else:
            pass
        
        
          
        if(a!=0 and b!=0 and opr!=0):
            stateC_i = True
        if(a!='0' and b == '0' and raw == '='):
            stateAC_i = True
        else:
            stateAC_i = False    
                
        if (raw.upper() == 'R' and RPN == False):
    
            print('switch to RPN mode')
            b = opr = '0'
            RPN =True
            stateS = True
            print('|'+len_*"_"+'{}|'.format(a),18)
    if(raw.upper() != 'R'):
        stateS =False
    else:
        pass
    #print('num1:{},num2:{},opr:{},enter:{},RPN:{},stateS:{},stateA_r:{},stateB_r:{},stateC_i:{},stateR_i:{},stateA_i:{},stateAC_i:{}'.format(a,b,opr,enter,RPN,stateS,stateA_r,stateB_r,stateC_i,stateR_i,stateA_i,stateAC_i))