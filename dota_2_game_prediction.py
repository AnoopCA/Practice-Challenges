import sys
import pandas as pd
from itertools import chain
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import warnings
warnings.filterwarnings('ignore')

def preprocess(data_in, task):
    data_in = [[j for j in i.strip().split(',')] for i in data_in]
    char_cols = ['tm_1_chr_1','tm_1_chr_2','tm_1_chr_3','tm_1_chr_4','tm_1_chr_5','tm_2_chr_1','tm_2_chr_2','tm_2_chr_3','tm_2_chr_4','tm_2_chr_5']
    char_dict = {'Viper': 0, 'Morphling': 1, 'Vengeful Spirit': 2, 'Ursa': 3, 'Enigma': 4, 'Treant Protector': 5, 'Visage': 6, 'Death Prophet': 7, 
                 'Shadow Fiend': 8, 'Kunkka': 9, 'Silencer': 10, 'Bounty Hunter': 11, "Nature's Prophet": 12, 'Magnus': 13, 'Shadow Shaman': 14, 
                 'Spectre': 15, 'Naga Siren': 16, 'Keeper of the Light': 17, 'Pudge': 18, 'Queen of Pain': 19, 'Warlock': 20, 'Ogre Magi': 21, 
                 'Skeleton King': 22, 'Witch Doctor': 23, 'Phantom Assassin': 24, 'Razor': 25, 'Centaur Warrunner': 26, 'Drow Ranger': 27, 
                 'Spirit Breaker': 28, 'Sniper': 29, 'Brewmaster': 30, 'Zeus': 31, 'Pugna': 32, 'Tiny': 33, 'Bloodseeker': 34, 'Wisp': 35, 'Timbersaw': 36, 
                 'Disruptor': 37, 'Windrunner': 38, 'Lion': 39, 'Chaos Knight': 40, 'Bane': 41, 'Tinker': 42, 'Slark': 43, 'Chen': 44, 'Doom': 45, 
                 'Jakiro': 46, 'Slardar': 47, 'Sven': 48, 'Undying': 49, 'Venomancer': 50, 'Invoker': 51, 'Juggernaut': 52, 'Lich': 53, 'Tidehunter': 54, 
                 'Anti-Mage': 55, 'Dragon Knight': 56, 'Ancient Apparition': 57, 'Alchemist': 58, 'Storm Spirit': 59, 'Riki': 60, 'Dazzle': 61, 
                 'Nyx Assassin': 62, 'Mirana': 63, 'Lone Druid': 64, 'Phantom Lancer': 65, 'Templar Assassin': 66, 'Puck': 67, 'Huskar': 68, 
                 'Enchantress': 69, 'Rubick': 70, 'Dark Seer': 71, 'Troll Warlord': 72, 'Clockwerk': 73, 'Sand King': 74, 'Beastmaster': 75, 'Necrolyte': 76, 
                 'Broodmother': 77, 'Gyrocopter': 78, 'Clinkz': 79, 'Leshrac': 80, 'Faceless Void': 81, 'Batrider': 82, 'Earthshaker': 83, 'Axe': 84, 
                 'Meepo': 85, 'Outworld Devourer': 86, 'Shadow Demon': 87, 'Weaver': 88, 'Lina': 89, 'Night Stalker': 90, 'Lifestealer': 91, 'Medusa': 92, 
                 'Lycanthrope': 93, 'Crystal Maiden': 94, 'Luna': 95, 'Omniknight': 96}
    #unique_chars = set(list(chain.from_iterable(data.drop('won_tm', axis=1).values.tolist())))
    #char_dict = {char:idx for idx,char in enumerate(unique_chars)}
    if task == 'train':
        data = pd.DataFrame(data_in, columns=[*char_cols,'won_tm'])
        data[char_cols] = data[char_cols].replace(char_dict)
        data['won_tm'] = data['won_tm'].map({'1':0, '2':1})
    else:
        data = pd.DataFrame(data_in, columns=char_cols)
        data[char_cols] = data[char_cols].replace(char_dict)
    return data

if __name__ == "__main__":
    with open('trainingdata.txt', 'r') as f:
        data_in = f.readlines()
    data = preprocess(data_in, 'train')    
    X_train,X_test,y_train,y_test = train_test_split(data.drop('won_tm',axis=1), data['won_tm'], stratify=data['won_tm'], test_size=0.01)

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)

    data_in = sys.stdin.read().strip().split('\n')
    k = int(data_in[0])
    data = preprocess(data_in[1:], 'test')
    pred = rf_model.predict(data)
    for i in pred:
        if i == 0:
            print(1)
        else:
            print(2)
    