import yaml

config_vals = ""
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

b = config_vals['b']
c = config_vals['c']
n = config_vals['n']

config_vals['b'] = b + 1
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)

config_vals['c'] = c + 1
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True)

config_vals['n'] = n + 2
with open("/app/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True) 
   
print("(All Operations - Successfully!)")
