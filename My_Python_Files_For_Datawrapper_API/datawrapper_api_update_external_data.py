from datetime import datetime, timedelta
from datawrapper import Datawrapper

yesterday1 = datetime.today() - timedelta(days=1)
a = yesterday1.strftime('%Y%m%d')
yesterday2 = datetime.today() - timedelta(days=2)
b = yesterday2.strftime('%Y%m%d')
yesterday3 = datetime.today() - timedelta(days=3)
c = yesterday3.strftime('%Y%m%d')
yesterday4 = datetime.today() - timedelta(days=4)
d = yesterday4.strftime('%Y%m%d')
yesterday5 = datetime.today() - timedelta(days=5)
e = yesterday5.strftime('%Y%m%d')
yesterday6 = datetime.today() - timedelta(days=6)
f = yesterday6.strftime('%Y%m%d')
yesterday7 = datetime.today() - timedelta(days=7)
g = yesterday7.strftime('%Y%m%d')     

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


dw = Datawrapper(access_token = "********************")

dw_id = 'nK681'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(a)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'ZJF26'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(b)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'FwfK3'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(c)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'omUrz'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(d)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = '1cfR3'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(e)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'galdz'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(f)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = '23zkY'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(g)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)



dw_id = '3btH7'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(a)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'zRe7S'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(b)+'&single=true&output=csv'

metadata = {

    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'YTJUM'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(c)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'EnedJ'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(d)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = '2rIZu'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(e)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'msk23'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(f)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)


dw_id = 'KNHOM'

external_data = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRIjws4Q1BZo9Wb4WoCG33oGOHPT0MRz440MXsFj2IjSttKJblRuz-U86j53WGZ7occaPDAYGKSIC8g/pub?gid='+str(g)+'&single=true&output=csv'

metadata = {
    "data": {
        "external-data": external_data
    }
}

dw.update_metadata(dw_id, metadata)

properties = dw.chart_properties(dw_id)

dw.publish_chart(dw_id)

print(properties)

# python3 /app/datawrapper_api_update_external_data.py
