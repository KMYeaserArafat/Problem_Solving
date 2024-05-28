/*
# Problem Solving Task in JS : 
---------------------------------------------
Problem 1: Make a convertor feetToMile


Problem 2: woodCalculator, Here we assume for making a chair we need 1 cc wood, table 2 cc wood, bed 5 cc wood, 
Now task is care oder from user and calculate how much total wood actually need this customer


Problem 3: brickCalculator, take one input how much tall of your building. 
we assume here 1-10 floor tall building 15 feet, 10-20 floor tall building 20 feet, 20-40 floor tall building 25 feet, 
Per feet we need 5000 Pes bricks, Now calculate the total needed bricks for this building.


Problem 4: tinyFriend, take n number of friends, take friends name and find out the min length of friend name

*/

function feetToMile(n) {
   var feet = n;
   var mile = feet * 0.0001894;
   return mile;
}


function woodCalculator(numOfChair,numOfTable,numOfBed){
    forMakingChairWood = 1;
    forMakingTableWood = 2;
    forMakingBedWood = 5; 

    useChairWood = numOfChair*forMakingChairWood;
    useTableWood = numOfTable*forMakingTableWood;
    useBedWood = numOfBed*forMakingBedWood;

    totalUsedWood = useChairWood+useTableWood+useBedWood;
    return totalUsedWood;
}

function brickCalculator(buildingHeight){
    perFeetNeedBricks = 5000

    if(buildingHeight>=1 && buildingHeight<=10){
        feet = 15;
        totalBricks = perFeetNeedBricks*feet; 
        return totalBricks;
    }else if(buildingHeight>=11 && buildingHeight<=20){
        feet = 20;
        totalBricks = perFeetNeedBricks*feet; 
        return totalBricks;
    }else if(buildingHeight>=21 && buildingHeight<=40){
        feet = 25; 
        totalBricks = perFeetNeedBricks*feet; 
        return totalBricks;
    }else{
        return 0;
    }

}

function tinyFriend(friendsName){
    
    minLenghtName = friendsName[0].length;
    friendName = friendsName[0];

    for(var i=1; i<friendsName.length; i++){
       if(minLenghtName>friendsName[i].length){
        minLenghtName = friendsName[i].length;  // for knowing about length, 
        friendName = friendName[i];
       }
       return friendName;
    }
}


console.log(feetToMile(1000));  // 1000 feet to convert for miles
console.log(woodCalculator(6,3,4))  // 6 Chairs, 3 Tables, 4 Bed
console.log(brickCalculator(21))  // 21 floor building needed bricks 1,25,000 number of bricks,
friendsName = ["Anis", "Shofik", "Tarek", "Alis"];
console.log(tinyFriend(friendsName))






