import sys
import time

import requests
from datetime import timedelta, datetime

timeout = timedelta(minutes=5)

start_time = datetime.now()
end_time = start_time + timeout

url = "http://www.imtoodumbtofigureout531onmyown-staging.com"

while datetime.now() < end_time:
    response = requests.get(url)
    if response.status_code == 200:
        sys.exit(0)
    time.sleep(10)

sys.exit(1)
