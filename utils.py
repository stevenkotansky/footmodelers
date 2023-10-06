from libs import *

def tierFunc(x, tierBreak = 6):
    """
    Function to split weekly rankings into tiers

    param x: players weekly rank
    param tierBreak: size of each tier (default 6)

    return: players weekly tier based on their rank
    """

    return int(x/tierBreak) + 1

def addActuals(actualsPath, pred_df, week):
    """
    Function to add actual weekly rankings to predicted weekly rankings

    param actualsPath: data path for actual weekly rankings
    param pred_df: df to merge actual rankings on
    param week: week that is being added

    return: dataframe with actual rankings
    """
    scored = pd.read_csv(actualsPath)
    week1_wScored = pred_df.merge(scored[['Player', week]], left_on='Name', right_on='Player')

    return week1_wScored