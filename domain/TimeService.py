from time import time

class TimeService:
    def getTime():
        return round(time() * 1_000)