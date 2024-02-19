def add_time(start, duration, day=None):
    start = start.replace(':', ' ').split()
    duration = duration.split(':')
    newTime = []
    days = 0
    
    # converting start to 24-hrs format
    if start[2]=='AM' and start[0]=='12':
        start[0] = '00'
    elif start[2]=='PM' and start[0]!='12':
        start[0] = str(int(start[0]) + 12)
        
    # adding duration to start
    newTime.append(int(start[0]) + int(duration[0]))
    newTime.append(int(start[1]) + int(duration[1]))

    # calculating days and new time
    newTime[0] += newTime[1] // 60
    newTime[1] = newTime[1] % 60
    days = newTime[0] // 24
    newTime[0] = newTime[0] % 24

    # converting newTime to 12-hrs format
    if newTime[0] < 12:
        newTime.append('AM')
    else:
        newTime.append('PM')
    newTime[0] %= 12
    if newTime[0] == 0:
        newTime[0] = 12
        
    # formatting newTime
    newTime[0] = str(newTime[0])
    newTime[1] = str(newTime[1]) if newTime[1] > 10 else '0'+str(newTime[1])
    newTime = newTime[0]+':'+newTime[1]+' '+newTime[2]

    if(day == None):
        if days == 0:
            return newTime
        elif days == 1:
            return newTime + ' (next day)'
        else:
            return newTime + ' ('+str(days)+' days later)'
    else:
        d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = day.lower().capitalize()
        day = d[(d.index(day)+days)%7]
        if days == 0:
            return newTime + ', ' + day
        elif days == 1:
            return newTime + ', ' + day + ' (next day)'
        else:
            return newTime + ', ' + day + ' ('+str(days)+' days later)'
