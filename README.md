# Классификация времен года

## Датасет
Всего было собрано 307 цветных изображений пейзажей из гугл картинок. В каждом классе содержится от 73 до 83 картинок. Датасет можно скачать с [гугл диска](https://drive.google.com/drive/folders/1GfCbtbueNeqcb1d1uChy9WKrUEnpa-su?usp=sharing)

## Модель
Для решения задачи была использована предобученная resnet-18 с последующим дообучением на собранном датасете.

## Обучение
Код обучение представлен в [notebook'е](https://github.com/vizhulin/season_classification/blob/main/classification.ipynb)

## Предсказания
Протестировать предсказания модели на собственных данных можно либо в [notebook'е](https://github.com/vizhulin/season_classification/blob/main/classification.ipynb), открыв его в [colab](https://colab.research.google.com/drive/1lbFGpK5NuACl49sfhTEzlBVEbUIsM_cV#scrollTo=uBg3Q1ARHJea), либо с помощью [скрипта](https://github.com/vizhulin/season_classification/blob/main/season_classifier.py) следующим образом:

```
python3 season_classifier.py --img_path *path_to_image*
```
