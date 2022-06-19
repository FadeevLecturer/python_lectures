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


(ipython_notebook)=

# Что такое Jupyter Notebooks?

[Jupyter](http://jupyter.org/) notebooks (блокноты, тетрадки) --- ещё один способ интерактивно работать с python. Он объединяет в себе возможность сохранять код и многократно его использовать и возможность интерактивного взаимодействия с интерпретатором python. Кроме того, помимо исходного кода python в jupyter notebook могут быть встроены форматированный текст, таблицы, изображения, анимация, математические формулы и многое другое.

Благодаря таким особенностям, тетрадки сейчас очень популярны в науке, особенно в сфере анализе данных и машинного обучения. 

{numref}`Скриншот %s <jp_demo>` демонстрирует выполнение кода (подсмотренного 
[здесь](http://matplotlib.org/examples/pylab_examples/hexbin_demo.html))
в Jupyter notebook.

```{figure} /_static/lecture_specific/jupyter_notebooks/jp_demo.png
:scale: 50%
:name: jp_demo

Jupyter notebook запущенный в браузере
```

## Запуск Jupyter Notebook

Установив `Anaconda`, запустить jupyter notebook можно двумя способами:

1.  вбив Jupyter в поиск по приложениям;
2.  открыв `Anaconda prompt` и набрав команду `jupyter notebook`;
    

В обоих случаях должен открыться браузер, а в `Anaconda prompt` вы увидите что-то похожее на
```{figure} /_static/lecture_specific/jupyter_notebooks/starting_nb.png
:scale: 50%
```

Вывод сообщает, что jupyter notebook запущен на [http://localhost:8888/](http://localhost:8888/), т.е. ядро Jupyter принимает Python команды по 8888 локальной машины.

Открывшееся окно в браузере должно выглядеть как-то так
```{figure} /_static/lecture_specific/jupyter_notebooks/nb.png
:scale: 50%
```

Содержимое этого окна называется the Jupyter *dashboard*. Здесь можно осуществлять навигацию по файловой системе, открывать уже написанные тетрадки или создавать новые. Чтобы создать новую, нажмите `New` в правом верхнем углу и выберите `Python 3`.


