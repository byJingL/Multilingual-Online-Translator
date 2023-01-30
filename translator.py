import requests
from bs4 import BeautifulSoup
URL = "https://context.reverso.net/translation"
LANGUAGE = {
    'en': 'english',
    'fr': 'french',
}


def get_response(url, headers):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.status_code, 'OK')
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def main():
    target_language = input('Type "en" if you want to translate from French into English, '
                            'or "fr" if you want to translate from English into French:\n')
    word = input('Type the word you want to translate:\n')
    print(f'You chose "{target_language}" as a language to translate "{word}".')

    headers = {
        'User-Agent': 'Mozilla/5.0',
    }

    if target_language == 'fr':
        target_url = f'{URL}/english-french/{word}'
    if target_language == 'en':
        target_url = f'{URL}/french-english/{word}'

    soup = get_response(target_url, headers)
    word_tags = soup.find_all(name='span', class_='display-term')
    word_list = []
    for item in word_tags:
        word_list.append(item.text)

    from_tags = soup.find_all(name='div', class_='src ltr')
    from_list = []
    for item in from_tags:
        from_list.append(item.text.strip())

    to_tags = soup.find_all(name='div', class_='trg ltr')
    to_list = []
    for item in to_tags:
        to_list.append(item.text.strip())

    print(f'\n{LANGUAGE[target_language].capitalize()} Translations:')
    for word in word_list[0:5]:
        print(word)
    print(f'\n{LANGUAGE[target_language].capitalize()} Examples:')
    for i in range(5):
        print(from_list[i])
        print(f'to_list[i]\n')


if __name__ == '__main__':
    main()