# --------------------------------  NOTE  ----------------------------------------
# 1 This code is to download the NREL Solar Radiation Research
#   Laboratory (SRRL) dataset;
# 2 Coder: Cong Feng        Date: 2018/09/25       @ DOES Lab, UTD.
# --------------------------------------------------------------------------------
from datetime import datetime, date, timedelta
import os
import requests
import zipfile
import pandas as pd
import io


def SRRL_download(root_data, date_start, date_end, skyimg, tmseries, ifunzip, ifunique):
    if skyimg:
        lgth_day = (datetime.strptime(date_end, '%Y-%m-%d') -
                    datetime.strptime(date_start, '%Y-%m-%d')).total_seconds() / 86400
        for no_day in range(2):  # int(lgth_day)
            date = datetime.strptime(date_start, '%Y-%m-%d') + timedelta(days=no_day)
            date2 = date.strftime('%Y%m%d')
            year = date.strftime('%Y')
            URL = os.path.join('https://midcdmz.nrel.gov/tsi/SRRLASI', year, str(date2) + '.zip')

            root_save = os.path.join(root_data, str(date2))
            if not os.path.exists(root_save):
                os.mkdir(root_save)
            os.chdir(root_save)

            file_name = str(date2) + '.zip'
            r = requests.get(URL)

            with open(file_name, 'wb') as f:
                f.write(r.content)

            open(file_name, 'wb').write(r.content)

            # whether unzip the file
            if ifunzip:
                zip_ref = zipfile.ZipFile(os.path.join(root_save, file_name), 'r')
                zip_ref.extractall(root_save)
                zip_ref.close()
                os.remove(file_name)
            # whether delete redundant files
            if ifunique:
                list_file = os.listdir(root_save)  # files in the root
                list_file2 = pd.Series([x[0:14] for x in list_file])  # files without extensions
                list_file3 = list_file2.unique()  # unique file numbers
                list_file4 = pd.Series(list_file3 + '_11_NE.jpg')
                list_file5 = pd.Series(list_file3 + '_1112_CDOC.png')
                list_file6 = list_file4.append(list_file5)
                for n_file in range(len(list_file)):
                    if not list_file[n_file] in list(list_file6):
                        os.remove(list_file[n_file])

    if tmseries:
        os.chdir(root_data)
        URL1 = 'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS;start=20150101;edy=31;emo=11;eyr=2017;year=2017;month=01;day=1;time=1;zenloc=200;inst=3;inst=53;inst=67;type=data;endyear=2017;endmonth=11;endday=30'
        r1 = requests.get(URL1).content
        df_2017a = pd.read_csv(io.StringIO(r1.decode('utf-8')))
        df_2017a.columns.values[[0, 2, 3, 4]] = ['Date', 'GHI', 'DNI', 'DHI']
        URL2 = 'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS;start=20171201;edy=31;emo=12;eyr=9999;year=2017;month=12;day=1;time=1;zenloc=209;inst=3;inst=55;inst=69;type=data;endyear=2017;endmonth=12;endday=31'
        r2 = requests.get(URL2).content
        df_2017b = pd.read_csv(io.StringIO(r2.decode('utf-8')))
        df_2017b.columns.values[[0, 2, 3, 4]] = ['Date', 'GHI', 'DNI', 'DHI']
        df_2017 = pd.concat([df_2017a, df_2017b], axis=0)
        URL3 = 'https://midcdmz.nrel.gov/apps/plot.pl?site=BMS;start=20171201;edy=31;emo=12;eyr=9999;year=2018;month=01;day=1;time=1;zenloc=209;inst=3;inst=55;inst=69;type=data;endyear=2018;endmonth=12;endday=31'
        r3 = requests.get(URL3).content
        df_2018 = pd.read_csv(io.StringIO(r3.decode('utf-8')))
        df_2018.columns.values[[0, 2, 3, 4]] = ['Date', 'GHI', 'DNI', 'DHI']
        df_combine = pd.concat([df_2017, df_2018], axis=0)
        df_combine['Date'] = pd.to_datetime(df_combine['Date'])
        #df_combine['Date'] = df_combine['Date'].dt.date
        mask = (df_combine['Date'] >= datetime.strptime(str(date_start), '%Y-%m-%d')) & (df_combine['Date'] <= datetime.strptime(
                str(date_end), '%Y-%m-%d'))
        df_final = df_combine.loc[mask]
        df_final.to_csv(os.path.join(root_data, 'SRRL_measurement_timeseries.csv'), index=False)
