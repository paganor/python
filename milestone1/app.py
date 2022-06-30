MENU_PROMPT = "\nEnter 'a' to add a move, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []
user_selection = input(MENU_PROMPT)


def addMovie():
    movies.append({
        'title': input("Enter the movie title: "),
        'director': input("Enter the movie director: "),
        'year': input("Enter the movie release year: ")
    })


def printMovie(movie):
    print(
        f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")


def findMovie(title):
    for movie in movies:
        if title.lower() == movie["title"].lower():
            printMovie(movie)
            break
    else:
        print(f"No movie matching '{title}'")


def printMovies():
    if len(movies) == 0:
        print("No movies yet :(")
    else:
        for movie in movies:
            printMovie(movie)


while user_selection != 'q':
    if user_selection == 'a':
        addMovie()
    elif user_selection == 'l':
        printMovies()
    elif user_selection == 'f':
        selection = input("Enter movie title: ")
        findMovie(selection)
    else:
        print("Unknown command. Please try again")

    user_selection = input(MENU_PROMPT)
