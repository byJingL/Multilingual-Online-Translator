import requests
from bs4 import BeautifulSoup

URL = "https://context.reverso.net/translation"
LANGUAGE = {
    '1': 'Arabic',
    '2': 'German',
    '3': 'English',
    '4': 'Spanish',
    '5': 'French',
    '6': 'Hebrew',
    '7': 'Japanese',
    '8': 'Dutch',
    '9': 'Polish',
    '10': 'Portuguese',
    '11': 'Romanian',
    '12': 'Russian',
    '13': 'Turkish',
}


def get_input():
    print('Hello, welcome to the translator. Translator supports:\n')
    for key in LANGUAGE:
        print(f'{key}: {LANGUAGE[key]}')

    # Get from language num
    while True:
        from_num = input('Type the number of your language:\n')
        if from_num.isdigit() and 1 <= int(from_num) <= 13:
            break
        else:
            print('Invalid input!')

    # Get to language num
    while True:
        to_num = input('Type the number of your language:\n')
        if to_num.isdigit() and 0 <= int(to_num) <= 13:
            break
        else:
            print('Invalid input!')

    word = input('Type the word you want to translate:\n')
    return from_num, to_num, word


def get_response(url):
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    # print(response.status_code, 'OK')
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


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

    user_input = get_input()
    from_num = user_input[0]
    to_num = user_input[1]
    word = user_input[2]

    from_language = LANGUAGE[from_num]
    to_languages = []
    if to_num != '0':
        to_languages.append(LANGUAGE[to_num])
    else:
        for key in LANGUAGE:
            if key != from_num:
                to_languages.append(LANGUAGE[key])

    if len(to_languages) == 1:
        target_url = f'{URL}/{from_language.lower()}-{to_languages[0].lower()}/{word}'
        soup = get_response(target_url)

        contains = get_info(soup, 'multi_lines')

        with open(f'{word}.txt', 'a') as file:
            file.write(f'\n{to_languages[0]} Translations:\n')
            for item in contains[0][0:5]:
                file.write(f'{item}\n')
            file.write(f'\n{to_languages[0]} Examples:\n')
            for i in range(5):
                file.write(f'{contains[1][i]}\n')
                file.write(f'{contains[2][i]}\n\n')

    else:
        for to_language in to_languages:
            target_url = f'{URL}/{from_language.lower()}-{to_language.lower()}/{word}'
            soup = get_response(target_url)

            contain = get_info(soup, 'single_line')
            with open(f'{word}.txt', 'a') as file:
                file.write(f'{to_language} Translations:\n{contain[0]}\n')
                file.write(f'\n{to_language} Examples:\n{contain[1]}:\n{contain[2]}\n\n\n')

    with open(f'{word}.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            print(line, end='')


if __name__ == '__main__':
    main()
