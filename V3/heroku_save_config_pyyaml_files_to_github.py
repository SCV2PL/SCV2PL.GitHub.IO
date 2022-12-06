from github import Github
from datetime import datetime

g = Github("********************")
# or  g = github.Github(login, password)

repo = g.get_user().get_repo("scv2pl")

contents1 = repo.get_contents("config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml")
with open('config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml', 'r') as file:
    content1 = file.read()

# update
repo.update_file(contents1.path, "Save: config_for_delete_unnecessary_rows_in_SUM_sheets_py.yaml", content1, contents1.sha)

print(content1)


contents2 = repo.get_contents("config_for_save_daily_sum_py.yaml")
with open('config_for_save_daily_sum_py.yaml', 'r') as file:
    content2 = file.read()

# update
repo.update_file(contents2.path, "Save: config_for_save_daily_sum_py.yaml", content2, contents2.sha)

print(content2)


contents3 = repo.get_contents("config_for_update_avr7d_array_range_7d_py.yaml")
with open('config_for_update_avr7d_array_range_7d_py.yaml', 'r') as file:
    content3 = file.read()

# update
repo.update_file(contents3.path, "Save: config_for_update_avr7d_array_range_7d_py.yaml", content3, contents3.sha)

print(content3)


contents4 = repo.get_contents("config_for_update_avr7d_ir28_fdr21_py.yaml")
with open('config_for_update_avr7d_ir28_fdr21_py.yaml', 'r') as file:
    content4 = file.read()

# update
repo.update_file(contents4.path, "Save: config_for_update_avr7d_ir28_fdr21_py.yaml", content4, contents4.sha)

print(content4)


contents5 = repo.get_contents("config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml")
with open('config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml', 'r') as file:
    content5 = file.read()

# update
repo.update_file(contents5.path, "Save: config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", content5, contents5.sha)

print(content5)


contents6 = repo.get_contents("config_for_delete_daily_unnecessary_sheets_py.yaml")
with open('config_for_delete_daily_unnecessary_sheets_py.yaml', 'r') as file:
    content6 = file.read()

# update
repo.update_file(contents6.path, "Save: config_for_delete_daily_unnecessary_sheets_py.yaml", content6, contents6.sha)

print(content6)


print("(All Operations - Successfully!)")
