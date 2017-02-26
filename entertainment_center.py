import media
import fresh_tomatoes


""" all this classes are are my favorite movies that display in web page"""

# code of toy story movie
ss = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life ",
                        ss,
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
# end of code of toy story movie

# code of avater movie
ss1 = "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg"
avatar = media.Movie("Avatar",
                     "A marine on an alien planet ",
                     ss1,
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# end of code of avatar movie

# code of kubo and the two strings movie
ss2 = "https://upload.wikimedia.org/wikipedia/en/"
"c/c4/Kubo_and_the_Two_Strings_poster.png"
kubo = media.Movie("Kubo and the Two Strings",
                   "boy story",
                   ss2,
                   "https://www.youtube.com/watch?v=p4-6qJzeb3A")
# end of code of kubo and the two strings movie

# code of school of rock movie

school_of_rock = media.Movie("School of rock",
                             "story line",
                             "https://upload.wikimedia.org/wikipedia"
                             "/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
# end of code of school of rock movie

# code of ratatouille movie

ratatouille = media.Movie("Ratatouille",
                          "story line",
                          "https://upload.wikimedia.org/wikipedia/"
                          "en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# end of code of ratatouille movie

# code of midnight in paris movie

midnight_in_paris = media.Movie("Midnight_in_paris",
                                "story line",
                                "https://upload.wikimedia.org/wikipedia/"
                                "en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

# end of code of midnight in paris movie

# code of hunger games movie

hunger_games = media.Movie("Hunger Games",
                           "story line",
                           "https://upload.wikimedia.org/wikipedia/"
                           "en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# end of code of hunger games movie

# code of harry potter movie

harry_potter = media.Movie("Harry Potter",
                           "Magic",
                           "https://upload.wikimedia.org/wikipedia/en/c/c9/"
                           "Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                           "https://www.youtube.com/watch?v=geNlXmmIp7w")

# end of code of harry potter movie

# code of Dilwale Dulhaniya Le Jayenge movie
str1 = "https://upload.wikimedia.org/wikipedia/"
"en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg"
dilwale = media.Movie("Dilwale Dulhaniya Le Jayenge",
                      "Love",
                      str1,
                      "https://www.youtube.com/watch?v=c25GKl5VNeY&vl=en")
# end of code of Dilwale Dulhaniya Le Jayenge movie

# all my favorite movie in this list movies
movies = [toy_story, avatar, kubo, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games, harry_potter, dilwale]

# the file fresh_tomatoes that is used to run the project in web page
fresh_tomatoes.open_movies_page(movies)
