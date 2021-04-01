import pandas as pd
import os
from datetime import datetime

def get_correl(rolling_window= 10):
    
    var_values = pd.read_csv('var_values.csv')

    df = var_values.drop('submit_date', axis = 1).set_index(['variable_id','as_of_date']).stack().unstack(level=0).reset_index().drop('level_1', axis = 1).set_index('as_of_date')

    var_correlations = pd.DataFrame()
    for i in df.columns:
        for j in df.columns:
            tmp = {'variable_id_1':[i for r in range(0,len(df))],'variable_id_2':[j for r in range(0,len(df))], 'calculation_date':datetime.today().strftime('%Y-%m-%d'), 'value':df[i].rolling(rolling_window).corr(df[j])}
            tmp = pd.DataFrame(tmp)
            var_correlations = var_correlations.append(tmp)

    return var_correlations.reset_index()