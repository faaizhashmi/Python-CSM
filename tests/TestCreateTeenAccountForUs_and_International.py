from lib.pages_screen import CreateTeenAccountForUs_and_InternationalPage
from tests import Init


class TestCreateTeenAccountForUs_and_International(Init):

    def test_free_teen_signup_for_us_and_international(self):
        teen_signup = CreateTeenAccountForUs_and_InternationalPage.CreateTeenAccountForUs_and_InternationalPage(self.driver)
        teen_signup.test_free_teen_signup_for_international()
        teen_signup.test_free_teen_signup_for_us()
