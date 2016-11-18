import fresh_tomatoes
import media

usual_suspects = media.Movie("The Usual Suspects", "Who is Keyser Soze?",
							 "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",  # NOQA
							 "https://youtu.be/oiXdPolca5w",  # NOQA
							 "1995",
							 "Kevin Spacey, Gabriel Byrne, Chazz Palminteri")

matrix = media.Movie("The Matrix", "A computer hacker has to choose: the blue or the red pill?",
					"https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
					"https://youtu.be/vKQi3bBA1y8",  # NOQA 
					"1999",
					"Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

shawshank_redemption = media.Movie("The Shawshank Redemption", 
	"Two imprisoned men bond over a number of years, finding solace and eventual redemption", 
	"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  #NOQA
	"https://youtu.be/6hB3S9bIaco",  #NOQA
	"1994", 
	"Tim Robbins, Morgan Freeman")

big_lebowski = media.Movie("The Big Lebowski", 
	"'The Dude' abides...",
	"https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",  #NOQA
	"https://youtu.be/cd-go0oBF4Y",  #NOQA
	"1998", 
	"Jeff Bridges, John Goodman, Julianne Moore")

momento = media.Movie("Momemto", 
	"A man creates a strange system to help him remember things...",
	"https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",  #NOQA
	"https://youtu.be/zgd0-VttkmA",  #NOQA
	"2000", 
	"Guy Pearce, Carrie-Anne Moss, Joe Pantoliano")

movies=[usual_suspects, matrix, shawshank_redemption, big_lebowski, momento]
fresh_tomatoes.open_movies_page(movies)
