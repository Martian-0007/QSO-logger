def CurTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y_%H-%M-%S")
    return(current_time)