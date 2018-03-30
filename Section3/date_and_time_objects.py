"""
You can refer to http://strftime.org/ for datetime formatting help
"""

from datetime import datetime
start_date = datetime(2017, 9, 14, 11, 41)
delta = datetime.now() - start_date
print(delta)
