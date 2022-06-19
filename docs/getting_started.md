---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(getting_started)=

# Установка `python`


## `python` vs Anaconda

Установить `python` можно сам по себе или в составе дистрибутива. При этом в научной среде не редко предпочитают устанавливать [Anaconda](https://www.anaconda.com/what-is-anaconda/), которая помимо самого `python` включает в себя
- пакетный менеджер [conda](https://docs.conda.io/en/latest/);
- приложение `Anaconda Navigator`, которое позволяет запускать приложения, устанавливать дополнительные библиотеки, настраивать окружения и др.;
- среду разработки [spyder](https://www.spyder-ide.org/);
- ряд предустановленных популярных научных библиотек, таких как `NumPy`, `Matplotlib`, `Pandas`, `jupyterlab` и т.п.;
- и др.

Если вы установите `Anaconda`, то у вас автоматически будут установленны совместимые версии всех библиотек, которые вам потребуются в первом семестре нашего курса. Было время, когда нередко встречались проблемы с совместимостями сторонних библиотек при использовании стандартных средств `python`, а `Anaconda` собирала и распространяла набор заведомо совместимых между собой версий библиотек. 

Тем не менее назвать `Anaconda` незаменимым нельзя даже для научных целей. Автор курса предпочитает устанавливать `python` сам по себе и устанавливать библиотеки по мере необходимости, используя пакетный менеджер [PyPI](https://pypi.org/), который поставляется с `python`. Сегодня `PyPI` справляется с зависимостями не хуже `conda`, но такой подход требует некоторого уровня знакомства с командной строкой. 



(install_anaconda)=
## Anaconda

### Установка

Чтобы установить, [скачайте](https://www.anaconda.com/products/individual) установщик и следуйте инструкциям.


```{note}
Установите последнюю версию!
```


```{toggle} 
![](/_static/lecture_specific/getting_started/anaconda-setup-1.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-2.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-3.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-4.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-5.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-6.png)

![](/_static/lecture_specific/getting_started/anaconda-setup-7.png)
```

После установки запустите приложение `Anaconda Navigator` (обновите его, если выскочит предложение) и вы должны увидеть следующее окно.

```{figure} /_static/lecture_specific/getting_started/navigator.png
```

### Обновление

Не лишним будет сразу после установки обновиться. Для этого познакомимся с инструментом `Anaconda prompt`, который по сути дела представляет из себя командную строку с рядом надстроек для управления `Anaconda`. Запустить `Anaconda prompt` можно из `Anaconda Navigator` выбрав пункт "`CMD.exe Prompt`" или набрав в поиске "`Anaconda prompt`". В открывшейся командной строке наберите следующую команду и нажмите клавишу `Enter`.

```sh
conda update anaconda
```

```{figure} /_static/lecture_specific/getting_started/conda_update.gif
```

Больше информации о `conda` можно получить набрав `conda help`.

### Тестирование работоспособности `python`

Проверить работоспособность `python` в составе `Anaconda` можно также из "`Anaconda prompt`". Наберите следующую команду и если в ответ появится сообщение с версией `python`, то установка прошла успешно.

```python
python -V
```

```{figure} /_static/lecture_specific/getting_started/conda_test.gif
```

В данном примере версия установленного `python` --- 3.9.7.

## CPython

### Установка 

В качестве альтернативы можно установить `python` сам по себе. Для этого необходимо скачать установщик с официального сайта, запустить его и следовать инструкциям. Рекомендуется поставить галочку напротив пункта "Add Python 3.X to PATH".

```{toggle} 
![](/_static/lecture_specific/getting_started/python-install-1.png)

![](/_static/lecture_specific/getting_started/python-install-2.png)
```

### Обновление

После установки в качестве упражнения из командной строки обновите пакетный менеджер `PyPI` следующей командой.

```sh
python -m pip install update pip
```

```{figure} /_static/lecture_specific/getting_started/pip_update.gif
```

### Тестирование работоспособности `python`

 Наберите следующую команду и если в ответ появится сообщение с версией `python`, то установка прошла успешно.

```sh
python -V
```

```{figure} /_static/lecture_specific/getting_started/python_test.gif
```
(python_hello_world)=

