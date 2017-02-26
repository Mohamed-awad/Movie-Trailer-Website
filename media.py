import webbrowser


class Movie():
    """  this class provide a way to store movie related information  """
# the function that intialize all class variable
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# the function that display the movie trailer on youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
