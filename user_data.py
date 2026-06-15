from .locators.order_locators import Order

class UserData:
    RENTAL_PERIOD_DAY = Order.RENTAL_PERIOD_DAY
    RENTAL_PERIOD_TWO_DAYS = Order.RENTAL_PERIOD_TWO_DAYS
    RENTAL_PERIOD_THREE_DAYS = Order.RENTAL_PERIOD_THREE_DAYS
    RENTAL_PERIOD_FOUR_DAYS = Order.RENTAL_PERIOD_FOUR_DAYS
    RENTAL_PERIOD_FIVE_DAYS = Order.RENTAL_PERIOD_FIVE_DAYS
    RENTAL_PERIOD_SIX_DAYS = Order.RENTAL_PERIOD_SIX_DAYS
    RENTAL_PERIOD_SEVEN_DAYS = Order.RENTAL_PERIOD_SEVEN_DAYS
    COLOR_BLACK = Order.COLOR_BLACK
    COLOR_GREY = Order.COLOR_GREY

    USER1 = {
        "order1":{
        "name": "Регина" ,
        "surname": "Львицкая",
        "address": "Моховая улица, 15",
        "metro": "Охотный ряд",
        "telephon": "89276782828"
        },
        "order2": {
        "delivery": "07.08.2026",
        "period": RENTAL_PERIOD_THREE_DAYS,
        "color": COLOR_GREY,
        "comment": "Оставить у дома",}
    }

    USER2 = {
        "order1": {
        "name": "Клава" ,
        "surname": "Ловицкая",
        "address": "Композиторская, 33",
        "metro": "Черкизовская",
        "telephon": "89175755528"
        },
       "order2": {
        "delivery": "17.07.2026",
        "period": RENTAL_PERIOD_TWO_DAYS,
        "color": COLOR_BLACK,
        "comment": "Не звонить",}
    }