import unittest
from invitation.distance import Invite


class TestInvitation(unittest.TestCase):

    def test_output(self):
        invitation = Invite()
        a = invitation.get_invitees()


if __name__ == '__main__':
    unittest.main()
