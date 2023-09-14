# %%
# import utility functions (which also imports libraries needed)
from utils import *

# %%
# read in data
folder_path = "/Users/nicolaskuntz/Documents/projects/football and betting projects/footmodelers/data/Week 1"
xlsx_files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]
dataframes = []

for xlsx_file in xlsx_files:
    file_path = os.path.join(folder_path, xlsx_file)
    df = pd.read_excel(file_path)
    dataframes.append(df)
# %%
week1_wScored = addActuals(
    actualsPath='FantasyPros_Fantasy_Football_Points_PPR.csv',
    pred_df=dataframes[0],
    week='1'
)
# %%
week1_wScored_top100 = week1_wScored.head(100)
# %%
sorted_scores = pd.Series(sorted(week1_wScored_top100['1'], reverse=True), index=range(1,101))
sorted_scores = pd.DataFrame({'score': sorted_scores, 'scored_rank': sorted_scores.index})
# %%
week1_wScored_top100 = week1_wScored_top100.merge(sorted_scores, left_on='1', right_on='score').drop('score', axis=1)
# %%
### Data ready for testing - going to create 4 different scoring options:
# Option 1: Tiered scoring - tiers in increments of 6 and score is based on distance from predicted tier (no tier weigths involved yet)
# Option 2: Tiered scoring - same as option 1, but tiers are weighted. Lots of options for weighting, 
# but one option could be that if a player in tier one is outside of tier one, that has a bigger penalty than say a player in tier 3 dropping to tier 4
# Option 3: Straight up numerical ranking residuals (predicted = 5th overall and actual = 10th overall is -5 score)
# Option 4: Weighted numerical ranking - similar to tiers weighting, but still uses actual numerical residual for the score)
### Note: Depending on what we want to use this tool for, I think we should have different values on a player doing better than expected vs a player doing worse than expected. 
### For example, if we expect a player to be top 24 and they drop to like top 36, that probably has bigger impact on decision making than that player being top 12
### because a player dropping out of top 24 would cause you to not start them but you would still start them if they became top 12

#### Another Note: I'm finding that players are dropping out of tiers not because they played poorly, but because other random players did really well. 
#### For example, Chubb only got 2 less points than expected but he dropped 3 tiers because random players got way higher than expected points. 
#### Maybe we want to add a combined score of difference in weekly points and weekly rank? Idk we need to brainstorm this some more
# %%
# Option 1 Testing
test_df = week1_wScored_top100    
# %%
# Convert weekly rank into tiers and find difference between predicted and actual
# For this data I'm treating the 'Rank' column as the predicted data, once the model is built we can use the predictions instead of that column
test_df['predicted_tier'] = test_df['Rank'].apply(lambda x: tierFunc(x, tierBreak=12))
test_df['scored_tier'] = test_df['scored_rank'].apply(lambda x: tierFunc(x, tierBreak=12))
test_df['residual_score'] = test_df['predicted_tier'] - test_df['scored_tier']

# Comment on results from option 1: This was expected but good to call out that residuals are much lower when the tierBreak is less strict, i.e. tiers of 6 have worse residuals than tiers of 12

# %%
