import fresh_tomatoes
import media

usual_suspects = media.Movie("The Usual Suspects", "Who is Keyser Soze?",
							 "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",  # NOQA
							 "https://youtu.be/oiXdPolca5w")  # NOQA

matrix = media.Movie("The Matrix", "A computer hacker has to choose: the blue or the red pill?",
					"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
					"https://youtu.be/vKQi3bBA1y8")  # NOQA 

movies=[usual_suspects, matrix]
fresh_tomatoes.open_movies_page(movies)
