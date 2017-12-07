import requests
import json
import sys

def returnRouteDetails(routeString):
    routesUriString = "http://svc.metrotransit.org/nextrip/routes?format=json"
    response = requests.get(routesUriString)
    data = response.json()

    #iterate thru the list of dictionaries
    for lis in data:
        if (routeString == lis['Description']):
            return lis['Route']

    return ""

def returnStopDetails(stopName, routeNumber, direction):
    stopUriString = "http://svc.metrotransit.org/nextrip/stops/{}/{}?format=json".format(routeNumber, direction)
    response = requests.get(stopUriString)
    data = response.json()

    #iterate thru the list of dictionaries
    for lis in data:
        if (stopName == lis['Text']):
            return lis['Value']

    return ""

def returnTimepointDetails(routeNumber, direction, stopID):
    timepointUriString = "http://svc.metrotransit.org/nextrip/{}/{}/{}?format=json".format(routeNumber, direction, stopID)
    response = requests.get(timepointUriString)
    data = response.json()

    #iterate thru the list of dictionaries
    for lis in data:
        print(lis['Actual'])
        if (lis['Actual'] is not False):
            return lis['DepartureText']

    return ""

def main():

    if (sys.argv[3] == "south"):
        direction = 1
    elif (sys.argv[3] == "east"):
        direction = 2
    elif (sys.argv[3] == "west"):
        direction = 3
    else:
        direction = 4

    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])

    routeResult = returnRouteDetails(sys.argv[1])
    stopResult = returnStopDetails(sys.argv[2], routeResult, direction)
    timepointResult = returnTimepointDetails(routeResult, direction, stopResult)

    print(timepointResult)

def test():
    routeResult = returnRouteDetails("METRO Blue Line")
    print(routeResult)

    stopResult = returnStopDetails("Target Field Station Platform 1", routeResult, 4)
    print(stopResult)

    timepointResult = returnTimepointDetails( routeResult, 4, stopResult)
    print(timepointResult)

main()
