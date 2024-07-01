def celsius_to_fahrenheit(celsius):
    return celsius* 9/5+32;

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_Celsius(fahrenheit):
    return (fahrenheit -32)* 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32)* 5/9+273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin -273.15) *9/5 +32

def main():
    temperature=float(input('Enter the temperature value:'))
    unit=input('Enter the unit of measurement (celsius,fahrenheit,kelvin):').lower()

    if unit=='celsius':
        fahrenheit=celsius_to_fahrenheit(temperature)
        kelvin=celsius_to_kelvin(temperature)
        print(f'{temperature} Celsius is {fahrenheit} Fahrenheit and {kelvin} Kelvin')
    
    elif unit=='fahrenheit':
        celsius=fahrenheit_to_Celsius(temperature)
        kelvin=fahrenheit_to_kelvin(temperature)
        print(f'{temperature} Fahrenheit is {celsius} Celsius and {kelvin} Kelvin')

    elif unit=='kelvin':
        celsius=kelvin_to_celsius(temperature)
        fahrenheit=kelvin_to_fahrenheit(temperature)
        print(f'{temperature} Kelvin is {celsius} Celsius and {fahrenheit} Fahrenheit')
    
    else:
        print('Invalid unit of measurement')

if __name__ == '__main__':
    main()