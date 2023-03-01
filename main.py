from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import RequestError, LogisticError

store = Store(
    items={
        "печенье": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1
    }
)

shop = Shop(
    items={
        "печенье": 2,
        "собачка": 2,
        "елка": 2,
        "пончик": 1,
        "зонт": 1,
    }
)

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день!\n')

    while True:
        # Выводим содержимое складов
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        # Запрашиваем ввод от пользователя
        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "stop" или "стоп" если хотите закончить\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        # Распарсить и провалидировать ввод пользователя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        # Запустить доставку
        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} из {request.departure}')

        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
        except LogisticError as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f'Курьер вернул {request.amount} {request.product} в {request.departure}')
            continue


if __name__ == '__main__':
    main()
