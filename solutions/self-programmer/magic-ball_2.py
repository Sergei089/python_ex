import random
import time

# по примеру https://rubyrush.ru/steps/magic-ball

ans = [
  # Положительные
  "Бесспорно",
  "Предрешено",
  "Никаких сомнений",
  "Определённо да",
  "Можешь быть уверен в этом",

  # Нерешительно положительные
  "Мне кажется — «да»",
  "Вероятнее всего",
  "Хорошие перспективы",
  "Знаки говорят — «да»",
  "Да",

  # Нейтральные
  "Пока не ясно, попробуй снова",
  "Спроси позже",
  "Лучше не рассказывать",
  "Сейчас нельзя предсказать",
  "Сконцентрируйся и спроси опять",

  # Отрицательные
  "Даже не думай",
  "Мой ответ — «нет»",
  "По моим данным — «нет»",
  "Перспективы не очень хорошие",
  "Весьма сомнительно"
]
answers = list(ans)

# print((ans[0]))

txt = input("Введите число от 0 до 19\n")
index = int(txt)

print("")

replic = ans[int(index)]
list_replic = list(replic)


print(list_replic)
# time.sleep(1.5)
# print(replic)

def getReplic():
  for index in list_replic:
    #time.sleep(1)

    print(index)
    index += 1

getReplic()



  