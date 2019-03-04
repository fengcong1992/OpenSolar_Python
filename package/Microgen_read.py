#--------------------------------  NOTE  ----------------------------------------
# 1 This code is to manamge the Microgen dataset from Sheffield Solar;
# 2 Coder: Cong Feng        Date: 2018/10/11       @ DOES Lab, UTD.
#--------------------------------------------------------------------------------
def Microgen_read(root_data):
    import os
    import pandas as pd


    # read in data
    df_info = pd.read_csv(os.path.join(root_data, 'metadata.csv'))
    df_all = pd.read_csv(os.path.join(root_data, 'readings.csv'))

    list_loc = df_info['id'] # list of house IDs
    # initialize data frame
    df_genall = df_all[df_all['id'] == df_info.ix[0, 'id']][['date', 'time']]

    for no_loc in range(len(list_loc)):#len(list_loc)
        no_id = list_loc[no_loc]
        df_pv = df_all[df_all['id'] == no_id]
        pv_gen = df_pv['cumulative_reading'] - df_pv['cumulative_reading'].shift(1)
        pv_gen = pv_gen.reset_index(drop = True)
        pv_gen[0] = pv_gen[1]

        df_genall['new'] = pv_gen
        df_genall = df_genall.rename(columns={df_genall.columns[df_genall.shape[1]-1]: no_id})
    return df_genall