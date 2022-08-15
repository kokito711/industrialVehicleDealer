import random

from project.src.entities.Maintenance import Maintenance
from project.src.entities.User import User
from project.src.service.VehicleDealer import VehicleDealer


def initialize_vehicle_dealer():
    vehicle_dealer: VehicleDealer = VehicleDealer()
    vehicle_dealer.add_user(User('1234', 'Sergio', 'Lopez Jimenez', '1234'))
    if len(vehicle_dealer.user_list) == 0:
        _create_user_first_time_user(vehicle_dealer)
    else:
        _login_user(vehicle_dealer)

    chosen_option = None
    while chosen_option != 'S':
        chosen_option = _get_main_menu_option()
        if chosen_option == 'E':
            submenu_option = None
            while submenu_option is None or submenu_option != 'S':
                submenu_option = _get_menu_showroom()
                # TODO
        elif chosen_option == 'V':
            submenu_option = None
            while submenu_option is None or submenu_option != 'S':
                submenu_option = _get_menu_sales()
                # TODO
                pass
        elif chosen_option == 'M':
            _manage_maintenance(vehicle_dealer)
        elif chosen_option == 'U':
            _manage_user_data(vehicle_dealer)
        else:
            print('Not implemented')

    print('Number of Vehicles: ' + str(len(vehicle_dealer.vehicle_list)))
    print('Number of Sales: ' + str(len(vehicle_dealer.sales_list)))
    print('Number of Users: ' + str(len(vehicle_dealer.user_list)))

    print('Application will be closed...\nSee you soon!')


def _manage_maintenance(vehicle_dealer):
    submenu_option = None
    while submenu_option is None or submenu_option != 'S':
        submenu_option = _get_menu_maintenance()
        if submenu_option == 'A':
            _clear()
            _add_maintenance(vehicle_dealer)
        elif submenu_option == 'L':
            _clear()
            _show_maintenances(vehicle_dealer)
        else:
            pass


def _show_maintenances(vehicle_dealer):
    license_plate = input('Please, introduce the vehicle\'s license plate')
    if _is_valid_license_plate(license_plate) and vehicle_dealer.exist_vehicle(license_plate):
        vehicle_dealer.show_sale_info(license_plate)
        _clear()
        print('========================================')
        print('       Vehicle\'s maintenance list      ')
        print('========================================')
        vehicle_dealer.get_sale_vehicle(license_plate).print_maintenance_list()
    else:
        print('Vehicle with the given license plate does not exist or license plate not correct')
        _press_enter()


def _add_maintenance(vehicle_dealer):
    license_plate = input('Please, introduce the vehicle\'s license plate')
    if _is_valid_license_plate(license_plate) and vehicle_dealer.exist_vehicle(license_plate):
        kilometers = None
        while kilometers is None:
            read_value = input('Please, introduce the vehicle\'s number of kilometers')
            if read_value.isnumeric():
                kilometers = read_value
            else:
                print('Kilometers are not right')
        operations = None
        while operations is None:
            read_value = input('Please, introduce the made operations')
            if read_value != '':
                operations = read_value
            else:
                print('Operations cannot be empty')
        price = None
        while price is None:
            read_value = input('Please, introduce the price')
            if read_value.isnumeric():
                price = read_value
            else:
                print('Price cannot be empty or is a valid value')
        vehicle_dealer.get_sale_vehicle(license_plate) \
            .add_maintenance(Maintenance(kilometers, operations, price))
        print('Maintenance successfully added.')
        _press_enter()
    else:
        print('Vehicle with the given license plate does not exist or license plate not correct')
        _press_enter()


def _is_valid_license_plate(license_plate):
    if len(license_plate) != 7:
        return False
    for index, char in enumerate(license_plate):
        if index < 4 and not char.isDigit():
            return False
        elif char.isDigit():
            return False
    return True


def _manage_user_data(vehicle_dealer):
    submenu_option = None
    while submenu_option is None or submenu_option != 'S':
        submenu_option = _get_menu_users()
        if submenu_option == 'A':
            _clear()
            _add_new_user(vehicle_dealer)
        elif submenu_option == 'B':
            _clear()
            _delete_user(vehicle_dealer)
        elif submenu_option == 'M':
            _clear()
            print('not implemented')
        elif submenu_option == 'L':
            _clear()
            vehicle_dealer.get_users_list()
        elif submenu_option == 'U':
            _clear()
            _show_user_info(vehicle_dealer)
        else:
            pass


def _delete_user(vehicle_dealer):
    _clear()
    user_id = input('Please, enter an user id: ')
    if user_id is not None and (user_id != '' and not vehicle_dealer.exist_user(user_id)):
        confirm = None
        while confirm is None:
            answer = input('Are you sure to remove the user? (s/n)')
            if len(answer) == 1 and str(answer).upper() == 's':
                vehicle_dealer.delete_user(user_id)
                print('User successfully removed.')
            else:
                print('User won\'t be removed')
        _press_enter()
    else:
        print('User Id does not exist.')
        _press_enter()


def _add_new_user(vehicle_dealer):
    user, username, surnames, pwd = None, None, None, None
    _clear()
    while user is None:
        value = input('Please, enter an user id: ')
        if value is not None and (value != '' and not vehicle_dealer.exist_user(value)):
            user = value
        else:
            print('User Id not valid.')
    while pwd is None:
        value = input('Please, enter a password: ')
        if value is not None and value != '':
            pwd = value
        else:
            print('Password not valid.')
    username = input('Please enter a name: ')
    surnames = input('Please enter surnames: ')
    vehicle_dealer.add_user(User(user, username, surnames, pwd))
    print('User successfully added.')
    _press_enter()


def _show_user_info(vehicle_dealer):
    user_id = input('Please, enter an user id: ')
    if vehicle_dealer.exist_user(user_id):
        vehicle_dealer.get_user_info(user_id)
    else:
        print('User with ID ' + user_id + ' not found')
        _press_enter()


def _login_user(vehicle_dealer):
    logged = False
    while not logged:
        user_id = _read_value_from_prompt('user ID')
        pwd = _read_value_from_prompt('password')
        _clear()
        user = vehicle_dealer.get_user(user_id)
        if user is not None and user.get_pwd() == pwd:
            logged = True
            print('Welcome to Vehicle dealer application ' + user.get_name() + ' ' + user.get_surnames() + '!')
            _press_enter()
        else:
            print('User or password not valid, please try it again')


def _create_user_first_time_user(vehicle_dealer):
    print('No users right now. Proceeding to create a new one...')
    user_id = random.Random
    username = _read_value_from_prompt('name')
    surnames = _read_value_from_prompt('surnames')
    password = _read_value_from_prompt('password')
    vehicle_dealer.add_user(User(user_id, username, surnames, password))
    print('Your user id is:' + user_id)


def _read_value_from_prompt(required_value):
    value = None
    while value is None or len(value) == 0:
        value = input('Please, write your ' + required_value + ': ')
    return value


def _get_main_menu_option():
    _clear()
    values = ['E', 'V', 'M', 'U', 'G', 'S']
    print('========================================')
    print('                 MAIN MENU              ')
    print('========================================\n')
    print(' E  Showroom')
    print(' V  Sale')
    print(' M  Maintenance')
    print(' U  Users\n')
    print(' G  Save data')
    print(' S  Exit\n')
    return _ask_for_option(values)


def _get_menu_users():
    _clear()
    values = ['A', 'B', 'M', 'L', 'U', 'S']
    print('========================================')
    print('                   USERS                ')
    print('========================================\n')
    print(' A  Create user')
    print(' B  Delete user\n')
    print(' M  Modify user\n')
    print(' L  Show existing users\n')
    print(' U  Show user data')
    print(' S  Exit\n')
    return _ask_for_option(values)


def _get_menu_maintenance():
    _clear()
    values = ['A', 'L', 'S']
    print('========================================')
    print('               MAINTENANCE              ')
    print('========================================\n')
    print(' A  Add maintenance\n')
    print(' L  Show maintenance for a vehicle\n')
    print(' S  Exit\n')
    return _ask_for_option(values)


def _get_menu_showroom():
    _clear()
    values = ['A', 'B', 'L', 'M', 'S', 'V']
    print('========================================')
    print('                 SHOWROOM               ')
    print('========================================\n')
    print(' A  Add vehicle')
    print(' B  Remove showroom vehicle\n')
    print(' M  Modify showroom vehicle\n')
    print(' L  List showroom vehicles')
    print(' V  Show information about a vehicle in showroom\n')
    print(' S  Exit\n')
    return _ask_for_option(values)


def _get_menu_sales():
    _clear()
    values = ['L', 'M', 'S', 'V']
    print('========================================')
    print('                  SALES                 ')
    print('========================================\n')
    print(' V  Sell vehicle\n')
    print(' L  Show sales list')
    print(' M  Show sale info\n')
    print(' S  Exit\n')
    return _ask_for_option(values)


def _ask_for_option(values):
    option = None
    while option is None:
        input_value = input('Please, choose an option: ')
        if len(input_value) == 1 and str(input_value).upper() in values:
            option = str(input_value).upper()
            return option
        else:
            print('Selected option is not valid.')


def _clear():
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
    """
    print('\n' * 100)


def _press_enter():
    input('Press <Enter> to continue')


if __name__ == '__main__':
    initialize_vehicle_dealer()
