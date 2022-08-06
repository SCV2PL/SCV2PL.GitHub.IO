from datawrapper import Datawrapper

dw = Datawrapper(access_token = "********************")

dw_id = '4nqZF'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'j0TYA'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

print("All Operations - Successfully!")
