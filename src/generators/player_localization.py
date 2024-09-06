from faker import Faker


fake = Faker()
class PlayerLocalization:
    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {
            "nikname": self.fake.first_name()
        }

    def build(self):
        return self.result