from datetime import datetime

def despertador(h1, m1, s1, s2):
    data1 = datetime.now()


    if (data1.hour == h1 and data1.minute == m1 and data1.second >= 0 and data1.second <= 15):
        return True
    
    else:
        return False

