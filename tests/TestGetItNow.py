
from selenium import webdriver
import unittest
from lib.pages_screen import GetItNow
from lib.utils.urls import Url
from tests import Init


class MovieStream(Init):


    def testMovieStream(self):
        stream = GetItNow.GetItNow(self.driver)
        stream.verifying_get_it_now()

