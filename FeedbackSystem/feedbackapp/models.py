from django.db import models
from django.contrib.auth.models import User


def create_student_users():
    """Create the default student accounts when explicitly called."""
    users_to_create = []
    for i in range(1, 71):
        student_id = f"MP/CS/{i}"
        user = User(username=student_id)
        user.set_password(f"MP@{i}")
        users_to_create.append(user)

    User.objects.bulk_create(users_to_create, ignore_conflicts=True)
    return len(users_to_create)
