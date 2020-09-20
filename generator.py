from faker import Faker
from sys import argv
import random
import json
import os


def main():
    script, size = argv

    print(os.getcwd())
    path = os.getcwd() + "/test_data"
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"created: {path}")

    for i in range(6):
        filename = f"test_data/test_data_{i}.txt"

        target = open(filename, "w")

        for j in range(int(size)):
            event = event_gen()
            target.write(event+"\n")

        target.close()
        print(f"Created {size} test events stored in {filename}")




def event_gen() -> str:
    event_types = ["track", "page", "identify"]
    random_type = event_types[random.randrange(2)]
    print(f"event: {random_type}")
    fake = Faker()
    event = {
        "type": random_type,
        "properties": {"email": fake.email()},
        "traits": {"firstname": fake.first_name()},
        "segment_id": fake.ssn()
        }
    return json.dumps(event)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
