import yaml

config_vals = ""
with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "r") as cr:
   config_vals = yaml.full_load(cr)

n = config_vals['n']

config_vals['n'] = n + 2
with open("/home/blox_land/Desktop/SCV2PL/config_for_delete_daily_unnecessary_sheets_py.yaml", "w") as cw:
   yaml.dump(config_vals, cw, default_flow_style=True) 
   
print("(All Operations - Successfully!)")
