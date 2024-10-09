import matplotlib.pyplot as plt
import math

#declination angle: Angle of the Solary array from the ground
def calculate_declination_angle(n):
    return 23.45 * math.sin(((360 / 365) * (284 + n)) * (180/math.pi))

#Solar Hour Angle: distance between the sun at the solar noon and the local solar time
def calculate_solar_hour_angle(LST):
    return (LST - 12) * 15 

#Solar Altitude Angle: angular posiiton of the sun above the horizon
def calculate_solar_altitude_angle(delta, lat, h):
    return (180/math.pi) * math.asin(math.sin(delta*(math.pi/180)) * math.sin(lat*(math.pi/180)) + 
                     math.cos(lat*(math.pi/180)) * math.cos(delta*(math.pi/180)) * math.cos(h*(math.pi/180)))

#Solar Azimuth Angle: Angle between projection axis and due North. Measured on a horizontal plane
def calculate_solar_azimuth_angle(delta, h, alpha):
    return (180/math.pi) * math.asin((math.cos(delta * (math.pi / 180)) * math.sin(h * (math.pi / 180)))/(math.cos(alpha * (math.pi / 180))));

#Time Duration of Day: Length of the sunlight hours
def calculate_time_duration_of_day(lat, delta):
    return 0.1333333333 * (180/math.pi) * math.acos(-1.0 * math.tan(lat*(math.pi/180)) * math.tan(delta*(math.pi/180)))

def calculate_sunrise_hour(l):
    sunrise_hour = 12 - (l/2)
    return float_to_time(sunrise_hour)


def calculate_sunset_hour(l):
    sunrise_hour = 12 + (l/2)
    return float_to_time(sunrise_hour)

#Time conversion
def float_to_time(time_float):

    hours = int(time_float)  

    minutes = int((time_float - hours) * 60) 

    seconds = int(((time_float - hours) * 60 - minutes) * 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"

lat = -0.88035
day = []
time_duration = []


#Day vs Day Length Graph
for i in range (151,243):
    dec_angle = calculate_declination_angle(i)
    day.append(i)
    time_duration.append(calculate_time_duration_of_day(lat, dec_angle))
    
plt.plot(day,time_duration)

plt.xlabel('Day in the year')
plt.ylabel('Calculate Day Length')


