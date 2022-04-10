from lib.pages_screen.FilterWorkingForMovieBookAndGamePage import FilterWorkingForMovieBookAndGamePage
from tests import Init


class FilterWorkingForMovieBookAndGameTest(Init):

    def test_filter_working_for_movie_book_and_game(self):
        plus_adding_kid = FilterWorkingForMovieBookAndGamePage(self.driver)
        plus_adding_kid.verify_filter_working_for_movie_book_and_game()