def calculateAreaofCircle(radius):
    from math import pi;
    area = pi * radius ** 2;
    return area;

def calculateMpg(miles, gallon):
    milesPergallon = miles / gallon;
    return milesPergallon;

def calculateFahrenheitTocelsuis(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9;
    return celsius;


def calculateDistancebetweenpoints(x,y,x1,y1):
    pointOne = x+y;
    pointTwo = x1+y1;
    distance = pointOne - pointTwo ;
    return distance;

