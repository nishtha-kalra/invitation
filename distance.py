from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
import urllib.request
import ast


class Invite(object):
    def __init__(self):
        return

    def get_invitees(self):
        # approximate radius of earth in km
        earth_radius = 6371.009

        url = "https://s3.amazonaws.com/intercom-take-home-test/customers.txt"

        # GPS coordinates of Dublin office
        lat_dublin = 53.339428
        lon_dublin = -6.257664
        lat_dublin = radians(lat_dublin)
        lon_dublin = radians(lon_dublin)

        # list to store details of invitees
        invitees = []

        file = urllib.request.urlopen(url)

        for row in file:
            dict_str = row.decode("UTF-8")
            customer_data = ast.literal_eval(dict_str)
            distance = self.calculate_distance(customer_data, earth_radius, lat_dublin, lon_dublin)
            if distance > 100:
                invitees.append(customer_data)

        # sort the list of dictionary by user id
        invitees = sorted(invitees, key=itemgetter('user_id'))
        print("Name and User Id of customers within 100km of our Dublin office:")
        for invitee in invitees:
            print("Name:", invitee['name'], "User id:", invitee['user_id'])

    def calculate_distance(self, customer_data, earth_radius, lat_dublin, lon_dublin):
        lat = radians(float(customer_data['latitude']))
        lon = radians(float(customer_data['longitude']))
        delta_lon = lon - lon_dublin
        delta_lat = lat - lat_dublin
        a = sin(delta_lat / 2) ** 2 + cos(lat_dublin) * cos(lat) * sin(delta_lon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = earth_radius * c
        return distance


if __name__ == "__main__":
    invite = Invite()
    invite.get_invitees()
