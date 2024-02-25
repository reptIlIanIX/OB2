# Диплом OB2

### Задача

Реализовать платформу для публикации записей пользователями. Публикация может быть бесплатной, то есть доступной любому пользователю без регистрации, либо платной, которая доступна только авторизованным пользователям, который оплатили разовую подписку. Для реализации оплаты подписки используйте Stripe. Регистрация пользователя должна быть по номеру телефона.

### Дополнительные ссылки

- [Stripe](https://stripe.com/docs/api)

### Требуемый стэк

- python
- postgresql
- django
- docker

## Описание
Две модели ```user``` и ```blog```
в папке ```static``` лежат стили ```cs``` и ```js```. В ```templates```
лежат ```html```. Для реализации фронтенд части использовались шаблоны ```Bootstrap```
В папке ```media``` сохраняются img, которые загружает пользователь на странице создания/редактиврования блога

## Installation

```bash
pip install -r requirements.txt
```

## Usage

модели ```user``` и ```blog``` описаны через CBV

в ```blog``` полностью реализован CRUD

в ```user``` частично (Create/Update)

Также в ```user``` описано взаимодействие с ```API Stripe```

# *

Столкнулся с двумя проблемами, которые, учитывая то, что сегодня последний день сдачи диплома, не успеваю (по своей
ошибке)

1. В ```user.tests.py``` не смог подробнее реализовать тесты из-за того, что не удается залогинить ```self.user```(всеми
   способами, которыми пробовал: и через```force_login``` и через ```Client()```)

2. Не понял, как реализовать подписку ```Stripe``` в рамках модели ```User```. я видел это через создание
   поля ```is_subscriped``` и смену его статуса на ```true```, если после страницы оплаты выпадает ```success.html```.
   Если ```user.is_subscriped```, то сделать новые кнопки для него доступные(как премиуму)

## DOCKER


Чтобы запустить сбор ```Docker```, ввести команду ```docker-compose build```

Для старта сервера ```docker-compose up```
В составе ```Docker```:

```db```\
```redis```\
```app```\



В ```.env``` лежат секретные переменные окружения и данные 

В ```.env.sample``` лежат переменные