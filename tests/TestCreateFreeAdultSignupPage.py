from lib.pages_screen import CreateFreeAdultSignupPage
from tests import Init


class TestCreateFreeAdultSignupPage(Init):

    def test_free_adult_signup(self):
        adult_signup = CreateFreeAdultSignupPage.CreateFreeAdultSignupPage(self.driver)
        adult_signup.test_free_adult_signup()
