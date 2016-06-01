# convertDIST_ALL
#   This program converts Metric distance measures to American, or vice-versa
# Kevin Kredit
import string

def main():
    print "This program uses the input of one kind of distance measurement and"
    print "converts it to all other measurements of distance."
    print
    which = raw_input("Which distance value do you know? (ex. 'inch')   ")
    print
    which = which.lower()
    # Metric
    if which == "millimeter":
        milli = input("Input the distance in millimeters:   ")
        centi = milli / 10
        print 'Metric Conversions'
        print
        print "The distance in centimeters is:", centi, "centimeters."
        deci = milli / 100
	print "The distance in decimeters is:", deci, "decimeters."
	meter = milli / 1000
	print "The distance in meters is:", meter, "meters."
	deka = milli / 10000
	print "The distance in decameters is:", deka, "decameters."
	hecto = milli / 100000
	print "The distance in hectometers is:", hecto, "hectometers."
	kilo = milli / 1000000
	print "The distance in kilometers is:", kilo, "kilometers."	  

    if which == "centimeter":
        centi = input("Input the distance in centimeters:   ")
        milli = centi * 10
        print "The distance in millimeters is:", milli, "millimeters."
	deci = centi / 10
	print "The distance in decimeters is:", deci, "decimeters."
	meter = centi / 100
	print "The distance in meters is:", meter, "meters."
	deka = centi / 1000
	print "The distance in decameters is:", deka, "decameters."
	hecto = centi / 10000
	print "The distance in hectometers is:", hecto, "hectometers."
	kilo = centi / 100000
	print "The distance in kilometers is:", kilo, "kilometers."
	
    if which == "decimeter":
	deci = input("Input the distance in decimeters:   ")
        milli = deci * 100
        print "The distance in millimeters is:", milli, "millimeters."
	cenri = deci * 10
	print "The distance in centimeters is:", centi, "centimeters."
	meter = deci / 10
	print "The distance in meters is:", meter, "meters."
	deka = deci / 100
	print "The distance in decameters is:", deka, "decameters."
	hecto = deci / 1000
	print "The distance in hectometers is:", hecto, "hectometers."
	kilo = deci / 10000
	print "The distance in kilometers is:", kilo, "kilometers."

    if which == "meter":
	meter = input("Input the distance in meters:   ")
        milli = meter * 1000
        print "The distance in millimeters is:", milli, "millimeters."
	centi = meter * 100
	print "The distance in centimeters is:", centi, "centimeters."
	deci = meter * 10
	print "The distance in decimeters is:", deci, "decimeters."
	deka = meter / 10
	print "The distance in decameters is:", deka, "decameters."
	hecto = meter / 100
	print "The distance in hectometers is:", hecto, "hectometers."
	kilo = meter / 1000
	print "The distance in kilometers is:", kilo, "kilometers."	  
main()
                 
