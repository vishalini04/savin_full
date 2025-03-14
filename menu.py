from rich.console import Console # pip3 install Rich
from rich.table import Table
from speakListen import *


def print_menu():
    """Display a table with list of tasks and their associated commands.
    """
    speak("I can do the following")
    table = Table(title="\nI can do the following :- ", show_lines = True) 

    table.add_column("Sr. No.", style="cyan", no_wrap=True)
    table.add_column("Task", style="yellow")
    table.add_column("Command", justify="left", style="green")

    table.add_row("1", "Speak Text entered by User", "text to speech")
    table.add_row("2", "Search anything on Google", "Search on Google")
    table.add_row("3", "Search anything on Wikipedia", "Search on Wikipedia")
    table.add_row("4", "Read a MS Word(docx) document", "Read MS Word document")
    table.add_row("5", "Convert speech to text", "Convert speech to text")
    table.add_row("6", "Read a book(PDF)", "Read a book ")
    table.add_row("7", "Open WhatsApp", "open whatsapp")
    table.add_row("8", "Open Instagram", "open instagram")
    table.add_row("9", "Open Facebook", "open facebook")
    table.add_row("10", "Open Discord", "open discord")
    table.add_row("11", "Open Notepad", "open notepad")
    table.add_row("12", "Open Calculator", "open calculator")
    table.add_row("13", "Open Paint", "open paint")
    table.add_row("14", "Open YouTube", "open youtube")
    table.add_row("15", "Open Spotify", "open spotify")
    table.add_row("16", "Open Gmail", "open gmail")
    table.add_row("17", "Open File Explorer", "open file explorer")
    table.add_row("18", "Tell the Date", "What's the date?")
    table.add_row("19", "Tell the Time", "What's the time?")
    table.add_row("20", "Tell the Weather", "What's the weather?")
    table.add_row("21", "Quit the program", "Python close")

    console = Console()
    console.print(table)

#print_menu()