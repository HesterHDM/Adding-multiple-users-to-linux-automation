from faker import Faker

fake = Faker()

with open('random_names.txt', 'w') as file:
    for _ in range(1000000):
        name = fake.name()
        file.write(name + '\n')

print("Random names generated and saved to 'random_names.txt'.")
