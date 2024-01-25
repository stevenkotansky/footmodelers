from sleeperpy import Players, Leagues
import pandas as pd
from pandas import json_normalize 
import pickle
import os
league_id = os.getenv("LEAGUE_ID")
league_id = 1049034345945649152

# Get all players
all_players = Players.get_all_players()

# save player data to pkl file
with open('player_data.pkl', 'wb') as f:  # open a text file
    pickle.dump(all_players, f) # serialize the player data
f.close()