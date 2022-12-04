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


dw_id = 'JW5zN'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'p1M7c'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'wt85J'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'WVcSA'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'uO9JC'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

dw_id = 'C3dh5'

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

print("All Operations - Successfully!")
