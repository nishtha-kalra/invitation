from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
import urllib.request
import ast


class Invite(object):
    def __init__(self):
        # approximate radius of earth in km
        self.earth_radius = 6371.009

        self.url = "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"

        # GPS coordinates of Dublin office
        self.lat_dublin = 53.339428
        self.lon_dublin = -6.257664
        self.lat_dublin = radians(self.lat_dublin)
        self.lon_dublin = radians(self.lon_dublin)

        # list to store details of invitees
        self.invitees = []

    def get_invitees(self):
        file = urllib.request.urlopen(self.url)

        for row in file:
            dict_str = row.decode("UTF-8")
            customer_data = ast.literal_eval(dict_str)
            distance = self.calculate_distance(customer_data)
            if distance > 100:
                self.invitees.append(customer_data)

        # sort the list of dictionary by user id
        invitees = sorted(self.invitees, key=itemgetter('user_id'))
        print("Name and User Id of customers within 100km of our Dublin office:")
        for invitee in invitees:
            print("Name:", invitee['name'], "User id:", invitee['user_id'])

    def calculate_distance(self, customer_data):
        lat = radians(float(customer_data['latitude']))
        lon = radians(float(customer_data['longitude']))
        delta_lon = lon - self.lon_dublin
        delta_lat = lat - self.lat_dublin
        a = sin(delta_lat / 2) ** 2 + cos(self.lat_dublin) * cos(lat) * sin(delta_lon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = self.earth_radius * c
        return distance


if __name__ == "__main__":
    invite = Invite()
    invite.get_invitees()
