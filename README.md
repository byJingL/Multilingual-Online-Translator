# Multilingual Online Translator
This program can translate words to many languages and give you many usage examples at the same time.

Supported Languages: Arabic, German, English, Spanish, French, Hebrew, Japanese, Dutch, Polish, Portuguese, Romanian, Russian, Turkish
## Main Skill
Web scraping, BeautifulSoup, argparser module, requests module, 
## Theory
- Input arguments from terminal are parsed using argparse module
- The word to translate is then translated by [ReversoContext](https://context.reverso.net/translation/)
- The results are scraping by BeautifulSoup library
## How to use
- Download [translator.py](/translator.py) and install required modules
- Run [translator.py](/translator.py) with 3 arguments:
  -  Original language
  -  Language to translate to
  -  Word to be translated
-  Examples:  
    Translate `hello` from english to frencn
    ```
    python3 translator.py english french hello
    ```
    Translate `hello` from english to all support languages
    ```
    python3 translator.py english all hello
    ```

## Example
```
> python3 translator.py english japanses hello
Japanese Translations:
こんにちは

Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。
```

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.