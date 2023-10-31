"""
8.	Monthly rainfall data of 1970 of different station is given.
    Data column as follows: Year StationName Month rainfall stationID. 
    Use a Rainfall class with data member: 
     year, stationName, month, rainfall, stationID and write a function to find average rainfall of Chittagong in 1970. 
"""

class Rainfall:
    
    def __init__(self,year,stationName,month,rainfall,stationId) -> None:
        self.year = year
        self.stationName = stationName
        self.month = month
        self.rainfall = rainfall
        stationId = stationId



RainfallData = [Rainfall(1970,"Jhenidah","January",5,1),
                Rainfall(1970,"Jhenidah","February",6,1),
                Rainfall(1970,"Jhenidah","March",10,1),
                Rainfall(1970,"Jessore","January",7,4),
                Rainfall(1970,"Jessore","Frbruary",5,4),
                Rainfall(1970,"Jessore","March",5,4),
                Rainfall(1970,"Dhaka","November",21,14),
                Rainfall(1970,"Dhaka","November",20,15),
                Rainfall(1970, "Chittagong", "January", 15.2, 1),
                Rainfall(1970, "Chittagong", "February", 14.5, 1),
                ]


def Cittagong_avg_rainfall_1970(data,location):
    total_rainfall = 0
    count = 0

    for x in data:
        if x.year == 1970 and x.stationName == location:
            total_rainfall += x.rainfall
            count +=1

    
    if count>0:
        avg = total_rainfall/count
        return avg
    else:
        return 0
    


c_Avg_rainfall_1970 = Cittagong_avg_rainfall_1970(RainfallData,"Chittagong")
print("The Average rainfall of Chittagong in 1970 : ", c_Avg_rainfall_1970)
