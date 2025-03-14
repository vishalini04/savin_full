from speakListen import greet, hear
from speakListen import speak,hear
import wikipedia
import webbrowser


def google_search(query=None):
    """Opens Google in the default browser and searches the given query."""
    google_search_link = "https://www.google.com/search?q="
    print(google_search)
    speak(google_search)
    
    query = hear()

    if query != "None":
        webbrowser.open(google_search_link+query)
    elif query == "None":
        print("I could'nt understand what you just said!")
        speak("I could'nt understand what you just said!")

def wiki_search(query=None):
    """Searches Wikipedia for the asked topic."""
    if query is None:  # If no query is given, ask the user
        speak("What do you want to search on Wikipedia?")
        query = hear().lower()

    if query:
        try:
    # Your code that might cause an error
            print("Trying something risky...")
            result = 10 / 0  # Example risky code

        except Exception as e:  # ✅ Correct Syntax
            print(f"An error occurred: {e}")
            
def search_youtube(query):
    """Searches for a query on YouTube."""
    youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    speak(f"Searching for {query} on YouTube.")
    webbrowser.open(youtube_url)


#wiki_search()
#google_search()