from pprint import pprint


class ClientUI:
    @staticmethod
    def display_menu():
        print('1. Add Client')
        print('2. Remove client')
        print('3. Update client')
        print('4. Display one clients')
        print('5. Display all clients')
        print('x. Exit')

    @staticmethod
    def get_user_option():
        return input('Please select an option: ')

    @staticmethod
    def display_one_client(client):
        print(client)

    @staticmethod
    def display_all_clients(clients):
        pprint(clients)

    @staticmethod
    def get_client_id():
        return int(input('Please provide the client_id: '))

    @staticmethod
    def get_client_last_name():
        return input('Please provide the last_name: ')

    @staticmethod
    def get_client_first_name():
        return input('Please provide the first_name: ')

    @staticmethod
    def get_client_age():
        return int(input('Please provide the age: '))

    @staticmethod
    def get_client_email():
        return input('Please provide the email: ')

    @staticmethod
    def confirm_operation_successful():
        print('Operation finished successfully')

