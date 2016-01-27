def main():
    t = raw_input("Enter time - HH:MM format\n").split(':')
    h = int(t[0])
    m = int(t[1])
    #print h, m
    angleh = 0
    anglem = 0
    if h<0 or m<0 or h>23 or m>59:
        print "invalid time"
        return
    if h<12:         #12 hr format
        angleh = (h*60+m)*0.5
    else:            #24 hr format
        angleh = ((h-12)*60+m)*0.5
    anglem = m*6
    print "angleh:", angleh
    print "anglem:", anglem
    angle = int(abs(angleh-anglem))
    if angle>180:
        angle=360-angle
    print "Angle between hour hand and minute hand at {0:s}:{1:s} is {2:3d} degrees".format(str(h).zfill(2), str(m).zfill(2), angle)

if __name__ == "__main__":
    main()
