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

# Сторонние библиотеки и пакетные менеджеры

## Сторонние библиотеки 

Пришло время познакомимся с первой сторонней библиотекой для python, т.е. библиотекой, которая по умолчанию не включена в дистрибутив python и должна быть установлена самостоятельно. Существует огромное количество сторонних библиотек для python, а для удобства их установки были разработаны **пакетные менеджеры**. 

В качестве примеров сторонних библиотек можно привести [numpy](https://numpy.org/), [matplotlib](https://matplotlib.org/), [scipy](https://scipy.org/), [pandas](https://pandas.pydata.org/), [scikit-learn](https://scikit-learn.org/stable/), [tensorflow](https://www.tensorflow.org/), [torch](https://pytorch.org/docs/stable/torch.html), [openCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) и многие другие. Подавляющее большинство этих библиотек представляет из себя проекты с открытым исходным (`open source`), которые можно использовать в своих научных исследованиях абсолютно бесплатно. 

Самые популярные пакетные менеджеры --- `conda` и `PyPI`.

## Conda

При установке anaconda, [conda](https://docs.conda.io/en/latest/) ставится по умолчанию. Более того, anaconda, кроме самого python, пакетного менеджера `conda`, устанавливает сразу и ряд часто используемых библиотек. Например, `numpy`,  `matplotlib`, `pandas`, `scipy`, `scikit-image` и `scikit-learn` устанавливаются по умолчанию. Библиотека `tensorflow` устанавливается по умолчанию только на машины с OS Linux, а библиотеки `torch` и `openCV` не входят в стандартный набор anaconda и требуют дополнительной установки.

Самый простой способ установить библиотеку --- установить её глобально.
```console
  conda install seaborn
```

## PyPI

При установке "голого" python с [официального сайта](https://www.python.org/) устанавливаются только интерпретатор `CPython`. Никакие сторонние библиотеки и пакетные менеджеры не устанавливаются (хотя в установщике `windows` есть возможность установить `PyPI` одновременно с `CPython`).  

[PyPI](https://pypi.org/) (Python Package Index) --- пакетный менеджер, в целом аналогичный `conda`. Установка библиотек глобально осуществляется схожей командой.

```console
  pip install seaborn
```

Или чуть более сложной, но позволяющей явно указать интерпретатор python, для которого устанавливается библиотека (полезно, когда стоит несколько версий python).

```console
  python -m pip install seaborn
```


## Виртуальные окружения

Установка библиотеки глобально означает, что библиотека будет доступна для импортирования в любом коде. Такой подход имеет ряд недостатков. Например, если библиотек становиться слишком много, то могут возникнуть проблемы с совместимостью каких-то из них между собой. Такое может возникнуть, если в разных проектах используются разные библиотеки, но библиотеки из одного проекта требуют какой-то пакет одной версии, а библиотеки другой версии требуют тот же пакет, но другой версии (например, какие-то из них давно не обновлялись).

Чтобы избежать таких проблем, рекомендуется использовать виртуальные окружения (`virtual environments`), которые позволяют создавать отдельные окружения, каждое из которых может иметь свой набор библиотек своих версий. Подробнее о виртуальных окружения в anaconda можно почитать [здесь](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), а в "голом" `CPython` предусмотрен модуль [`venv`](https://docs.python.org/3/library/venv.html).


## Импортирование сторонних библиотек

После установки библиотеки её можно импортировать так же, как и модули стандартной библиотеки.
Самый стандартный импорт
```python
import scipy
```
или импорт с созданием псевдонима
```python
import numpy as np
```
или импорт определенных имен из модулей
```python
from matplotlib import pyplot
```
или комбинированный подход
```python
from matplotlib import pyplot as plt
```
или даже так
```python
import matplotlib.pyplot as plt
```