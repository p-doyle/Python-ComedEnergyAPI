import requests
import json
import datetime


def loginToComedAndAuthSAML(comedUesrname, comedPassword):

    mySession = requests.session()

    
    data = {
        'USER': comedUesrname,
        'PASSWORD': comedPassword,
        'Target': 'https://secure.comed.com/pages/adaptor.aspx',
        'SMAUTHREASON': '0'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'DNT': '1'
    }

    # this will give us a sessionID but its not needed anywhere???
    requestURL = 'https://secure.comed.com/forms/login.fcc'
    response = mySession.post(requestURL, data=data, headers=headers, allow_redirects=True)


    # this url doesnt matter?  just need to send a request so it will redirect us with a SAMLRequest number
    energyUseURL = 'https://cec.opower.com/ei/x/e/energy-use-details'
    response2 = mySession.get(energyUseURL, cookies=response.cookies, allow_redirects=True)


    # this will redirect to a url like:
    # https://secure.comed.com/fed/Pages/saml2sso.aspx?SAMLRequest=asdf
    samlURL = response2.url  
    response3 = mySession.get(samlURL, allow_redirects=True)


    # need to pull the SAMLRsponse and RelayState from the request response so we can use it in the next one
    samlResponse = response3.text.split("SAMLResponse:'")[1].split("'")[0]
    relayState = response3.url.split('&')[-1].split('=')[1]

    data4 = {
        'SAMLResponse': samlResponse,
        'RelayState': relayState
    }

    # this will authenticate the session
    samlURL = 'https://sso.opower.com/sp/ACS.saml2'
    response4 = mySession.post(samlURL, data=data4, allow_redirects=True)


    # return the auth'd session so it can be used for other requests
    return mySession


def sendUsageRequest(startDate, endDate, dataPeriod, utilityAccountId):
    
    startDateStr = datetime.datetime.strftime(startDate, '%Y-%m-%dT%H:00+0000')
    endDateStr = datetime.datetime.strftime(endDate, '%Y-%m-%dT%H:00+0000')

    requestParams = {
        'startDate': startDateStr,
        'endDate': endDateStr,
        'aggregateType': dataPeriod
    }

    requestDataURL = 'https://cec.opower.com/ei/edge/apis/DataBrowser-v1/cost/utilityAccount/{}'.format(utilityAccountId)
    response = authedSession.get(requestDataURL, allow_redirects=True, params=requestParams)

    return json.loads(response.text)
