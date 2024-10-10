import random
import faker


class Generator:
    @staticmethod
    def generate_random_float():
        return random.uniform(0.0, 999.99)

    @staticmethod
    def generate_random_string_name():
        return faker.Faker().name()
