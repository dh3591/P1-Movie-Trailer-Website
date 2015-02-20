#related files need to be imported for program to work.
#"fresh_tomatoes" takes python code and converts to HTML webpage.
#"media" holds the information to define class "Movie".

import fresh_tomatoes
import media

#list of three instances of class Movie for website display.
#each instance defines the three elements of the class Movie (movie_title, poster_image, trailer_youtube).

gone_60sec = media.Movie("Gone In 60 Seconds",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/2/2a/Gone_in_sixty_seconds.jpg/220px-Gone_in_sixty_seconds.jpg",
                         "https://www.youtube.com/watch?v=o6AyAM1buQ8")

biker_boyz = media.Movie("Biker Boyz",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Biker_boyz_poster.jpg/220px-Biker_boyz_poster.jpg",
                         "https://www.youtube.com/watch?v=BPAFue9tDhU")

fast7 = media.Movie("Fast & Furious 7",
                    "http://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg",
                    "https://www.youtube.com/watch?v=QgZlDFnEozw")

#"movies" is the array built for "fresh_tomatoes" to utilize when rendering webpage.

movies = [gone_60sec, biker_boyz, fast7]
fresh_tomatoes.open_movies_page(movies)

                     

