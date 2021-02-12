from datetime import datetime

# method: return date time string
def get_now():
    now = datetime.now()
    strtime = now.strftime("%Y%m%d%H%M%S")
    return strtime
