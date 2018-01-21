import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

player_data = pd.read_csv('player_data2.csv')
cols_w_na = []
for col in player_data.columns:
    if player_data[col].isnull().values.any():
        cols_w_na.append(col)


player_comps = player_data[player_data['Age'] > 23] # to be used for project
player_data = player_data[player_data['Age'] <= 23] #limiting data set to 23 or below


ws = player_data['WS'] #Target
player_comps = player_comps.drop(['Rk', 'Player', 'Season', 'Tm', 'Lg', 'WS'], axis=1) # No value columns
player_data = player_data.drop(['Rk', 'Player', 'Season', 'Tm', 'Lg', 'WS'], axis=1) # No value columns


# ['FG%', '2P%', '3P%', 'eFG%', 'FT%', 'TS%'], fill with average of field
for col in cols_w_na:
    player_data[col] = player_data[col].fillna(np.mean(player_data[col]))
    player_comps[col] = player_comps[col].fillna(np.mean(player_comps[col]))

player_data_train, player_data_test, ws_train, ws_test = train_test_split(player_data, ws, test_size=0.20, random_state=42)

gbm = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=10, random_state=0, loss='ls')
mdl_gbm = gbm.fit(player_data_train, ws_train)

regr = RandomForestRegressor(max_depth=10, random_state=0)

regr = RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=10,
           max_features='auto', max_leaf_nodes=None, min_impurity_split=0,
           min_samples_leaf=2, min_samples_split=4,
           min_weight_fraction_leaf=0.0, n_estimators=200, n_jobs=1,
           oob_score=False, random_state=0, verbose=0, warm_start=False)
mdl_regr = regr.fit(player_data_train, ws_train)

print "GBM: {0}".format(mdl_gbm.score(player_data_test, ws_test))
print "Random Forest: {0}".format(mdl_regr.score(player_data_test, ws_test))

# Predictions
player_data['final_pred'] = (mdl_gbm.predict(player_data) + mdl_regr.predict(player_data))/2
final_pred_by_age_before_24 = [(x, np.mean(player_data['final_pred'][player_data['Age'] == x])) for x in player_data['Age'].unique()]
out_df_before_24 = pd.DataFrame(final_pred_by_age_before_24, columns = ['Age', 'WS_pred'])

player_comps['final_pred'] = (mdl_gbm.predict(player_comps) + mdl_regr.predict(player_comps))/2
final_pred_by_age = [(x, np.mean(player_comps['final_pred'][player_comps['Age'] == x])) for x in player_comps['Age'].unique()]

out_df = pd.DataFrame(final_pred_by_age, columns = ['Age', 'WS_pred'])
out_df = out_df.append(out_df_before_24)

out_df.to_csv('predictions.csv', index=False)
print out_df
