# octopus_smart_meter_to_csv
Small repository for connecting to Octopus smart meter api and formatting pulled data into csv file for anaylsis

1) Clone the repository into your local host

``` 
git clone https://github.com/tmitcheson/octopus_smart_meter_to_csv.git
cd octopus_smart_meter_to_csv
```

2) Then set up a virtual environment and activate it

```
python3 -m venv my_env
source my_env/bin/activate
```
3) Install the requirements from requirements.txt
```
pip install requirements.txt
```
4) The enter the pull_data.py file and enter your account information on lines 25-30. These can be found on your Octopus account details page.
![mpan_mprn](https://user-images.githubusercontent.com/72881815/182808225-1c6ccb3e-2fc9-45f0-8e2e-1f881a5dd7f9.png)

You will also need your API key, which is available at https://octopus.energy/dashboard/developer/

5) Once you have all five variables configured, you can run the file
```
python3 pull_data.py
```
and your loaded csv files should appear in your folder. These are what you will upload to the Google Form.
