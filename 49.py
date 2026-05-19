from datetime import datetime,timedelta

cities=["San Fransisco","New York","London","Dubai","Bangalore","Singapore","Tokyo","Sydney","Wellington"]
offsets=[-7,-4,1,4,5.5,8,9,10,12]
utc_time=datetime.utcnow()

for i in range(0,len(cities),1):
    hours=int(offsets[i])
    minutes=int((offsets[i]-hours)*60)
    local_time=utc_time+timedelta(hours=hours,minutes=minutes)
    print(cities[i],":",local_time.strftime("%H:%M:%S"))
