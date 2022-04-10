from selenium import webdriver
import unittest
from lib.utils.urls import Url
from lib.pages_screen import CreateFreeKidSignupPage, CreateFreeAdultSignupPage, CreateTeenAccountForUs_and_InternationalPage
from tests import Init


class TestCreateFreeKidSignupPage(Init):

    def test_free_kid_signup(self):
        adult_signup = CreateFreeKidSignupPage.CreateFreeKidSignupPage(self.driver)
        adult_signup.test_free_kid_signup()
