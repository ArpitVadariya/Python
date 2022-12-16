def KelvinToFahrenheit(Temperature):
    assert (Temperature>=0),"Colder than absolute ZERO"
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(508.78))
print(KelvinToFahrenheit(-5))
