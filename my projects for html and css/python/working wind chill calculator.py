#welcome to my wind chill calculator for creativity I changed the colours of the texts
print("\033[35m" , end = " " )
print("HELLO AND WELCOME TO MY WIND CHILL CALCULATOR ")
print("\033[33m" , end = " " )
print('=' * 65, 'WIND CHILL CALCULATOR', '=' * 14)
print("\033[31m" , end = " " )
print('🌧️' * 65, 'THIS PROGRAM GENERATES THE TEMPERATURE AND THE VELOCITY OF THE WIND FOR YOU\nDONT USE THE WEATHER FORECAST ANYMORE, WE GAT YOU', '🌧️' * 10)
value = float(input('What is the temperature? '))
wind = -1
conversion = 9 * value / 5 + 32
degree = input("Fahrenheit or Celsius (F/C)? ")
print()


def C_to_F(temp):
    formula = 9 * temp / 5 + 32
    formula2 = 35.74 + (0.6215 * formula) - 35.75 * (wind ** 0.16) + (0.4275 * formula) * (wind ** 0.16)
    return formula2
    
def wind_chill():
    formula3 = 35.74 + (0.6215 * value) - 35.75 * (wind ** 0.16) + (0.4275 * value) * (wind ** 0.16)
    return formula3


for wind in range(5, 61, 5):
    if degree.lower() == 'c':
        result = C_to_F(value)
        print(f'The temperature {value:.1f} C° is equal to {conversion:.1f} F°, '
              f'and wind speed {wind} mph. The wind chill is: {result:.2f} F°')
    elif degree.lower() == 'f':
        result = wind_chill()
        print(f'The temperature {value:.1f} F° is equal to {conversion:.1f} C°, '
              f'and wind speed {wind} mph. The wind chill is: {result:.2f} F°')

print()
print("\033[33m" , end = " " )
print('=' * 65, 'JOY OF THE DAY', '=' * 18)