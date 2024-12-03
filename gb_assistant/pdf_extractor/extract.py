import requests
from bs4 import BeautifulSoup
from gb_assistant.pdf_extractor.data import load_games_list, save_pdf


def get_soup(url, page=1):
    ''' Extract hmtl-presentation of search page'''

    response = requests.get(url+str(page))

    return BeautifulSoup(response.content, "html.parser")


def get_games_info(soup, language="English"):
    ''' Extract <a href=... class=...> elements of a page, 12 per page '''

    return soup.find_all(
        class_="btn btn-sm btn-secondary mb-1",
        title="In "+language
    )


def extract_game(game_info):
    ''' '''

    url = game_info.get("href")
    title = _extract_title(url)

    print("Extracted", title)
    return {
        "url": url,
        "title": title
    }


def _extract_title(url):
    ''' Extract title out of link'''

    title_full = url.split("/")[-1] \
                    .strip(".pdf")

    return " ".join(title_full.split("-")[1:-1])


# to be fixed: Change page range
def get_games(url,  language="English"):
    ''' Extracts title and download url of all games'''

    games_list = []

    for page in range(395): # substitute for dyn.solution
        print("Extracting from page", page+1)
        soup = get_soup(url, page)

        for game_info in get_games_info(soup, language=language):
            games_list.append(extract_game(game_info))

    return games_list


def download_pdfs():
    ''' Download all the pdfs '''
    games_list = load_games_list()

    for game in games_list["games"]:

        content = requests.get(game["url"]).content
        save_pdf(content, game["title"])

    print("PDFs downloaded!")
