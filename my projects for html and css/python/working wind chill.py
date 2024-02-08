#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
print('='*65, 'WIND CHILL','='*18) 
value = float(input('What is the temperature? '))
wind = -1
conversion = formula = 9 * value / 5 + 32
degree = input("Fahrenheit or Celsius (F/C)? ")
print()
def C_to_F():
    formula = 9 * value / 5 + 32
    temp = formula
    formula2 = 35.74 + (0.6215 * temp) - 35.75 * (wind ** 0.16) + (0.4275 * temp) *(wind ** 0.16)
    return formula2
    def wind_chill():
        formular3 = 35.74 + (0.6215 * value) - 35.75 * (wind ** 0.16) + (0.4275 *value) * (wind ** 0.16) 
    return formula3 
for wind in range (5,61,5): 
    if degree.lower() == 'c':
        result = C_to_F() 
        print (f'The temperature {value:.0f} C°, is equal to {conversion} F° and wind speed {wind}(mph), the windchill is: {result:.0f} F°') 
    if degree.lower() == 'f': 
            total = wind_chill() 
            print (f'At temperature {value:.0f} F°, and wind speed {wind}(mph), the windchill is: {total:.0f} F°') 
            print() 
            print('='*65, 'JOY THE DAY ', '='*18) 