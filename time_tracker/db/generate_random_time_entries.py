import random
import json

import sys

from datetime import datetime, timedelta

sys.path.append('..')
from time_tracker.models.serializable import DATE_FORMAT

words = """Repellendus sint ipsa facilis repudiandae asperiores modi. Aliquam 
eveniet modi odit eos eum voluptas nostrum. Molestias voluptate rerum ipsam 
suscipit maxime. Et iure aut et et sunt aliquam. Deleniti sit officiis ad 
asperiores. Repudiandae consequuntur sint ducimus ut quae magnam. Ut id et 
laudantium eos et dolor. Eveniet id fuga aspernatur at. Voluptas consequatur aut
aut atque qui fugit et. Inventore accusantium nobis ut aut accusamus. 
Aspernatur perferendis quisquam eius laboriosam distinctio labore. Mollitia quis
 veniam minima ea eaque. Sed optio nesciunt ab quia animi commodi fuga quidem.
Voluptatibus praesentium cumque est odit reiciendis praesentium. Est omnis et 
optio maxime sint. Quos ut nisi ut. Assumenda id et adipisci omnis ipsam et 
architecto. Repudiandae et aut deleniti accusamus temporibus omnis quo ducimus.
Pariatur dignissimos dolor ut occaecati maxime voluptatum ab."""

words = words.replace('.', '').lower().split()

def random_time_entry(id_: int, user_id: int):
    start_date = datetime(
        year=random.randint(2012, 2016),
        month=random.randint(1, 12),
        day=random.randint(1, 28),
        hour=random.randint(8, 13),
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    duration = timedelta(
        hours=random.randint(3, 6),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    end_date = start_date + duration
    return {
        'id': id_,
        'user_id': user_id,
        'start_time': start_date.strftime(DATE_FORMAT),
        'end_time': end_date.strftime(DATE_FORMAT),
        'what': ' '.join(random.sample(words, random.randint(10, 30)))
    }


def generate_random_time_entries(user_id, max_, start_id=1):
    entries = []

    for id_ in range(start_id, start_id+max_):
        entries.append(
            random_time_entry(id_, user_id)
        )

    return entries


def generate_random_user_data(max_):
    entries = []

    for id_ in range(1, max_):
        entries += generate_random_time_entries(id_, random.randint(5, 8),
                                                len(entries) + 1)

    return entries


def main():
    data = generate_random_user_data(20)
    print(json.dumps(data).replace('}, ', '},\n'))


if __name__ == "__main__":
    main()