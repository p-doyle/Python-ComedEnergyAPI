# Python-ComedEnergyAPI
## No longer in active development, use at your own risk!
Script for pulling Smart Meter energy usage data from Comed's API


Reverse engineered using [Fiddler](http://www.telerik.com/fiddler)

### 3 pieces of information are needed:
- Comed Username
- Comed Password
- Utility Account Id

The Comed username/password is the same as what you use to login to [Comed](https://secure.comed.com/pages/login.aspx).

The Utility Account Id is a unique identifier that, as far as I can tell, is not displayed anywhere on the site itself.  The only way I know to get this is to use Fiddler.

## Retrieve Utility Account Id
1. Login to [Comed](https://secure.comed.com/pages/login.aspx)
2. Open Fiddler and start capturing traffic
3. Open the [Comed 'View My Usage' page](https://secure.comed.com/MyAccount/MyBillUsage/pages/secure/ViewMyUsage.aspx)
4. Look for a request URL that looks like this(the account id is highlighted):

cec.opower.com/ei/edge/apis/DataBrowser-v1/cost/utilityAccount/**92a35d5d-be12-12e4-336a-c32867e62e64**?startDate=2015-07-30T05%3A00%2B0000&endDate=2017-07-29T05%3A00%2B0000&aggregateType=bill


## Using the API

#### Login to Comed and return an auth'd requests session
 - loginToComedAndAuthSAML(comedUser, comedPwd)

#### Send usage request for data between startDate and endDate over the given datePeriod, returned as JSON
- sendUsageRequest(authedSession, startDate, endDate, dataPeriod, utilityAccountId)
- datePeriod can be 'hour', 'day', or 'bill'

### Example Output
```
{u'ratePlans': [{u'code': u'C24',
                 u'description': None,
                 u'endDate': None,
                 u'isNew': False,
                 u'meterType': u'ELEC',
                 u'name': None,
                 u'series': {},
                 u'startDate': u'2015-01-19T00:00:00.000-06:00',
                 u'waysToLower': None}],
 u'reads': [{u'endTime': u'2017-05-02T00:00:00.000-05:00',
             u'isPeakPeriod': False,
             u'milesDriven': None,
             u'providedCost': 0.96466275,
             u'readComponents': [{u'cost': 0.96466275,
                                  u'dayPart': None,
                                  u'season': None,
                                  u'tierNumber': None,
                                  u'tierType': u'ORDINAL',
                                  u'value': 9.0375}],
             u'readType': u'ACTUAL',
             u'rebateAmount': 0,
             u'startTime': u'2017-05-01T00:00:00.000-05:00',
             u'value': 9.0375},
            {u'endTime': u'2017-05-03T00:00:00.000-05:00',
             u'isPeakPeriod': False,
             u'milesDriven': None,
             u'providedCost': 0.68713875,
             u'readComponents': [{u'cost': 0.68713875,
                                  u'dayPart': None,
                                  u'season': None,
                                  u'tierNumber': None,
                                  u'tierType': u'ORDINAL',
                                  u'value': 6.4375}],
             u'readType': u'ACTUAL',
             u'rebateAmount': 0,
             u'startTime': u'2017-05-02T00:00:00.000-05:00',
             u'value': 6.4375},
            {u'endTime': u'2017-05-04T00:00:00.000-05:00',
             u'isPeakPeriod': False,
             u'milesDriven': None,
             u'providedCost': 0.88620885,
             u'readComponents': [{u'cost': 0.88620885,
                                  u'dayPart': None,
                                  u'season': None,
                                  u'tierNumber': None,
                                  u'tierType': u'ORDINAL',
                                  u'value': 8.3025}],
             u'readType': u'ACTUAL',
             u'rebateAmount': 0,
             u'startTime': u'2017-05-03T00:00:00.000-05:00',
             u'value': 8.3025},
            {u'endTime': u'2017-05-05T00:00:00.000-05:00',
             u'isPeakPeriod': False,
             u'milesDriven': None,
             u'providedCost': 1.0652652,
             u'readComponents': [{u'cost': 1.0652652,
                                  u'dayPart': None,
                                  u'season': None,
                                  u'tierNumber': None,
                                  u'tierType': u'ORDINAL',
                                  u'value': 9.98}],
             u'readType': u'ACTUAL',
             u'rebateAmount': 0,
             u'startTime': u'2017-05-04T00:00:00.000-05:00',
             u'value': 9.98}],
 u'servicePointId': u'',
 u'siteTimeZoneId': u'America/Chicago',
 u'unit': u'KWH',
 u'utilityAccountUuid': u''}
 ```
