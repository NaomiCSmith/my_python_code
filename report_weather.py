# report_weather

# Create a weather reporting function that takes another function as its argument

def report_weather(temperature, function):
    return function(temperature)

def as_sun_lover(temperature):
    if temperature >= 25:
        return("Great")
    else:
        return("Not Great")

def as_snow_lover(temperature):
    if temperature <= 0:
        return("Great")
    else:
        return("Not Great")

sun_lover_report = report_weather(-1, as_sun_lover)
snow_lover_report = report_weather(-1, as_snow_lover)

print(f"Sun Lover's Report: {sun_lover_report}")
print(f"Snow Lover's Report: {snow_lover_report}")
