T=int(input("Enter any temperature:  "))

D=str(input(" Temperature Convert From: "))

def temp (T,D):
 if D=='c' :
    fah= T *(9/5)+32
    print("In fahrenheit= "+ str(round(fah,2)) ) 
    kelvin=(T+273)
    print("In KELVIN= "+  str(round(kelvin,2))) 
 elif D== 'f':
    celcius = int(( T-32)*(5/9))
    print("In celcius = "+ str(round(celcius,2))) 
    kelvin = (T-32)*(5/9)+273
    print("In KELVIN = " + str(round(kelvin,2)) ) 
 elif D=='k':
    celcius= T-273
    print("In celcius = "+ str(round(celcius,2)) )
    fah=(T-32)*(5/9)+273
    print ("In fahrenheit= "+ str(round(fah,2)))  
    
temp(T,D)
  
  
    
    
    