import requests
from bs4 import BeautifulSoup
import argparse

URL = "https://context.reverso.net/translation"
LANGUAGE = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
            'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']


def get_response(from_, to_, word):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    url = f'{URL}/{from_}-{to_}/{word}'
    response = requests.get(url, headers=headers)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    elif response.status_code == 404:
        print(f"Sorry, unable to find {word}")
        quit()
    else:
        print('Something wrong with your internet connection')
        quit()


def get_info(soup, mode):
    if mode == 'multi_lines':
        word_tags = soup.find_all(name='span', class_='display-term')
        word_list = []
        for item in word_tags:
            word_list.append(item.text)

        from_tags = soup.find_all(name='div', class_='src')
        from_list = []
        for item in from_tags:
            from_list.append(item.text.strip())

        to_tags = soup.find_all(name='div', class_='trg')
        to_list = []
        for item in to_tags:
            to_list.append(item.text.strip())

        return word_list, from_list, to_list

    if mode == 'single_line':
        word = soup.find(name='span', class_='display-term').text
        from_example = soup.find(name='div', class_='src').text.strip()
        to_example = soup.find(name='div', class_='trg').text.strip()
        return word, from_example, to_example


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("from_language", default=None)
    parser.add_argument("to_language", default=None)
    parser.add_argument("word", default=None)

    args = parser.parse_args()
    from_language = args.from_language.lower()
    to_language = args.to_language.lower()
    word = args.word.lower()

    if from_language.title() not in LANGUAGE:
        print(f"Sorry, the program doesn't support {from_language}")
        quit()

    if to_language == 'all':
        for item in LANGUAGE:
            if item.lower() != from_language:
                soup = get_response(from_language, item.lower(), word)

                contain = get_info(soup, 'single_line')
                with open(f'{word}.txt', 'a') as file:
                    file.write(f'{item.capitalize()} Translations:\n{contain[0]}\n')
                    file.write(f'\n{item} Examples:\n{contain[1]}:\n{contain[2]}\n\n\n')
    elif to_language.title() in LANGUAGE:
        soup = get_response(from_language, to_language, word)

        contains = get_info(soup, 'multi_lines')
        with open(f'{word}.txt', 'a') as file:
            file.write(f'\n{to_language.capitalize()} Translations:\n')
            for item in contains[0]:
                file.write(f'{item}\n')
            file.write(f'\n{to_language} Examples:\n')
            for i in range(min(len(contains[1]), len(contains[2]))):
                file.write(f'{contains[1][i]}\n')
                file.write(f'{contains[2][i]}\n\n')
    else:
        print(f"Sorry, the program doesn't support {to_language}")
        quit()

    with open(f'{word}.txt', 'r') as file:
        print(file.read())


if __name__ == '__main__':
    main()
