import webbrowser


# defines Movie class, metadata & function to show the trailer

class Movie():
    """
    Stores film metadata for each film instance
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url, movie_date, movie_stars):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.date = movie_date
        self.stars = movie_stars


# opens browers and plays film trailer

def show_trailer(self):
    """
    plays film trailer
    input is film instance
    output is film trailer
    """
    webbrowser.open(self.trailer_youtube_url)
