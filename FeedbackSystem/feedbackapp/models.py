from django.db import models
from django.contrib.auth.models import User


def create_student_users():
    """Create the default student accounts when explicitly called."""
    users = []
    for i in range(1, 71):
        student_id = f"MP_CS_{i}"
        user = User(student_id=student_id)
        user.set_password(f"MP@{i}")
        users.append(user)

    User.objects.bulk_create(users, ignore_conflicts=True)
    return len(users)
