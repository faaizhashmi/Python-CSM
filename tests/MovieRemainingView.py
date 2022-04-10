from lib.pages_screen import MovieAndTvPage
from tests import Init


class MovieRemainingView(Init):

    def testMovieRemainingView(self):
        moviesTvList = MovieAndTvPage.MovieAndTvPage(self.driver)
        moviesTvList.verifying_movies_and_tv_review()
        moviesTvList.verifying_movies_and_tv_second_review()
        moviesTvList.verifying_movies_and_tv_third_review()
