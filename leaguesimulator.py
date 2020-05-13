import numpy as np
import os

file = os.path.join("ChampionData.csv")
data = np.genfromtxt(file,names="Champion, Role, Rank, WinPercent,	PlayPercent, BanRate,	PlayerbaseAvg.Games, Kills, Deaths, Assists, LargestKillingSpree, DamageDealt,	DamageTaken, TotalHealing, MinionsKilled, EnemyJungleCS, TeamJungleCS, GoldEarned, RolePosition, PositionChange", delimiter=",", skip_header=1,usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))
data = np.asarray(data)

champnames = np.genfromtxt(file,dtype=str, delimiter=",",usecols=(0,1),skip_header=1)
np.asarray(champnames)

myteam = input("Enter the names of your champions (including spaces and capitals) separated by commas (Ex: Talon,Miss Fortune,Darius...):")
myteam = myteam.split(',')

if len(myteam) is not 5:
    raise Exception("This is not the correct number of champions.")

print(myteam)

def data_extraction(locusnumber):
    print(data[locusnumber])

def find_location(team):
    for champion in range(len(myteam)):
        location = np.where(champnames == team[champion])
        print(champnames[location])
        locusnumber = location[0]
        data_extraction(locusnumber)

enemyteam = input("Enter the names of the enemy champions (including spaces and capitals) separated by commas (Ex: Talon,Miss Fortune,Darius...):")
enemyteam = enemyteam.split(',')

find_location(myteam)
find_location(enemyteam)
