from github import Github
import pandas as pd
from datetime import datetime, timedelta
import yaml
import time
import subprocess

with open("config_create_sheets.yaml", "r") as cr:
    config_vals = yaml.full_load(cr)
Source1 = config_vals['api_daily_data_Source1']
Source2 = config_vals['api_daily_data_Source2']
sep = config_vals['sep']
save_path_extract1 = config_vals['save_path_extract1']
save_path_extract2 = config_vals['save_path_extract2']
s = config_vals['g']
g = Github(s)

# 'YYYMMDD'
a = datetime.today().strftime('%Y%m%d')
sheet_id1 = a
sheet_id2 = a
b = datetime.today() - timedelta(days=1)
c = b.strftime('%Y-%m-%d')
t = datetime.today().strftime('%Y-%m-%d')
config_vals['datetime'] = t
with open("config_create_sheets.yaml",
          "w") as cw:
    yaml.dump(config_vals, cw, default_flow_style=True)
print('DATE: ' + a)
print('"stan_rekordu_na": ' + c)
file1 = a + '.csv'
file2 = a + '.csv'
script_path = "startupscript.sh.sh"

df1 = pd.read_csv(Source1, sep=sep, encoding="")
if 'liczba_nowych_zakazen' not in df1.columns:
    df1.insert(1, column="liczba_nowych_zakazen", value="-")
if 'liczba_ponownych_zakazen' not in df1.columns:
    df1.insert(2, column="liczba_ponownych_zakazen", value="-")
if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
    df1.insert(4, column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df1.columns:
    df1.insert(5, column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ozdrowiencow' not in df1.columns:
    df1.insert(11, column="liczba_ozdrowiencow", value="-")

df2 = pd.read_csv(Source2, sep=sep, encoding="")
if 'liczba_nowych_zakazen' not in df2.columns:
    df2.insert(2, column="liczba_nowych_zakazen", value="-")
if 'liczba_ponownych_zakazen' not in df2.columns:
    df2.insert(3, column="liczba_ponownych_zakazen", value="-")
if 'liczba_nowych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
    df2.insert(5, column="liczba_nowych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ponownych_zakazen_na_10_tys_mieszkancow' not in df2.columns:
    df2.insert(6, column="liczba_ponownych_zakazen_na_10_tys_mieszkancow",
               value="-")
if 'liczba_ozdrowiencow' not in df2.columns:
    df2.insert(12, column="liczba_ozdrowiencow", value="-")

print(df1)
print(df2)
print('Save: ' + save_path_extract1 + file1)
print('Save: ' + save_path_extract2 + file2)

check_date = df2.at[0, 'stan_rekordu_na']
print('"stan_rekordu_na" from source: ' + check_date)
print('Whether: "stan_rekordu_na" from source = "stan_rekordu_na" ???:')

while check_date == c:
    print('YES')
    df1.to_csv(save_path_extract1 + (a) + '.csv', index=False)
    df2.to_csv(save_path_extract2 + (a) + '.csv', index=False)

    repo = g.get_user().get_repo("SARS-CoV-2_PL_V_2.0")

    file_path = 'Source1/'+(a)+'.csv'
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, "Save: Source1/"+str(a)+".csv",
                     content)

    file_path = 'Source2/'+(a)+'.csv'
    with open(file_path, 'r') as file:
        content = file.read()
    repo.create_file(file_path, "Save: Source2/"+str(a)+".csv",
                     content)
    time.sleep(15)

    result = subprocess.check_call(['bash', 'script.sh'], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    print(result.stdout.decode())

    break
else:
    print('NO')
