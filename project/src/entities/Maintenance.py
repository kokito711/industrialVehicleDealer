from datetime import datetime


class Maintenance:
    """
    Contiene un constructor que inicializa todos los atributos de la clase menos maintenance_date
    """

    def __init__(self, kilometers, done_work, price):
        self.maintenance_date = datetime.now().strftime('dd/MM/yyyy')
        self.kilometers = kilometers
        self.done_work = done_work
        self.price = price
