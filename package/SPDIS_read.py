# --------------------------------  NOTE  ----------------------------------------
# 1 This code is to download and manamge the Solar Power Data for Integration
#   Studies (SPDIS);
# 2 The code includes SPDIS.download and SPDIS.read functions;
# 3 Coder: Cong Feng        Date: 2018/09/25       @ DOES Lab, UTD.
# --------------------------------------------------------------------------------
def SPDIS_read(root_data, name_st, list_files, readall):
    # read data code
    import os
    import xlrd
    import pandas as pd
    import zipfile
    import pandas

    if readall:
        list_files = os.listdir(os.path.join(root_data, name_st))
    os.chdir(os.path.join(root_data, name_st))  # set saving directory
    df_all = pd.read_csv(list_files[0])
    df_meta = pd.DataFrame()
    for n_file in range(1, len(list_files)):
        name_file = list_files[n_file]
        df_location = pd.read_csv(name_file)
        df_meta = df_meta.append([['Location' + str(n_file), name_file[7:12], name_file[13:20], name_file[-14:-10]]])
        df_all = pd.merge(df_all, df_location, on = ['LocalTime', 'LocalTime'])
        name_column = 'Location' + str(n_file) + "_" + name_file[-14:-10]
        df_all = df_all.rename(columns={df_all.columns[df_all.shape[1]-1]: name_column})
    return df_all, df_meta



