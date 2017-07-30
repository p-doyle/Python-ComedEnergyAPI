import datetime
import pprint
import ComedEnergyAPI

comedUser = 'yourusername'
comedPwd = 'yourpassword'
utilityAccountId = 'yourutilityaccountid'

authedSession = ComedFunctions.loginToComedAndAuthSAML(comedUser, comedPwd)

startDate = datetime.datetime(2017, 05, 01, hour=1)
endDate = datetime.datetime(2017, 06, 01, hour=1)

# data period can be hour, day or bill
dataPeriod = 'hour'

usageJson = ComedFunctions.sendUsageRequest(startDate, endDate, dataPeriod, utilityAccountId)

pprint.pprint(usageJson)


authedSession.close()
