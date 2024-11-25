
from params import URL
from pdf_extractor.extract import get_games, download_pdfs
from pdf_extractor.data import save_games_list


def main():
    save_games_list(get_games(URL))
    download_pdfs()

if __name__ == "__main__":

    main()
