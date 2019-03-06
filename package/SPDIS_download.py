def SPDIS_download(root_data, list_st_download, ifunzip, actualonly):
    import os
    import zipfile
    import requests

    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }


    list_st_data = ['Alabama', 'Arkansas', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Illinois', 'Indiana',
                    'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                    'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                    'Nebraska', 'New Hampshire', 'New Jersey',
                    'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'Rhode Island',
                    'South Carolina', 'South Dakota', 'Tennessee',
                    'Texas', 'Vermont', 'Virginia', 'West Virginia', 'Wisconsin', 'Arizona', 'California', 'Colorado',
                    'Idaho', 'Montana', 'Nevada',
                    'Oregon', 'Utah', 'Washington', 'Wyoming']



    for no_lst in range(len(list_st_download)):  ## This loops for each different state name user input
        name_st = list_st_download[no_lst]
        # check data availability
        if not name_st in ['Alabama', 'Arkansas', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Illinois', 'Indiana',
                    'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                    'Minnesota', 'Mississippi', 'Missouri', 'Montana',
                    'Nebraska', 'New Hampshire', 'New Jersey',
                    'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'Rhode Island',
                    'South Carolina', 'South Dakota', 'Tennessee',
                    'Texas', 'Vermont', 'Virginia', 'West Virginia', 'Wisconsin', 'Arizona', 'California', 'Colorado',
                    'Idaho', 'Montana', 'Nevada',
                    'Oregon', 'Utah', 'Washington', 'Wyoming']:  ##select column $state.name compare
            sys.exit('No data available for this state!')

        else:
            root_state = os.path.join(root_data, name_st)
            if not os.path.exists(root_state):
                os.mkdir(root_state)
            os.chdir(root_state) # set saving directory
            # download zip from URL
            URL = 'https://www.nrel.gov/grid/assets/downloads/' + us_state_abbrev[name_st].lower() + '-pv-2006.zip'
            r = requests.get(URL, allow_redirects=True)
            open(name_st + '.zip', 'wb').write(r.content)
            # unzip the files
            if ifunzip:
                zip_ref = zipfile.ZipFile(os.path.join(root_state, name_st + '.zip'), 'r')
                zip_ref.extractall(root_state)
                zip_ref.close()
            # if only remain actual data
            if actualonly:
                list_file = os.listdir(root_state)
                for n_file in range(len(list_file)):
                    name_file = list_file[n_file]
                    if not name_file[:6] == 'Actual':
                        os.remove(name_file)