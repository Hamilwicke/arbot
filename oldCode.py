def normalize_reading():
    reading = None
    av_distance = []
    for i in range(1, 8):
        if reading is None:
            reading = self.get_distance(sensor)
        print "reading %s = %s" % (i, reading)
    else:
        reading2 = self.get_distance(sensor)
    if reading2 <= (reading * 3) or reading2 >= reading * .25:
        reading = reading2
    else:
        reading = None
    print "reading %s = %s" % (i, reading)
    if reading is not None:
        av_distance.append(reading)
        print av_distance
    if len(av_distance) > 1:
        return sum(av_distance) / float(len(av_distance))
    else:
        return None
