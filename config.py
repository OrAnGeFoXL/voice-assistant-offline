#Файл содержит основные настройки голосового ассистента

#Микрофон
sample_rate = 48000
chunk_size = 4096
device_index = 7    #Установите индекс устройства, чтобы использовать ваше микрофон sr.Microphone.list_microphone_names()

#Распознавание речи
recognize_language = 'ru-RU'
online_recognize = False

#Голосовой ассистент
language = 'ru'
bye_phrase = 'Пока'     #Фраза деактиивации ассистента

master_name = 'Хозяин'  #Как ассистент будет обращаться к вам