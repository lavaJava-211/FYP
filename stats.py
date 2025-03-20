import database
from collections import Counter

def graphPC():
    moduleList = database.get_modules()
    mCount = Counter(module[0] for module in moduleList)
    modules = list(mCount.keys())
    count = list(mCount.values())

    return modules, count

def graphLine():
    dateList = database.get_dates()
    dCount = Counter(module[0] for module in dateList)
    dates = list(dCount.keys())
    count = list(dCount.values())

    return dates, count

def emotionCount():
    eList = database.get_emotions()
    all_emotions = [emotion for row in eList for emotion in row if emotion]  
    eCount = Counter(all_emotions)  
    emotions = list(eCount.keys())
    count = list(eCount.values())

    return emotions, count
