#--------------------------------  NOTE  ----------------------------------------
# 1 This code is to download and manamge the Dataport dataset;
# 2 The code includes Dataport_meta and Dataport_get;
# 3 Coder: Cong Feng        Date: 2018/10/12       @ DOES Lab, UTD.
#--------------------------------------------------------------------------------
def Dataport_get(usrname, pswd, hsid, timeres, qc):
    import psycopg2
    import pandas as pd

    # database parameters
    PGHOST = "dataport.cloud"
    PGDATABASE = 'postgres'

    name_tb = 'university.electricity_egauge_' + timeres  # table name
    conn_string = "host=" + PGHOST + " port=" + "5434" + " dbname=" + PGDATABASE + " user=" + usrname \
                  + " password=" + pswd
    conn = psycopg2.connect(conn_string)
    sql_command = 'SELECT * FROM ' + name_tb + ' where dataid=' + str(hsid)
    sql_command2 = 'SELECT total_amount_of_pv FROM ' + 'university.metadata where dataid=' + str(hsid)
    df_hs = pd.read_sql(sql_command, conn) # extract house data from the database
    cap = pd.read_sql(sql_command2, conn) # get the PV installation capacity
    conn.close()

    # perform quality controls (QCs)
    df_hs = df_hs.dropna(axis = 1, thresh = .9*len(df_hs)) # remove columns with 90% NAs
    df_hs = df_hs.sort_values(['localhour'])
    if qc:
        # flag: 0-good data, 1-missing data, 2-out of bound data
        df_hs['flag'] = 0
        df_hs.loc[df_hs.apply(lambda x: x.count(), axis=1) != df_hs.shape[1], 'flag'] = 1
        df_hs.loc[(df_hs['gen'] < 0) | (df_hs['gen'] > cap.iat[0, 0]), 'flag'] = 2
        # bound gen column
        df_hs.loc[(df_hs['gen'] < 0), 'gen'] = 0
        df_hs.loc[(df_hs['gen'] > cap.iat[0, 0]), 'gen'] = cap

        # interpolate NAs
        df_hs.ix[:, 2:df_hs.shape[1]] = df_hs.ix[:, 2:df_hs.shape[1]].interpolate(method = 'linear', axis = 1)
    return df_hs