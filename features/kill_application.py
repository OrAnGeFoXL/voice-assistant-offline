import subprocess
import os
import psutil

from assist import vass

# Создание словаря с названиями приложений и ключевыми словами
app_keywords = {
    "telegram-desktop": ["Телеграм", "Телеграмм", "Telegram"],
    "obsidian": ["обсидиан", "заметки", "блокнот", "планер"],
    "thunar": ["файловый менеджер", "проводник", "тюнар", "тюнер"],
    "firefox": ["Браузер", "Интернет", "Firefox", "Fire fox", "Файерфокс"],
    "code-oss": ["vs code", "vscode", "висикод", "вскод", "IDE"],
}

def get_processes_by_name(name):
   """Return a list of processes matching 'name'."""
   matching_processes = [proc for proc in psutil.process_iter(['name']) if proc.info['name'] == name]
   return matching_processes

def kill_processes(processes):
   """Attempt to kill all 'processes'."""
   for proc in processes:
      try:
         proc.kill()
      except psutil.NoSuchProcess:
         print(f"No such process: {proc.pid}")
      except psutil.AccessDenied:
         print(f"Access denied to {proc.pid}")


def kill_application(application_name):
  
    processes_to_kill = get_processes_by_name(application_name)
    kill_processes(processes_to_kill)

    print(f"Приложение {application_name} завершено.")


def kill_app(text):

# Проверка каждого ключевого слова для каждого приложения в словаре на наличие в тексте
    for app, keywords in app_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text.lower():
                # Выполнить действие для соответствующего приложения
                print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{app} \033[92mнайдено\033[0m в тексте.")
                vass.say(f'Завершаю процесс {app}')
                kill_application(app)               
                return

            else:
                print(f"Ключевое слово \033[94m{keyword}\033[0m для \033[93m{app} \033[91m не найдено\033[0m в тексте.")
        
    morgana.say('Не могу разбрать какую команду вы хотите завершить')


if __name__ == "__main__":
    pass


