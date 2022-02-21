class Client:

    def __init__(self, my_client_id, my_last_name, my_first_name, my_age, my_email):
        self.client_id = my_client_id
        self.last_name = my_last_name
        self.first_name = my_first_name
        self.age = my_age
        self.email = my_email

    def __repr__(self):
        return f'{self.client_id} {self.last_name} {self.first_name} {self.age} {self.email}'

    def send_email(self):
        print(f'Sending email to {self.last_name} {self.first_name}')