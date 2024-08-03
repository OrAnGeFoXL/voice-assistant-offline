from features.start_application import start_app
from features.kill_application import kill_app
from features.web_search import youtube_search, wiki_search,google_search


command_keywords = {
    "start_app": ["Запусти", "Открой", "Запустить" ],
    "close_app": ["Закрой", "Закрыть", "Выключи"],
    "google_search": ["загугли", "Найди в google", "Найди в Гугле", "Найди в интернете"],
    "youtube_search": ["Ютубе","Ютуби", "youtube", "Найди в Youtube", "Найди видео"],
    "wiki_search": ["Найди в Википедии", "Найди в википедии"]
}


def start_routing(text):

    #Преобразование текста в нижний регистр
    text = text.lower()

    # Проверка каждого ключевого слова для каждого приложения в словаре на наличие в тексте
    for command, keywords in command_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text:
               if command == "start_app":
                   print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{command} \033[92mнайдено\033[0m в тексте.")
                   start_app(text)
                   return
                   
               elif command == "close_app":
                   print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{command} \033[92mнайдено\033[0m в тексте.")
                   kill_app(text)
                   return

               elif command == "google_search":
                   print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{command} \033[92mнайдено\033[0m в тексте.")
                   google_search(text, keyword)
                   return

               elif command == "youtube_search":
                   print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{command} \033[92mнайдено\033[0m в тексте.")
                   youtube_search(text, keyword)
                   return

               elif command == "wiki_search":
                   print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{command} \033[92mнайдено\033[0m в тексте.")
                   wiki_search(text, keyword)
                   return

        else:
            print(f"Ключевые слова \033[94m{keywords}\033[0m для \033[93m{command} \033[91mне найдены\033[0m в тексте.")


if __name__ == "__main__":

    text="Закрой Телеграм"
    start_routing(text)

                