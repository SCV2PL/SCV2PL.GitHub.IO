import yaml

config_vals = ""
with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

n = config_vals['n']

config_vals['n'] = n + 4
with open("/app/config_for_delete_unnecessary_rows_in_voivodeships_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True) 
   
print("(All Operations - Successfully!)")
