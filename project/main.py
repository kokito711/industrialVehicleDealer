import datetime
import random

from project.src.entities.Bus import Bus
from project.src.entities.Maintenance import Maintenance
from project.src.entities.Truck import Truck
from project.src.entities.User import User
from project.src.entities.Van import Van
from project.src.entities.Video import Video
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
                if submenu_option == 'A':
                    _clear()
                    vehicle_type = _select_vehicle_type()
                    _insert_vehicle_values(vehicle_dealer, vehicle_type)
                    _press_enter('Vehicle successfully added')
                elif submenu_option == 'B':
                    _clear()
                    _remove_vehicle(vehicle_dealer)
                elif submenu_option == 'M':
                    _clear()
                    # TODO
                elif submenu_option == 'L':
                    _clear()
                    vehicle_dealer.get_vehicle_list()
                elif submenu_option == 'V':
                    _clear()
                    _show_vehicle_info(vehicle_dealer)
                else:
                    pass
        elif chosen_option == 'V':
            submenu_option = None
            while submenu_option is None or submenu_option != 'S':
                submenu_option = _get_menu_sales()
                if submenu_option == 'V':
                    _clear()
                    # TODO
                elif submenu_option == 'L':
                    _clear()
                    vehicle_dealer.show_sale_list()
                elif submenu_option == 'M':
                    _clear()
                    license_plate = input('Please, introduce the vehicle\'s license plate')
                    if _is_valid_license_plate(license_plate) and vehicle_dealer.exist_sale(license_plate):
                        vehicle_dealer.show_sale_info(license_plate)
                    else:
                        _press_enter('Sale does not exist')
                else:
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


def _show_vehicle_info(vehicle_dealer):
    register_number = _read_value_from_prompt('vehicle\'s register number')
    if register_number is None or len(register_number) == 0:
        _press_enter('Register number not valid')
    elif vehicle_dealer.exist_vehicle_by_register_number(register_number):
        vehicle_dealer.show_showroom_vehicle_info(register_number)
    else:
        _press_enter('Vehicle does not exist')


def _remove_vehicle(vehicle_dealer):
    register_number = _read_value_from_prompt('vehicle\'s register number')
    if register_number is None or len(register_number) == 0:
        _press_enter('Register number not valid')
    elif vehicle_dealer.exist_vehicle_by_register_number(register_number):
        vehicle_dealer.remove_vehicle(register_number)
        _press_enter('Vehicle successfully removed')
    else:
        _press_enter('Vehicle does not exist')


def _insert_vehicle_values(vehicle_dealer, vehicle_type):
    if vehicle_type == 1:
        _set_truck_values_and_save(vehicle_dealer)
    elif vehicle_type == 2:
        _set_bus_values_and_save(vehicle_dealer)
    else:
        _set_van_values_and_save(vehicle_dealer)


def _set_van_values_and_save(vehicle_dealer):
    brand = _insert_vehicle_brand()
    model = _insert_vehicle_model()
    color = _insert_vehicle_color()
    build_date = _insert_vehicle_build_date()
    passengers = _insert_passengers_number()
    max_volume_load = _insert_max_volume_load()
    max_load_length = _insert_max_load_length()
    kilometers = _insert_vehicle_kilometers()
    observations = _insert_observations()
    vehicle_dealer.add_vehicle(
        Van(brand, model, color, build_date, passengers, max_volume_load, max_load_length,
            kilometers, observations))


def _set_bus_values_and_save(vehicle_dealer):
    brand = _insert_vehicle_brand()
    model = _insert_vehicle_model()
    color = _insert_vehicle_color()
    build_date = _insert_vehicle_build_date()
    passengers = _insert_passengers_number()
    video = _insert_video()
    wheel_number = _insert_wheel_number()
    kilometers = _insert_vehicle_kilometers()
    observations = _insert_observations()
    vehicle_dealer.add_vehicle(
        Bus(brand, model, color, build_date, passengers, video, wheel_number, kilometers,
            observations))


def _set_truck_values_and_save(vehicle_dealer):
    brand = _insert_vehicle_brand()
    model = _insert_vehicle_model()
    color = _insert_vehicle_color()
    build_date = _insert_vehicle_build_date()
    tara = _insert_tara()
    max_auth_load = _insert_max_auth_load()
    wheel_number = _insert_wheel_number()
    kilometers = _insert_vehicle_kilometers()
    observations = _insert_observations()
    vehicle_dealer.add_vehicle(
        Truck(brand, model, color, build_date, tara, max_auth_load, wheel_number, kilometers,
              observations))


def _insert_vehicle_brand(brand=None):
    while brand is None:
        input_value = _read_value_from_prompt('vehicle\'s brand')
        if input_value is not None and len(input_value) > 0:
            brand = input_value
        else:
            print("Brand cannot be empty")
    return brand


def _insert_vehicle_model(model=None):
    while model is None:
        input_value = _read_value_from_prompt('vehicle\'s model')
        if input_value is not None and len(input_value) > 0:
            model = input_value
        else:
            print("Model cannot be empty")
    return model


def _insert_vehicle_color(color=None):
    while color is None:
        input_value = _read_value_from_prompt('vehicle\'s color')
        if input_value is not None and len(input_value) > 0:
            color = input_value
        else:
            print("Color cannot be empty")
    return color


def _insert_vehicle_build_date(build_date=None):
    while build_date is None:
        input_value = _read_value_from_prompt('vehicle\'s build date (dd/MM/yyyy')
        try:
            datetime.datetime.strptime(input_value, '%02d/-%02d/%04d')
            build_date = input_value
        except (TypeError, ValueError):
            print("Build date cannot be empty or format is not valid")
    return build_date


def _insert_tara(tara=None):
    while tara is None:
        input_value = int(_read_value_from_prompt('vehicle\'s TARA'))
        if input_value is not None and input_value > 0:
            tara = input_value
        else:
            print("TARA cannot be empty")
    return tara


def _insert_max_auth_load(max_auth_load=None):
    while max_auth_load is None:
        input_value = int(_read_value_from_prompt('vehicle\'s maximum authorized load'))
        if input_value is not None and input_value > 0:
            max_auth_load = input_value
        else:
            print("Maximum authorized load cannot be empty")
    return max_auth_load


def _insert_wheel_number(wheel_number=None):
    while wheel_number is None:
        input_value = int(_read_value_from_prompt('vehicle\'s number of wheels'))
        if input_value is not None and input_value > 0:
            wheel_number = input_value
        else:
            print("Number of wheels cannot be empty")
    return wheel_number


def _insert_passengers_number(passengers_number=None):
    while passengers_number is None:
        input_value = int(_read_value_from_prompt('vehicle\'s number of passengers'))
        if input_value is not None and input_value > 0:
            passengers_number = input_value
        else:
            print("Number of passengers cannot be empty")
    return passengers_number


def _insert_max_load_length(max_load_length=None):
    while max_load_length is None:
        input_value = int(_read_value_from_prompt('vehicle\'s maximum load length'))
        if input_value is not None and input_value > 0:
            max_load_length = input_value
        else:
            print("Maximum load length cannot be empty")
    return max_load_length


def _insert_max_volume_load(max_volume_load=None):
    while max_volume_load is None:
        input_value = int(_read_value_from_prompt('vehicle\'s maximum load volume'))
        if input_value is not None and input_value > 0:
            max_volume_load = input_value
        else:
            print("Maximum load volume cannot be empty")
    return max_volume_load


def _insert_video(video=None):
    while video is None:
        input_value = _read_value_from_prompt('vehicle\'s contains video (YES/NO)')
        if input_value is not None:
            if input_value == 'YES':
                video = Video.YES
            elif input_value == 'NO':
                video = Video.NO
            else:
                print("Vehicle's video not valid")
        else:
            print("Vehicle's video cannot be empty")
    return video


def _insert_vehicle_kilometers(vehicle_kilometers=None):
    while vehicle_kilometers is None:
        input_value = int(_read_value_from_prompt('vehicle\'s kilometers'))
        if input_value is not None and input_value > 0:
            vehicle_kilometers = input_value
        else:
            print("Kilometers cannot be empty")
    return vehicle_kilometers


def _insert_observations():
    has_observations = input("Would you like to include any additional info? (s/n)")
    input_value = None
    if len(has_observations) == 1 and str(has_observations).upper() == 's':
        input_value = _read_value_from_prompt('additional information')
    if input_value is not None and len(input_value) > 0:
        return input_value
    else:
        print("No additional info added")
        return None


def _select_vehicle_type(vehicle_type=None):
    while vehicle_type is None:
        print('1 Truck')
        print('2 Bus')
        print('3 Van')
        input_val = input('Please select one type: ')
        if input_val is not None and input_val in [1, 2, 3]:
            vehicle_type = input_val
    return vehicle_type


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
        _press_enter('Vehicle with the given license plate does not exist or license plate not correct')


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
        _press_enter('Maintenance successfully added.')
    else:
        _press_enter('Vehicle with the given license plate does not exist or license plate not correct')


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
        _press_enter('User Id does not exist.')


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
    _press_enter('User successfully added.')


def _show_user_info(vehicle_dealer):
    user_id = input('Please, enter an user id: ')
    if vehicle_dealer.exist_user(user_id):
        vehicle_dealer.get_user_info(user_id)
    else:
        _press_enter('User with ID ' + user_id + ' not found')


def _login_user(vehicle_dealer):
    logged = False
    while not logged:
        user_id = _read_value_from_prompt('user ID')
        pwd = _read_value_from_prompt('password')
        _clear()
        user = vehicle_dealer.get_user(user_id)
        if user is not None and user.get_pwd() == pwd:
            logged = True
            _press_enter('Welcome to Vehicle dealer application ' + user.get_name() + ' ' + user.get_surnames() + '!')
        else:
            print('User or password not valid, please try it again')


def _create_user_first_time_user(vehicle_dealer):
    print('No users right now. Proceeding to create a new one...')
    user_id = random.Random
    username = _read_value_from_prompt('name')
    surnames = _read_value_from_prompt('surnames')
    password = _read_value_from_prompt('password')
    vehicle_dealer.add_user(User(user_id, username, surnames, password))
    print('Your user id is:' + str(user_id))


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


def _press_enter(previous_msg=None):
    if previous_msg is not None:
        print(previous_msg)
    input('Press <Enter> to continue')


if __name__ == '__main__':
    initialize_vehicle_dealer()
