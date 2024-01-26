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

        cookie = "SRCHHPGUSR=SRCHLANG=en&BRW=W&BRH=S&CW=1470&CH=398&SCW=1470&SCH=398&DPR=2.0&UTC=-480&DM=1&CIBV=1.1514.2&HV=1706244017&PRVCW=1470&PRVCH=398&CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF&copucnt=1; MUIDB=0A013B01BFB46E1F135F2F13BE0E6FBF; SnrOvr=X=rebateson; _RwBf=r=1&ilt=3&ihpd=3&ispd=0&rc=640&rb=640&gb=0&rg=9500&pc=0&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=4&l=2024-01-25T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2022-10-07T16:51:43.4816133-07:00&o=0&p=XBOXMIGRATION_0STAR&c=raw_mtrial&t=9196&s=2015-09-24T22:53:54.0000000+00:00&ts=2024-01-26T04:40:12.7982044+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=vJds9zfYc0OHFu1a6Y4Y5M0aVVs-TUCuBrZYJ207J3zUTUoY8cTiIE_sh-w6mjwppaGZAjE7DmR95s8fCZ2VAn4YnAnMYP_eqFWrV93kr4w&A=D6C6FC5C94635052AB5F36E9FFFFFFFF; _Rwho=u=d; _SS=SID=3031FBB6452E680F26F4EFA4449469B6&R=640&RB=640&GB=0&RG=9500&RP=0; ANON=A=D6C6FC5C94635052AB5F36E9FFFFFFFF&E=1d56&W=1; KievRPSSecAuth=FAB6BBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACGN4mzdYcqlJOAQ3epPy+kOKoXqc22ns9XDy3LyJxF01t2WjMxS8cbiV6oY+IHiBlw8oq8qrb6QPnWzyL+S9GoC63zxzMDt5hZ4n/gMOL2dRQG1wS+wGaD9EgdxbLGh2CMbmAATmqOpMm+HTscGxgQOOCtxvM7OUY2S24nr6EQzn/fqM2+ozbUSy09YxvXp6/krcWFe0Cfw6rf70PQWDJF+unJkpV3PZdApsyi14u6b4Ijs4QwqG9ACfoptwU2+aYcpRdQbDf5ZOMRfeuJgOujakoiqYyp+1wLSBzQ0Y/BwMyewvjt5GYLWSLppArVfgiZbaXK04CYzDQLjy7XW6V4cTVKlrp8YlkdRvV3hOczuuJ4cmuYz/tER8UzAh+6vkYndy0GvMUS0axG7BvxPCXMdzzo87PgAKg0XGwdx/1bGPePLhr/CnAVrOz24MrW2Z61p0gX68XwOUBKMJco4nIzVN6yTLsahPHXqn5zwTp/uQyDjXhtyfNQsPMmWnBhgrdjzzkEf5NMK+cIFcD8fkUzbijZ2ktX6Mzjsch5+fXZDk3Sg/k0lHGo/HogiGmTsmxiP7Pg+4lu6pJwJyzZdCVSsi3RhNYNQYVaunkYQU70LL/XkNRqV3tT+cw9/Po0J+68cRjUvCLG2il3qWw6XZK3ui0MPrFx/MUKraD+dAKYPLmtN2FgBBk5/9XPLkPDKYy+zrp+72GEgHii98+LR+JAeerlUA+TycpW/TbT0NgivqGKObGTdFe/rgqBqtgFg898Mtf50C1NS5H7fhJPBvnd2ZPbtMEr/x7wPUpMHyda7NQ/veqsw0bf4ZHBcwUzvOU+Gb+Y9hQDPsydAW8zju5Qhzmt1mGTuf6elTz8U3WJodCnzRt5hr2Qdh/MuB+HGaxfYjc1PQqjTjtfGi4AvM4H7LUDc4QD/52OsLthlTcMeS1ZYOLcAm6VBClS5HAUqa0vWe3tJH7Xh276SsgpM/HOIYrV4xZor4gG/LJMZGgJ6QfWX3V8yC7P805hjfzHj6UtYGQYfetaTdTGvDRW9WcwaMexdAxLpFtpgy7YJNQtB36ewcDL9JV/mOoDTqG1Wi1+Co1WVB1FuRLXn1EEwInbvb8w5SnQgC/swW8x3B+9U9BFbcGW/hClPdAkcIKRQNP1sWtQtLAZlbdoGeQbxnSe5uPI55WAWjv687k3VdF9YqRGtGIrsuV5fcJTKOULJBSlwuD/XpaOkH7D334Lcl7XyJgWik+BtgJYA1zofPHNjTu53szRjtRjt0xm7OfzuQh0gY05+/V4AuvaqR04kkETRT0S6A2yQZUAhWxf+ANJEf2Cc/274xYccJqCXZ2PHkY4vyNu7N7CXFxQJ3gXdwavgS2xu/bzrD2VIn+XTyokHZ9S8+Ou7QOK9bPZSMUnLjGBItu7/IgASZVNg34UxNnfKo7qh/XiYF7tDpnihuOEgzxxMUAJhUfGJihRTYCLet+xJdb7Fv2j+o; NAP=V=1.9&E=1cfc&C=sj4fa9SmJnLaYFpI5WCWqOqz0ceCxxrXYVFi9RY7Kg3CprF4awENYQ&W=1; PPLState=1; WLID=wN1A8Ls6DPS/CPdmZrxSU6wwBhvDSpVchojmQJQuwz53Nn06USAcAco2GJt3lj0j2p0YthCvpwPaln8oYPZxqqVHq9Oc+q2hDQGGqyLgZSk=; WLS=C=d1499cb94bb3b0f2&N=Steven; _U=1wBVngCmUtqLEaVoR3mD-EpYRiIcS9EUhA4U6JZBkyR13lxLQjarJk6r-rsdG9yMKE5oR_YtMkcIv7aa-o_Ow3OLJqy-Io970wNuPvqYS8BphDx4Hi9FpT-iAkEo8vyubly_LNA6olh3DEkH8AKJOGZrd5LEghOqSJFpsxp9qF5mzBmYmX6WUg6mZSRwqJOE6l39xIqgHhJ7h9EGRFzdC1MApO2Mg_YJbqwum4mtYU2U; CSRFCookie=3ba98cc8-e5e2-4b16-9900-3250ffc42ac8; SRCHUSR=DOB=20240126&POEX=W; BFBUSR=CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF; MUID=0A013B01BFB46E1F135F2F13BE0E6FBF; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=D4D0AEECCE674B7292A145F3B950E1F0&dmnchg=1; _EDGE_S=F=1&SID=3031FBB6452E680F26F4EFA4449469B6; _EDGE_V=1"

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