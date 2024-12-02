
from gb_assistant.pdf_extractor.extract import get_games, download_pdfs
from gb_assistant.pdf_extractor.data import save_games_list

URL = "https://en.1jour-1jeu.com/rules/search?page="

def main():
    #save_games_list(get_games(URL))
    download_pdfs()

if __name__ == "__main__":

    main()
