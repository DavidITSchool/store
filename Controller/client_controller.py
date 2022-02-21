from datetime import datetime
from Model.client_repository import DBClientRepository #ClientRepository
from View.client_ui import ClientUI


class ClientController:
    def __init__(self, client_ui, client_repo):
        self.client_ui = client_ui
        self.client_repo = client_repo

    def start(self):
        while True:
            self.client_ui.display_menu()
            opt = self.client_ui.get_user_option()

            if opt == '1':  # '1' == 'Add client'
                self.add_client()
            elif opt == '2':  # '2' == 'Remove client'
                self.remove_client()
            elif opt == '3':  # '3' == 'Update client'
                self.update_client()
            elif opt == '4':  # '4' == 'Display one clients'
                self.display_one_client()
            elif opt == '5':  # '5' == 'Display all clients'
                self.display_all_clients()
            elif opt == 'x':
                exit()
            else:
                print('No such option!')

    def add_client(self):
        client_id = self.client_ui.get_client_id()
        last_name = self.client_ui.get_client_last_name()
        first_name = self.client_ui.get_client_first_name()
        age = self.client_ui.get_client_age()
        email = self.client_ui.get_client_email()

        self.client_repo.add_client(client_id, last_name, first_name, age, email)

        self.client_ui.confirm_operation_successful()

    def remove_client(self):
        client_id = self.client_ui.get_client_id()

        self.client_repo.delete_client(client_id)

        self.client_ui.confirm_operation_successful()

    def update_client(self):
        client_id = self.client_ui.get_client_id()
        last_name = self.client_ui.get_client_last_name()
        first_name = self.client_ui.get_client_first_name()
        email = self.client_ui.get_client_email()

        self.client_repo.update_client(client_id, last_name, first_name, email)

        self.client_ui.confirm_operation_successful()

    def display_one_client(self):
        client_id = self.client_ui.get_client_id()

        client = self.client_repo.get_client(client_id)

        self.client_ui.display_one_client(client)

    def display_all_clients(self):
        clients = self.client_repo.get_all_clients()
        self.client_ui.display_all_clients(clients)


class StoreController:
    def __init__(self, store_ui, store_repo, client_ctrl, product_ctrl):
        self.store_ui = store_ui
        self.store_repo = store_repo
        self.client_ctrl = client_ctrl
        self.product_ctrl = product_ctrl

    def start(self):
        while True:
            self.store_ui.display_menu()
            opt = self.store_ui.get_user_option()

            if opt == '1':  # '1' == 'Client'
                self.client_ctrl.start()
            elif opt == '2':  # '2' == 'Product'
                self.product_ctrl.start()
            elif opt == '3':  # '3' == 'Buy Product'
                user_id = self.store_ui.get_user_id()
                if self.client_ctrl.verify_user_id(user_id):
                    product_id = self.store_ui.get_product_id()
                    if self.product_ctrl.verify_product_id(product_id) and self.product_ctrl.verify_product_stock(product_id):
                        self.store_repo.add_transaction(user_id, product_id, datetime.now())



if __name__ == '__main__':
    # client_repo = ClientRepository()
    client_repo = DBClientRepository()
    client_ui = ClientUI()
    client_ctrl = ClientController(client_ui, client_repo)
    client_ctrl.start()

