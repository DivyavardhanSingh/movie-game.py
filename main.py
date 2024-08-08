import random

# List of movies
movies = [
    "Inception", "Avatar", "Titanic", "The Matrix", "Gladiator", 
    "Jurassic Park", "The Godfather", "Pulp Fiction", "The Shawshank Redemption"
]

# Function to hide movie name with a few letters revealed
def hide_movie(movie):
    hidden_movie = ""
    for i, char in enumerate(movie):
        if char.lower() in ['a', 'e', 'i', 'o', 'u'] or i % 2 == 0:
            hidden_movie += char
        else:
            hidden_movie += "_"
    return hidden_movie

# Function to play the game
def play_game():
    movie = random.choice(movies).lower()  # Choose a random movie and convert it to lowercase
    hidden_movie = hide_movie(movie)  # Get the hint
    attempts = 5  # Number of attempts
    
    print("Welcome to the Movie Guessing Game!")
    print("You have to guess the movie name based on the hint.")
    print(f"Hint: {hidden_movie}")

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        
        if guess == movie:
            print("Congratulations! You guessed the movie correctly.")
            break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
            if attempts == 0:
                print(f"Game Over! The movie was '{movie.title()}'.")
            else:
                print(f"Hint: {hidden_movie}")
                
if __name__ == "__main__":
    play_game()
