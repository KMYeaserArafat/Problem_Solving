
# Physical-Energy
"""
Initially you have H amount of energy and D distance to travel. You may travel with any of the given 5 speeds. 
But you may only travel in units of 1 km. For each km distance traveled, you will spend corresponding amount of energy.e.g. the given speeds are:

Cost of traveling 1 km (Per KM Speed): [4, 5, 2, 3, 6]  
Time taken to travel 1 km (Per Km time): [200, 210, 230, 235, 215]

Find minimum time required to cover total D km with remaining H >= 0

1 <= H <= 4000
1 <= D <= 1000

"""
def MinTimeRequired():
    time = []
    for i in range(len(per_Km_Speed)):
        for j in range(len(per_km_time)):
            if H>=per_Km_Speed[i] and D<=per_km_time[j]:
                calculation = per_km_time[i]*per_Km_Speed[j]
                time.append(calculation)

    return min(time)
            



H = int(input("Enter the initial Energy (H)   : "))
D = int(input("Enter the initial Distance (D) : "))
per_Km_Speed = [4,5,2,3,6]
per_km_time = [200,210,230,235,215]

if(H>=1 and H<=4000 and D>=1 and D<=1000):
    print(MinTimeRequired())
else:
    print("H or D is Invalid!")