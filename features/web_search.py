import webbrowser

import wikipedia
from wikipedia.exceptions import DisambiguationError

from assist import vass

wikipedia.set_lang(vass.language)

def get_query(text, keyword):
    keyword = keyword.lower()
    if keyword in text.lower():
        separated_phrases = text.split(keyword)
        print(separated_phrases)
        return separated_phrases[1]
    else:
        return "Ошибка в распознавании ключевого слова"

def google_request(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)

def youtube_request(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open_new_tab(url)

def google_search(text, keyword):
    query = get_query(text, keyword)
    google_request(query)
    vass.say(f'Запускаю поиск по запросу {query}')
    

def youtube_search(text, keyword):
    query = get_query(text, keyword)
    youtube_request(query)
    vass.say(f'Запускаю поиск по запросу {query}')

def wiki_search(text, keyword):
    query = get_query(text, keyword)
    #url = f"https://ru.wikipedia.org/wiki/{query}"
    vass.say(f'Готовлю ответ по запросу {query}')

    try:
        wiki_summary= wikipedia.summary(query)
    except DisambiguationError:
        vass.say(f'Найдено несколько статей с запросом {query}')
        return

    vass.say(wiki_summary)
    

if __name__ == "__main__":
    
    text1="Найди в гугл породы собак"
    text2="Найди в гугл"
    query = get_query(text1, text2)
    search_google(query)

