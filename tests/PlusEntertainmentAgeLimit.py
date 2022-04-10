
from lib.pages_screen import PlusEntertainmentAgeLimitPage
from tests import Init


class PlusEntertainmentAgeLimit(Init):

    def testEntertainmentAgeLimit(self):
        entertainmentage = PlusEntertainmentAgeLimitPage.PlusEntertainmentAgeLimitPage(self.driver)
        entertainmentage.verifying_plus_entertainment_age_limit()
