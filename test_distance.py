import unittest
from math import radians
from distance import Invite


class TestInvitation(unittest.TestCase):

    def test_dublin_address(self):
        invite = Invite()
        self.assertEqual(radians(-6.257664), invite.lon_dublin)
        self.assertEqual(radians(53.339428), invite.lat_dublin)

    def test_calculate_distance(self):
        invite = Invite()
        data = {'latitude': '52.986375', 'user_id': 12, 'name': 'Christina McArdle', 'longitude': '-6.043701'}
        dist = invite.calculate_distance(data)
        self.assertEqual(dist, 41.76878450547117)


if __name__ == '__main__':
    unittest.main()
