def convertercelsiusParaFahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * 9/5 + 32
    return temp_fahrenheit

def main():
    temp_celsius = 30
    temp_fahrenheit = convertercelsiusParaFahrenheit(temp_celsius)
    print(temp_fahrenheit)

main()