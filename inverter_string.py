def inverter_string(s):
    
    invertida = ''
    
    
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    
    return invertida


print(inverter_string("amor"))
print(inverter_string("Adiva"))
print(inverter_string("Sim, isso são palíndromos D:"))
