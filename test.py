import tzlocal
import datetime
from tzlocal import get_localzone
t = get_localzone()
time = datetime.datetime.now(t)
replace = str(time.replace(microsecond=0))

print(replace[11:13])