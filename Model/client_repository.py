from Model.client_domain import Client


class ClientRepo:
    def __init__(self):
        self.client_list = []

    # CREATE
    def add_client(self, client_id, last_name, first_name, age, email):

        new_client = Client(
            my_client_id=client_id,
            my_last_name=last_name,
            my_first_name=first_name,
            my_age=age,
            my_email=email,
        )

        self.client_list.append(new_client)

    # READ
    def get_client(self, client_id):
        for client in self.client_list:
            if client.client_id == client_id:
                return client

    # UPDATE
    def update_client(self, client_id, last_name, first_name, email):
        for index, client in enumerate(self.client_list):
            if client.client_id == client_id:
                if last_name:
                    self.client_list[index].last_name = last_name
                if first_name:
                    self.client_list[index].first_name = first_name
                if email:
                    self.client_list[index].email = email
                return

    # DELETE
    def delete_client(self, client_id):
        for index, client in enumerate(self.client_list):
            if client.client_id == client_id:
                del self.client_list[index]
                return

    def get_all_clients(self):
        return self.client_list


if __name__ == '__main__':
    client_repo = ClientRepository()

    client_repo.add_client(1, 'Dan', 'David', 24, 'test@gmail.com')
    client_repo.add_client(2, 'Pop', 'Andrei', 44, 'pop.andrei@gmail.com')
    print(client_repo.get_all_clients())
    print(client_repo.get_client(1))
    client_repo.update_client(1, '', '', 'david@gmail.com')
    print(client_repo.client_list)
    client_repo.delete_client(1)
    print(client_repo.client_list)
