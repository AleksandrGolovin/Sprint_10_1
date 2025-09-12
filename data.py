class URL:
    # Базовый адрес сервиса
    BASE_URL = 'https://ez-route.stand.praktikum-services.ru/'
    # Конечные точки
    MAIN_PAGE = f'{BASE_URL}'

ADDRESS_FROM = 'Хамовнический вал, 34'
ADDRESS_TO = 'Зубовский бульвар, 37'

SAME_FROM_TO_RESULTS_TEXT = 'Авто Бесплатно'
SAME_FROM_TO_RESULTS_DURATION = 'В пути 0 мин.'

TARIFFS = {
    "Рабочий": "Для деловых особ, которых отвлекают",
    "Сонный": "Для тех, кто не выспался",
    "Отпускной": "Если пришла пора отдохнуть",
    "Разговорчивый": "Если мысли не выходят из головы",
    "Утешительный": "Если хочется свернуться калачиком",
    "Глянцевый": "Если нужно блистать"
}

AWAITING_BLOCK_TITLE = 'Поиск машины'
DETAILS_BLOCK_INFORMATION_COST = 'Стоимость'