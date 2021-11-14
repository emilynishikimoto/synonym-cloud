import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.thesaurus.com/"


def _get_synonyms_from(url: str) -> list:
    """Get synonyms from the given url.

    :param url: url with search term
    :return: empty list if synonyms not found
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    try:
        synonym_container = soup.find("div", {"id": "meanings"})
        lis = synonym_container.find_all("li")

        synonyms = []
        for li in lis:
            synonyms.append(li.text)
        return synonyms
    except AttributeError:
        return []


def get_synonyms() -> list:
    """Get synonyms of a user input.

    :return: list of synonyms
    """
    search_term = input("Search: ").lower()
    search_url = f"{BASE_URL}browse/{search_term}"
    synonyms = _get_synonyms_from(search_url)
    return synonyms


if __name__ == "__main__":
    get_synonyms()
