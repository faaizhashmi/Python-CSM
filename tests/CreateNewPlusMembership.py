
from lib.pages_screen.CreateNewPlusMemberPage import CreateNewPlusMemberPage
from tests import Init


class TestCreateNewPlusMembership(Init):

    def testCreateNewPlusMembership(self):
        plus_adding_kid = CreateNewPlusMemberPage(self.driver)
        plus_adding_kid.verify_create_new_plus_member_account()
