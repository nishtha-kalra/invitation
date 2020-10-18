from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
import urllib.request
import ast


class Invite(object):
    def __init__(self):
        return

    def find_distance(self):
        # approximate radius of earth in km
        earth_radius = 6371.009
        url = "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"
        file = urllib.request.urlopen(url)

        # GPS coordinates of Dublin office
        lat1 = 53.339428
        lon1 = -6.257664
        lat1 = radians(lat1)
        lon1 = radians(lon1)

        # list to store details of invitees
        invitees = []

        for row in file:
            dict_str = row.decode("UTF-8")
            mydata = ast.literal_eval(dict_str)
            lat2 = radians(float(mydata['latitude']))
            lon2 = radians(float(mydata['longitude']))
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = earth_radius * c
            if distance > 100:
                invitees.append(mydata)

        # sort the list of dictionary by user id
        invitees = sorted(invitees, key=itemgetter('user_id'))
        for invitee in invitees:
            print("Name:", invitee['name'], "User id:", invitee['user_id'])


if __name__ == "__main__":
    invite = Invite()
    invite.find_distance()
