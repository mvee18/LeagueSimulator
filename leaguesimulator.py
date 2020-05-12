import numpy as np
import os

file = os.path.join("ChampionData.csv")
data = np.genfromtxt(file,names="Champion,	Role,	Rank,	Win Percent,	Play Percent,	Ban Rate,	Playerbase Avg. Games, Kills, Deaths,	Assists, Largest Killing Spree,	Damage Dealt,	Damage Taken,	Total Healing, Minions Killed, Enemy Jungle CS, Team Jungle CS, Gold Earned, Role Position, Position Change", delimiter=",", skip_header=1,usecols=(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))
data = np.asarray(data)

championames = np.genfromtxt(file,dtype=str, delimiter=",",usecols=(0,1),skip_header=1)
np.asarray(championames)

print(championames)
print(data["Champion"])
