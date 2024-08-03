import subprocess
import os

from assist import vass

# Создание словаря с названиями приложений и ключевыми словами
app_keywords = {
    "telegram-desktop": ["Телеграм", "Телеграмм", "Telegram"],
    "obsidian": ["обсидиан", "заметки", "блокнот", "планер"],
    "thunar": ["файловый менеджер", "проводник", "тюнар", "тюнер"],
    "code-oss": ["vs code", "vscode", "висикод", "вскод", "IDE"],
    "alacritty": ["алакритти", "консоль", "терминал"],
}

def run_application(application_name):
    subprocess.Popen(["/usr/bin/{}".format(application_name)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Запуск приложения {application_name} завершен.")

def start_app(text):

# Проверка каждого ключевого слова для каждого приложения в словаре
    for app, keywords in app_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():

                print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{app} \033[92mнайдено\033[0m в тексте.")
                vass.say(f'Запускаю {app}')
                run_application(app)
                return
    vass.say('Не могу разобрать какое приложение вы хотите запустить')

if __name__ == "__main__":
    pass


