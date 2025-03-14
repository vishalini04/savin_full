import json
import time
import random
from speakListen import speak

# Load streak data (Persistent storage)
def load_streaks():
    try:
        with open("streaks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"focus_streak": 0, "word_score": 0, "best_reaction": None}

# Save streak data
def save_streaks(data):
    with open("streaks.json", "w") as f:
        json.dump(data, f)

streak_data = load_streaks()

def focus_timer(duration=25):
    """Focus Timer Game with Streak Tracking."""
    speak(f"Starting a {duration}-minute focus session. Stay focused!")
    time.sleep(duration * 60)  # Simulate focus time
    streak_data["focus_streak"] += 1
    save_streaks(streak_data)
    speak(f"Great job! Your focus streak is now {streak_data['focus_streak']}.")

def word_guessing_game():
    """Word Guessing Game with Score Tracking."""
    words = ["python", "assistant", "developer", "savin", "technology"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 4

    while attempts > 0 and "_" in guessed:
        speak("Current word: " + " ".join(guessed))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            streak_data["word_score"] += 10
        else:
            attempts -= 1

    save_streaks(streak_data)
    speak(f"Game over! Your total word score is {streak_data['word_score']}.")

def reaction_speed_test():
    """Reaction Speed Test with Best Time Tracking."""
    speak("Get ready! Wait for the signal...")
    time.sleep(random.randint(2, 5))
    speak("NOW! Press Enter as fast as you can!")
    
    start_time = time.time()
    input()
    reaction_time = round(time.time() - start_time, 2)

    if not streak_data["best_reaction"] or reaction_time < streak_data["best_reaction"]:
        streak_data["best_reaction"] = reaction_time
        speak(f"New best time! {reaction_time} seconds.")
    else:
        speak(f"Your reaction time was {reaction_time} seconds.")

    save_streaks(streak_data)

def play_game():
    """Game Selection Menu."""
    speak("Which game would you like to play? Focus Timer, Word Guessing, or Reaction Speed Test?")
    choice = input("Choose a game (focus/word/reaction): ").lower()
    
    if "focus" in choice:
        focus_timer()
    elif "word" in choice:
        word_guessing_game()
    elif "reaction" in choice:
        reaction_speed_test()
    else:
        speak("I didn't understand that. Please choose again.")
        play_game()

# Uncomment to test individual games
# play_game()
