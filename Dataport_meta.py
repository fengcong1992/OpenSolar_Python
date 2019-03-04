#--------------------------------  NOTE  ----------------------------------------
# 1 This code is to download and manamge the Dataport dataset;
# 2 The code includes Dataport_meta and Dataport_get;
# 3 Coder: Cong Feng        Date: 2018/10/12       @ DOES Lab, UTD.
#--------------------------------------------------------------------------------

def Dataport_meta(usrname, pswd, qc, ifdownload, root_save):
    import psycopg2
    import pandas as pd
    import os
    # database parameters
    PGHOST = "dataport.cloud"
    PGDATABASE = 'postgres'

    if not qc:  # decide if perform quality control
        # connect to the database
        conn_string = "host=" + PGHOST + " port=" + "5434" + " dbname=" + PGDATABASE + " user=" + usrname \
                      + " password=" + pswd
        conn = psycopg2.connect(conn_string)
        sql_command = 'SELECT * FROM university.metadata'
        df_all = pd.read_sql(sql_command, conn)  # extract meta data
        df_pv = df_all.loc[df_all['pv'] == 'yes']  # filter the data
        table_write = df_pv
        conn.close()
    else:
        # connect to the database
        conn_string = "host=" + PGHOST + " port=" + "5434" + " dbname=" + PGDATABASE + " user=" + usrname \
                      + " password=" + pswd
        conn = psycopg2.connect(conn_string)
        sql_command = 'SELECT * FROM university.metadata'
        df_all = pd.read_sql(sql_command, conn)  # extract meta data
        df_pv = df_all.loc[df_all['pv'] == 'yes']  # filter the data
        table_all = pd.DataFrame(columns=['dataid', 'startdate', 'enddate', 'ncols', 'ifpv'])
        for n_hs in range(len(df_pv)):  #
            hs_id = df_pv.iloc[n_hs].loc['dataid']
            time_resolution = 'hours'
            name_tb = 'university.electricity_egauge_' + time_resolution
            sql_command = 'SELECT * FROM ' + name_tb + ' where dataid=' + str(hs_id)
            df_hs = pd.read_sql(sql_command, conn)  # extract meta data
            if len(df_hs) == 0:
                table_all.loc[n_hs] = [hs_id, None, None, 0, False]
            else:
                table_all.loc[n_hs] = [hs_id, str(pd.Timestamp(df_hs.ix[:, 1].min())),
                                       str(pd.Timestamp(df_hs.ix[:, 1].max())), df_hs.shape[1], True]
        conn.close()
        table_write = table_all.loc[table_all['ifpv'] == True]
    if ifdownload:
        table_write.to_csv(os.path.join(root_save, 'Dataport_metadata.csv'), index=False)
    return table_write