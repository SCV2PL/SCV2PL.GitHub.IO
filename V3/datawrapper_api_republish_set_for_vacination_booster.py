from datawrapper import Datawrapper

dw = Datawrapper(access_token = "********************")

dw_id = 'EBztU'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'VFe7U'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'ogppd'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'uXBbj'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


print("All Operations - Successfully!")
