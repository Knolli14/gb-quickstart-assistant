
from gbextractor.params import URL
from gbextractor.extract import get_games, download_pdfs
from gbextractor.data import save_games_list


def main():
    save_games_list(get_games(URL))
    download_pdfs()

if __name__ == "__main__":

    main()
