from sleeperpy import Players, Leagues
import pandas as pd
from pandas import json_normalize 
import pickle
import os
from sydney import SydneyClient
import asyncio
league_id = os.getenv("LEAGUE_ID")
league_id = 1049034345945649152


# https://docs.sleeper.com/#fetch-all-players


# player_df = json_normalize(player_data)
# print(player_df.head())
# player_df.to_csv("test.csv", index=False)

# rosters = Leagues.get_rosters(league_id)
# print(rosters)

num_players_to_get = 10
# 1 through 168
hours = 48

# create df to store data in


print(f"Top {num_players_to_get} Adds in last {hours} hours:")
with open('player_data.pkl', 'rb') as f:
    player_data = pickle.load(f) # deserialize using load()
    for i in range(0,num_players_to_get):
        trending_adds = Players.get_trending_players(sport="nfl", type="add", hours=hours, limit=num_players_to_get)
        player_id = trending_adds[i]["player_id"]
        count = trending_adds[i]["count"]
        first_name = player_data[player_id]["first_name"]
        last_name = player_data[player_id]["last_name"]
        fantasy_positions = player_data[player_id]["fantasy_positions"]
        team = player_data[player_id]["team"]
        # get player position
        try:
            position = fantasy_positions[0]
        except:
            if len(fantasy_positions)==3:
                position = f"{fantasy_positions[0]}/{fantasy_positions[1]}/{fantasy_positions[2]}"
            elif len(fantasy_positions)==2:
                position = f"{fantasy_positions[0]}/{fantasy_positions[1]}"
            else:
                position = "UNK"

        # parse player data
        print(f"{i+1}. {first_name} {last_name} ({position}, {team}) {count}")

        # https://github.com/vsakkas/sydney.py

        cookie = "SRCHHPGUSR=SRCHLANG=en&BRW=W&BRH=S&CW=1470&CH=398&SCW=1470&SCH=398&DPR=2.0&UTC=-480&DM=1&CIBV=1.1514.2&HV=1706242239&PRVCW=1470&PRVCH=745&CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF; MUIDB=0A013B01BFB46E1F135F2F13BE0E6FBF; _RwBf=r=0&ilt=3&ihpd=3&ispd=0&rc=0&rb=0&gb=0&rg=200&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=3&l=2024-01-25T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0001-01-01T00:00:00.0000000&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2024-01-26T04:10:34.8255035+00:00&rwred=0&wls=&wlb=&wle=&ccp=&lka=0&lkt=0&aad=0&TH=; _Rwho=u=d; _SS=SID=3031FBB6452E680F26F4EFA4449469B6&R=0&RB=0&GB=0&RG=200&RP=0; BFBUSR=CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF; MUID=0A013B01BFB46E1F135F2F13BE0E6FBF; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=D4D0AEECCE674B7292A145F3B950E1F0&dmnchg=1; SRCHUSR=DOB=20240126; _EDGE_S=F=1&SID=3031FBB6452E680F26F4EFA4449469B6; _EDGE_V=1"

        os.environ["BING_COOKIES"] = cookie

        async def main() -> None:
            async with SydneyClient() as sydney:
                prompt = f"You are a highly-detailed, data-driven fantasy football analyst with 10 years of experience. Provide analysis on why {first_name} {last_name} ({position}, {team}) is a trending pickup on fantasy platforms during the last {hours} hours. Provide 3 concise reasons why it would be a good idea to follow the crowd and add him to my team and 3 concise reasons why this could be a false alarm and why I should not add him to my team. Only reference information from news from within 7 days of January 25th, 2024. This means you cannot reference any information from before January 18th, 2024. Make sure you ONLY reference information from the last 7 days, because it is likely that recent news is what triggered this adding spree."
                response = await sydney.ask(prompt, citations=True)
                print(response)
                print()
        if __name__ == "__main__":
            asyncio.run(main())

print()





# print()
# print("Top 100 Drops:")
# with open('player_data.pkl', 'rb') as f:
#     player_data = pickle.load(f) # deserialize using load()
#     for i in range(0,num_players_to_get):
#         # 168 is max hours
#         trending_drops = Players.get_trending_players(sport="nfl", type="drop", hours=hours, limit=num_players_to_get)
#         negative_trending_player = trending_drops[i]["player_id"]
#         negative_trending_player_drop_amount = trending_drops[i]["count"]

#         # parse player data
#         print(f"{i+1}. "+player_data[negative_trending_player]["first_name"]+" "+player_data[negative_trending_player]["last_name"]+" ("+player_data[negative_trending_player]["fantasy_positions"][0]+", "+player_data[negative_trending_player]["team"]+") "+f"({negative_trending_player_drop_amount})")