#"webbrowser" is a python module that allows end users to see web based documents

import webbrowser

#below code defines class "Movie" and its functions to be used to simplify coding for web page
#"__init__" contains the content space for the page
#"show_trailer" contains the ability to open web page when poster is clicked

class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
