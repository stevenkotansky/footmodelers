from sleeperpy import Players, Leagues
import pandas as pd
from pandas import json_normalize 
import pickle
import os
league_id = os.getenv("LEAGUE_ID")
league_id = 1049034345945649152


# https://docs.sleeper.com/#fetch-all-players


# player_df = json_normalize(player_data)
# print(player_df.head())
# player_df.to_csv("test.csv", index=False)

# rosters = Leagues.get_rosters(league_id)
# print(rosters)

num_players_to_get = 10
hours = 1

print("Top 100 Adds:")
with open('player_data.pkl', 'rb') as f:
    player_data = pickle.load(f) # deserialize using load()
    for i in range(0,num_players_to_get):
        # 168 is max hours
        trending_adds = Players.get_trending_players(sport="nfl", type="add", hours=hours, limit=num_players_to_get)
        top_trending_player = trending_adds[i]["player_id"]
        top_trending_player_add_amount = trending_adds[i]["count"]
    
        try:
            top_trending_player_team_name = player_data[top_trending_player]["team"]
        except:
            top_trending_player_team_name = "N/A"

        # parse player data
        print(f"{i+1}. "+player_data[top_trending_player]["first_name"]+" "+player_data[top_trending_player]["last_name"]+" ("+player_data[top_trending_player]["fantasy_positions"][0]+", "+top_trending_player_team_name+") "+f"({top_trending_player_add_amount})") # print player data
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