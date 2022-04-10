
from lib.pages_screen import PlusAddingDeletingKid
from tests import Init


class TestPlusAddingDeletingKid(Init):

    def testPlusAddingDeletingKid(self):
        login_screen = PlusAddingDeletingKid.PlusAddingDeletingKid(self.driver)
        login_screen.verifyingPlusAddingDeletingKid()
