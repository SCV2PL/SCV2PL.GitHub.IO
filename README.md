```
"""PEP 8 – Style Guide for Python Code 
https://peps.python.org/pep-0008
Is this style acceptable by convention and accepted by the Python community ???
Łukasz "Luke Blue" Andruszkiewicz
✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌
"""
```

For this my python code example: 

https://github.com/SCV2PL/SCV2PL.GitHub.IO/blob/main/V3/import_csv_data_from_urls.py

---
# SARS-CoV-2 Poland - "EPIDEMIC" App

Good changes generate improvements, verify the knowledge acquired so far - when using it in practice.

In my free time I will improve, correct and speed up my "EPIDEMIC" app regarding the SARS-CoV-2 virus in Poland:

https://scv2pl.github.io/scv2pl-en

Improved file - import_csv_data_from_urls.py:

https://github.com/SCV2PL/SCV2PL.GitHub.IO/blob/main/V3/import_csv_data_from_urls.py

Deprecated unused file - import_csv_data_from_urls_deprecated_2023-01-12.py:

https://github.com/SCV2PL/SCV2PL.GitHub.IO/blob/main/V2_deprecated_unused/import_csv_data_from_urls_deprecated_2023-01-12.py

&

Formula Parse ERROR:

=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33186,aktualne-dane-dla-powiatow/file",",",";"),"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20,Col21")

=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33186,aktualne-dane-dla-powiatow/file";",";";");"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20,Col21")

Both Formulas work without error for this sheet:

https://docs.google.com/spreadsheets/d/1JshfkqgC8bLhATHHkN3D5Bto19Sp3BpMBTYuAts5z_c/edit#gid=20230113

To my surprise and searching for the cause of the error - which I spent some time on, for this sheet:

https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g/edit#gid=20230113

Only this formula worked:

=QUERY(IMPORTDATA("https://api.dane.gov.pl/resources/33185,aktualne-dane-dla-wojewodztw/file";",";";");"Select Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14,Col15,Col16,Col17,Col18,Col19,Col20")

https://www.facebook.com/Blue.LOx.2020/posts/pfbid02CZJgCbf6hLWZn4VkVr9S7RcxRjFZB2iQJ7gVzrYuQVL2u3oAfLqYb3kb3YcKkiCul

# ✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌

#Python #Django #Ubuntu #Heroku #PostgreSQL #Postgres #SQL #GitHub #ML #AI #RPA

#PORTFOLIO - #OpenToWork

https://blox-land.herokuapp.com

#Plotly #Dash #Datawrapper #GoogleSheets #GoogleCloud #GCP #Data #DataVisualization #DataVisWriter #DataStorytelling #DataApplication #DataApplicationArchitect #DataScience #DataEngineering #DataMining #OpenData #OtwarteDane

Google Sheets for this project: 

https://lukebluelox.github.io/PORTFOLIO/#SCV2-PL

---

https://github.com/datawrapper

https://github.com/chekos/Datawrapper/blob/main/LICENSE

https://github.com/plotly/plotly.py/blob/master/LICENSE.txt

https://github.com/plotly/dash/blob/dev/LICENSE

# ✌💙💚♻️🌌🚀🌎🌍🌏🛰🌌♻️💚💙✌

 The MIT License (MIT)
 Copyright (c) 2021 chekos
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
 OR OTHER DEALINGS IN THE SOFTWARE.
 
 The MIT License (MIT)

Copyright (c) 2016-2018 Plotly, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The MIT License (MIT)

Copyright (c) 2022 Plotly, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<hr>
