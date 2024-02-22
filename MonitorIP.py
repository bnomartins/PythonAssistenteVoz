

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
from MonitorTemperatura import verificar_temperatura
import webbrowser

gyn = 0       

rv=0
mrv=0

cr=0
mcr=0

ct=0
mct=0

jt=0
mjt=0

rg=0
form=0
ipora=0
por=0
quir=0
g8=0
tel=0

cont = 15
rein = 17

def verificar_ip(ip, name):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip]

    resp = subprocess.call(command, shell=False) == 0
    print(f'Verificando servidor --------------> {name} - {resp}')
                
    if name == 'Hemovida de Goiânia':
        if (resp == False):
            global gyn
            gyn=gyn+1
            if (gyn > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(gyn > rein): 
                    gyn=0
        else:
            gyn=0         
            print(f'----------------------------------------------------------{name}---{gyn}')   

    if name == 'MPLS de Rio Verde':
        if(resp == False):
            global mrv
            mrv=mrv+1
            if (mrv > cont):
                # speak.say(f"{name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
                time.sleep(2)
                if(mrv > rein): 
                    mrv=0
            print(f'----------------------------------------------------------{name}---{mrv}')   
        else:
            mrv=0                     

    if name == 'Hemovida de Rio Verde':
        if(resp == False):
            global rv
            rv=rv+1
            if (rv > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()   
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
#  
                time.sleep(2)
                if(rv > rein): 
                    rv=0
            print(f'----------------------------------------------------------{name}---{rv}')   
        else:
            rv=0                     
        
    if name == 'MPLS de ceres':
        if (resp == False):
            global mcr
            mcr=mcr+1
            if (mcr > cont):
                # speak.say(f"{name} está inacessível")
                # speak.runAndWait() 
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
#    
                time.sleep(2)
                if(mcr > rein): 
                    mcr=0
            print(f'-----------------------------------------------------------{name}---{mcr}')    
        else:
            mcr=0        
        
    if name == 'Hemovida de ceres':
        if (resp == False):
            global cr
            cr=cr+1
            if (cr > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()  
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
#   
                time.sleep(2)
                if(cr > rein): 
                    cr=0
            print(f'-----------------------------------------------------------{name}---{cr}')    
        else:
            cr=0        
      
    if name == 'MPLS de Catalão':
        if(resp == False):
            global mct
            mct=mct+1
            if (mct > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()  
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
   
                time.sleep(2)
                if(mct > rein): 
                    mct=0
            print(f'-----------------------------------------------------------{name}---{mct}')     
        else:
            mct=0       
      
    if name == 'Hemovida de Catalão':
        if(resp == False):
            global ct
            ct=ct+1
            if (ct > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(ct > rein): 
                    ct=0
            print(f'-----------------------------------------------------------{name}---{ct}')     
        else:
            ct=0       
        
         
    if name == 'MPLS de jataí':
        if(resp == False):
            global mjt
            mjt=mjt+1
            if (mjt > cont):
                # speak.say(f"{name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
                time.sleep(2)
                if(mjt > rein): 
                    mjt=0
            print(f'-----------------------------------------------------------{name}---{mjt}')    
        else:
            gyn=0        
         
    if name == 'Hemovida de jataí':
        if(resp == False):
            global jt
            jt=jt+1
            if (jt > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(jt > rein): 
                    jt=0
            print(f'-----------------------------------------------------------{name}---{jt}')    
        else:
            gyn=0        
            
    if name == 'MPLS das Regionais':
        if(resp == False):
            global rg
            rg=rg+1
            if (rg > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(rg > rein): 
                    rg=0
            print(f'------------------------------------------------------------{name}---{rg}')    
        else:
            rg=0        
               
    if name == 'MPLS de Formosa':
        if(resp == False):
            global form
            form=form+1
            if (form > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()  
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')
#   
                time.sleep(2)
                if(form > rein): 
                    form=0
            print(f'-----------------------------------------------------------{name}---{form}')   
        else:
            form=0         
          
    if name == 'MPLS de Iporá':
        if(resp == False):
            global ipora
            ipora=ipora+1
            if (ipora > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(ipora > rein): 
                    ipora=0
            print(f'------------------------------------------------------------{name}---{ipora}')  
        else:
            ipora=0          
          
    if name == 'MPLS de Porangatu':
        if(resp == False):
            global por
            por=por+1
            if (por > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(por > rein): 
                    por=0
            print(f'------------------------------------------------------------{name}---{por}')   
        else:
            por=0         

    if name == 'MPLS de Quirinópolis':
        if resp == False:
            global quir
            quir=quir+1
            if (quir > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(quir > rein): 
                    quir=0
            print(f'--------------------------------------------------------------{name}---{quir}')   
        else:
            quir=0         
        
    if name == 'de telefonia':
        if resp == False:
            global tel
            tel=tel+1
            if (tel > cont):
                # speak.say(f"Servidor {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(tel > rein): 
                    tel=0
            print(f'-------------------------------------------------------------{name}---{tel}')  
        else:
            tel=0          
        
    if name == 'G8':
        if resp == False:
            global g8
            g8=g8+1
            if (g8 > cont):
                # speak.say(f"Conexão {name} está inacessível")
                # speak.runAndWait()    
                webbrowser.open(f'https://seusiteaqui.com {name} está inacessível/')

                time.sleep(2)
                if(g8 > rein): 
                    g8=0
            print(f'-------------------------------------------------------------{name}---{g8}')  
        else:
            g8=0          


# speak.say(f"Monitoramento ativado")
# speak.runAndWait()   


cont_temperatura = 0
cont_humidade = 0
ini = 0

while True:
    temp = verificar_temperatura()[0]
    hum = verificar_temperatura()[1]

    if ini == 0:
        webbrowser.open(f'https://seusiteaqui.com//Monitoramento da rede hemo está ativado/')
        ini = ini+1


    # Monitoramento de temperatura
    if float(temp) > float(21.9):
        # monitor = verificar_temperatura()
        # speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
        # speak.say("ATENÇÃO: RISCO DE COLAPSO DO DATACENTER")
        # speak.say(f"A Temperatura da sala está em {temp} graus celsius")
        # speak.runAndWait()  
        
        if(cont_temperatura > 5 and cont_temperatura < 7):
            webbrowser.open(f'https://seusiteaqui.com//Atenção o datacenter está com a climatização inadequada com a temperatura em {temp} graus celsius/')
        cont_temperatura=cont_temperatura+1
        

        if(cont_temperatura > 50):
            cont_temperatura = 0

    # Monitoramento de umidade
    if float(hum) > float(60.0):
        # monitor = verificar_temperatura()
        # speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
        # speak.say("ATENÇÃO: RISCO DE COLAPSO DO DATACENTER")
        # speak.say(f"A Umidade da sala está em {hum} por cento")
        # speak.runAndWait()  

        if(cont_humidade > 5 and cont_humidade < 7):
            webbrowser.open(f'https://seusiteaqui.com//Atenção o datacenter está com a climatização inadequada com a humidade relativa do ar em {hum} por cento/')
        cont_humidade=cont_humidade+1

        if( cont_humidade > 50):
            cont_humidade = 0        




    verificar_ip('102.109.83.2','nome do servidor')

    verificar_ip('102.109.52.1','nome do servidor')
    verificar_ip('102.109.52.11','nome do servidor')

    verificar_ip('102.109.108.1','nome do servidor')
    verificar_ip('102.109.108.2','nome do servidor')

    verificar_ip('102.109.48.252','nome do servidor')
    verificar_ip('102.109.48.250','nome do servidor')

    # verificar_ip('172.16.4.2','nome do servidor')
    verificar_ip('102.109.109.1','nome do servidor')
    verificar_ip('102.109.109.11','nome do servidor')

    verificar_ip('102.109.83.252','nome do servidor')
    verificar_ip('102.109.85.1','nome do servidor')
    verificar_ip('102.109.88.1','nome do servidor')
    verificar_ip('102.109.109.11','nome do servidor')
    verificar_ip('102.109.90.1','nome do servidor')
    verificar_ip('107.109.46.73','nome do servidor')
    
    # verificar_ip('192.168.10.10','de telefonia')
    verificar_ip('107.109.10.10','de telefonia')
    time.sleep(3)

    print (f""" gyn = {gyn}       
        mrv={mrv}
        mcr={mcr}
        mct={mct}
        mjt={mjt}
        rg={rg}
        form={form}
        ipora={ipora}
        por={por}
        quir={quir}
        g8={g8}
        tel={tel}
        temp={cont_temperatura} - t{temp}ºc
        hum={cont_humidade} - m{hum}%
        """)

