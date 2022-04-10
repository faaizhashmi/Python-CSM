import os
import unittest
from lib.pages_screen import CreateFreeKidSignupPage, CreateFreeAdultSignupPage, CreateTeenAccountForUs_and_InternationalPage, MovieAndTvPage, PlusEntertainmentAgeLimitPage
from selenium import webdriver
from lib.pages_screen import LoginPage
from lib.pages_screen import GetItNow
from lib.pages_screen import PlusAddingDeletingKid
from lib.pages_screen.CreateNewPlusMemberPage import CreateNewPlusMemberPage
from lib.pages_screen.FilterWorkingForMovieBookAndGamePage import FilterWorkingForMovieBookAndGamePage
from lib.pages_screen.PlusAddingKidOutsideManageFamilyArea import PlusAddingKidOutsideManageFamilyArea
from tests import Init
class CsmTest(Init):




    def test_login_with_valid_email_and_password(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.login_check("tngtesteditor", "Et3sts!t3")

    def test_login_with_valid_email_and_invalid_password(self):
        login_page=LoginPage.LoginPage(self.driver)
        login_page.login_check_invalid_password("tngtesteditor", "Et3st123213s!t")


#     3	Test Case Title	As a user, I am unable to login with invalid email and valid password (for parents).
# 	Step1	Given I navigate to login page.	"URL: https://d9-dev.commonsensemedia.org/user/login
# "	I see the login screen.
# 	Step2	When I enter invalid email and valid password	"Username: tngtestedito
# Pass:Et3sts!t3"	Then I see those credentials which I entered in the fields.
# 	Step3	And I click Sign in button		And I see the error message saying "Sorry, unrecognized username or password."
    def test_login_with_invalid_email_and_valid_password(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.Login("tngtestedito", "Et3sts!t3")
        login_page.login_check_homepage_not_showing()

        # ===========================AssertionError step 4 and step 5 ====================
        # 4	Test Case Title	As a user, I see the validation messages on email and password(for parents).
        # 	Step1	Given I navigate to login page.	URL: https://d9-dev.commonsensemedia.org/user/login	I see the login screen.
        # 	Step2	When I leave the credentials empty		Then I see those fields are empty.
        # 	Step3	And I click Sign in button		And I see that the validation message are showing on email and password.

    def test_login_see_the_validation_messages_on_email_and_password(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.check_empty_login()

    # 5	Test Case Title	As a user, I see the validation messages on invalid email and invalid password(for parents).
    # 	Step1	Given I navigate to login page.	URL: https://d9-dev.commonsensemedia.org/user/login	I see the login screen.
    # 	Step2	When I enter wrong email and wrong password	"Username: tngtesteditor1
    # Pass:Et3sts!t311"	Then I see the wrong credentials in email and password field
    # 	Step3	And I click Sign in button And I see that the validation message are showing on email and password.
    # FORGOT PASSWORD
    def test_see_the_validation_messages_on_invalid_email_and_invalid_password_parents(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.Login("tngtesteditor1", "Et3sts!t311")
        login_page.login_check_homepage_not_showing()
# 6	Test Case Title	As a user, I see that forgot password link is clickable.
# 	Step1	Given I navigate to login page.	URL: https://d9-dev.commonsensemedia.org/user/login	I see the login screen.
# 	Step2	When I click on "forgot password" link		Then I see that "forgot password" link is clickable and it
#               redirects me to "Reset your password" page.
    def test_login_see_that_forgot_password_link_is_clickable(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.visit_login_page()
        login_page.check_forget_password()


# 7	Test Case Title	As a user, I see the validation message on email.
#
# 	Step1	Given I navigate to forgot password page.	URL: https://d9-dev.commonsensemedia.org/user/password	I see the reset password page.
# 	Step2	When I leave the email field empty		Then I see the field is empty.
# 	Step3	And I click "Reset Password" button		And I see the validation message on email field.

    def test_login_see_the_validation_messages_on_email(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.visit_login_page()
        login_page.check_forget_password_email_empty()


# 8	Test Case Title	As a user, I am able to reset password with valid email.
# 	Step1	Given I navigate to forgot password page.	URL: https://d9-dev.commonsensemedia.org/user/password
#   	    I see the reset password page.
# 	Step2	When I enter the valid email		Then I see the credential which I entered in the field.
# 	Step3	And I click "Reset Password" button		"And it redirects me to login page along with success message saying ""We sent password reset instructions
# to the email address associated with your account.""
    def test_login_able_to_reset_password_with_valid_email(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.visit_login_page()
        login_page.check_forget_password_email_change("tngtesteditor")


# =====================================BUG=========================================
# 9	Test Case Title	As a user, I see the validation message on invalid email.
# 	Step1	Given I navigate to forgot password page.	URL: https://d9-dev.commonsensemedia.org/user/password	I see
#             the reset password page.
# 	Step2	When I enter invalid email in the email field	Email: asasasas	Then I see the invalid email entered in email field
# 	Step3	And I click "Reset Password" button		And I see the validation message on email field.
    def test_login_see_the_validation_messages_on_invalid_email(self):
        login_page = LoginPage.LoginPage(self.driver)
        login_page.visit_login_page()
        login_page.check_forget_password_email_not_change("asasasas")
# ======================BUG report for test case 9=====================================
#     when adding email:asasasas the validation message doesnot popup but says "We sent password reset instructions to the email address associated with your account."

    print("Doing this test case")


# =====================================Need GMAIL for verification  =========================
# 10	Test Case Title	As a user, I am able to see the reset password link in the given email.
# 	Step1	Given I navigate to forgot password page.	URL: https://d9-dev.commonsensemedia.org/user/password
# 	I see the reset password page.
# 	Step2	When I enter the valid email		Then I see the credential which I entered in the field.
# 	Step3	And I go the mail inbox		And I see the reset password link in the mail inbox

    # def test_login_see_the_reset_password_link_in_the_given_email(self):
    #     login_page = LoginPage.LoginPage(self.driver)
    #     login_page.visit_login_page()
    #     login_page.check_forget_password_email_not_change("tngtesteditor")
# ===================================================================================


# # REGISTER
# # 11	Test Case Title	As a user, I see that next button is showing disabled.
# # 	Step1	Given I navigate to register page.	URL: https://d9-dev.commonsensemedia.org/user/register	I see the signup page.
# # 	Step2	When I do not check the radio button on "Let's get started" section 		Then I see that next button is showing disabled.
#     def test_login_see_that_next_button_is_showing_disabled(self):
#         login_page = LoginPage.LoginPage(self.driver)
#         login_page.login_check("tngtesteditor", "Et3sts!t3")
#
#
# # 12	Test Case Title	As a user, I see that next button is showing enabled.
# # 	Step1	Given I navigate to register page.	URL: https://d9-dev.commonsensemedia.org/user/register	I see the signup page.
# # 	Step2	When I check the radio button on "Let's get started" section.		Then I see that next button gets enabled.
#     def test_login_see_that_next_button_is_showing_enabled(self):
#         login_page = LoginPage.LoginPage(self.driver)
#         login_page.login_check("tngtesteditor", "Et3sts!t3")
#
#
# # 13	Test Case Title	As a user, I see the validation message on password field.
# # 	Step1	Given I navigate to register page.	URL: https://d9-dev.commonsensemedia.org/user/register	I see the signup page.
# # 	Step2	When I check the "I'm a kid" radio button		Then I see that radio button gets checked.
# # 	Step3	And I click next button		And it redirects me to "Create your free account" page.
# # 	Step4	And I only enter the data into password field	Password: 123	"And I see the validation message saying ""Password must be at least 8 characters and include a capital
# # letter, a lowercase letter, and a number.""
#     def test_login_see_the_validation_message_on_password_field(self):
#         login_page = LoginPage.LoginPage(self.driver)
#         login_page.login_check("tngtesteditor", "Et3sts!t3")


# ===========================AssertionError step 4 and step 5 ====================


print("Here")
# =================================================================
# ==============================OLD tests==========================
#     def test_movie_remaining_view(self):
#         movies_tv_list = MovieAndTvPage.MovieAndTvPage(self.driver)
#         movies_tv_list.verifying_movies_and_tv_review()
#         movies_tv_list.verifying_movies_and_tv_second_review()
#         movies_tv_list.verifying_movies_and_tv_third_review()
    # def test_adding_deleting_kids(self):
    #     os.system('cls')
    #     adding_deleting_kids = PlusAddingDeletingKid.PlusAddingDeletingKid(self.driver)
    #     adding_deleting_kids.verifyingPlusAddingDeletingKid()
    # def test_plus_entertainment_age_limit(self):
    #     os.system('cls')
    #     entertainment_age_limit = PlusEntertainmentAgeLimitPage.PlusEntertainmentAgeLimitPage(self.driver)
    #     entertainment_age_limit.verifying_plus_entertainment_age_limit()
    # def test_free_kid_signup(self):
    #     adult_signup = CreateFreeKidSignupPage.CreateFreeKidSignupPage(self.driver)
    #     adult_signup.test_free_kid_signup()
    # def test_free_adult_signup(self):
    #     adult_signup = CreateFreeAdultSignupPage.CreateFreeAdultSignupPage(self.driver)
    #     adult_signup.test_free_adult_signup()
    # def test_free_teen_signup_for_us_and_international(self):
    #     teen_signup = CreateTeenAccountForUs_and_InternationalPage.CreateTeenAccountForUs_and_InternationalPage(
    #         self.driver)
    #     teen_signup.test_free_teen_signup_for_international()
    #     teen_signup.test_free_teen_signup_for_us()
    # def test_adding_kid_outside_manage_family_area(self):
    #     os.system('cls')
    #     plus_adding_kid = PlusAddingKidOutsideManageFamilyArea(self.driver)
    #     plus_adding_kid.verifyingAddingKidOutsideManageFamilyArea()
    # def test_get_it_now(self):
    #     stream = GetItNow.GetItNow(self.driver)
    #     stream.verifying_get_it_now()
    # def test_create_new_plus_membership(self):
    #     plus_adding_kid = CreateNewPlusMemberPage(self.driver)
    #     plus_adding_kid.verify_create_new_plus_member_account()
    # def test_filter_working_for_movie_book_and_game(self):
    #     plus_adding_kid = FilterWorkingForMovieBookAndGamePage(self.driver)
    #     plus_adding_kid.verify_filter_working_for_movie_book_and_game()
    #
    #
