#Kelvin = float(input("Ketikkan angka suhu Kelvin:"))
#Celcius = Kelvin - 273
#print(f"{Kelvin} adalah sama dengan {Celcius} pada Celcius")

def konversi(mode, suhu):
    if mode == "celcius ke kelvin":
        kelvin = suhu + 273
        return kelvin
    if mode == "kelvin ke celcius":
        celcius = suhu - 273
        return celcius

#def konversi_kelvin_ke_celcius(kelvin):
#    celcius = kelvin - 273
#    return celcius
#print(konversi_kelvin_ke_celcius(340))

#def konversi_celcius_ke_kelvin(celcius):
#    kelvin = celcius + 273
#    return kelvin
#print(konversi_celcius_ke_kelvin(37))

def convert_ke_fahrenheit(mode, suhu):
    if mode == "celcius":
        Celcius = suhu * 9/5 + 32
        return Celcius
    if mode == "kelvin":
        Kelvin = (suhu - 273) * 9/5 + 32
        return Kelvin


print(konversi("celcius ke kelvin", 37))
print(konversi("kelvin ke celcius", 344))
print(convert_ke_fahrenheit("celcius", 35))
print(convert_ke_fahrenheit("kelvin", 355))







