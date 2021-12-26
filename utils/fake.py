from faker import Faker


class Users(object):

    def generate_users(self, locale='zh_CN'):
        fake = Faker(locale)

        users = {}
        users['name'] = fake.name()
        users['ssn'] = fake.ssn()
        users['phone_number'] = fake.phone_number()
        print(users)

        return users

        # name = fake.name()
        # ssn = fake.ssn()
        # telephone = fake.phone_number()
        # print(name + ' ' + telephone + ' ' + ssn + '\n')
        # return name + ' ' + telephone + ' ' + ssn + '\n'

    # def write_user(self):
    #     with open(file=r'files/users.txt', mode='a') as f:
    #         f.writelines(self.generate_users())


# if __name__ == '__main__':
#     users = Users().generate_users()
#     users.write_user()
