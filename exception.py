class BaseError(Exception):
    t = "Неизвестная ошибка"


class NoSpaceError(BaseError):
    t = "Нет места"


class UnknownProductError(BaseError):
    t = "Неизвестный товар"


class NoProductError(BaseError):
    t = "Нет товара"


class InvalidRequestError(BaseError):
    t = "Неверный запрос"


class UnknownStorageError(BaseError):
    t = "Неизвестный склад"


class HugeAmountProduct(BaseError):
    t = "Много товаров"
