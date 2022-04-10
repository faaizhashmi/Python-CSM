from lib.pages_screen.PlusAddingKidOutsideManageFamilyArea import PlusAddingKidOutsideManageFamilyArea
from tests import Init


class TestPlusAddingKidOutsideManageFamilyArea(Init):

    def testAddingKidOutsideManageFamilyArea(self):
        plus_adding_kid = PlusAddingKidOutsideManageFamilyArea(self.driver)
        plus_adding_kid.verifyingAddingKidOutsideManageFamilyArea()
