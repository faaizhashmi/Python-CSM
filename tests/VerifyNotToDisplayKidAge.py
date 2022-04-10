
from lib.pages_screen.NotToDisplayTheirKidsAgePage import NotToDisplayKidAge
from tests import Init


class VerifyNotToDisplayKidAge(Init):

    def testNotToDisplayKidAge(self):
        plus_adding_kid = NotToDisplayKidAge(self.driver)
        plus_adding_kid.test_not_to_display_kid_age()

