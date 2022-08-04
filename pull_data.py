import requests
import pandas as pd
import datetime

def consumption_retriever(energy_type, mpn, serial_number, auth_api):

    url = "https://api.octopus.energy/v1/" + energy_type + "-meter-points/" + mpn + "/meters/" + serial_number + "/consumption/"
    auth=(auth_api, '')

    params = {"page_size": 25000, "period_from": "2021-07-31T00:00:00Z", "period_to": "2022-07-31T00:00:00Z"}
    response = requests.get(url, auth=auth, params=params)

    response_data = response.json()
    results = response_data['results']
    results_df = pd.DataFrame.from_records(results)
    print(results_df)

    csv_obj = results_df.to_csv(energy_type + '_records.csv', index=False)

    return results_df

''' INPUT YOUR ACCOUNT DETAILS HERE '''

auth = ''
mpan = ''
serial_elec = ''

mprn = ''
serial_gas = ''

elec_df = consumption_retriever('electricity',
                                mpan,
                                serial_elec, 
                                auth)
gas_df = consumption_retriever('gas', 
                                mprn, 
                                serial_gas, 
                                auth)
