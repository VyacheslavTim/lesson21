from Courier import Courier
from app.request import Request
from app.shop import Shop
from app.store import Store
from exception import BaseError

shop = Shop(
    items={
        'печенька': 3,
        'чипсы': 5,
        'сок': 3,
    },
)

store = Store(
    items={
        'печенька': 10,
        'чипсы': 7,
        'сок': 8,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input('Введите строку в формате "Доставить 3 печенька из склад в магазин"\n'
                           'Введите "stop" или "стоп", чтобы продолжить'
                           )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
            courier = Courier(request=request, storages=storages)
            # destination = storages[request.destination]
            # departure = storages[request.departure]
            courier.move()
        except BaseError as error:
            print(error.t)


if __name__ == "__main__":
    main()
