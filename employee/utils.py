def is_admin(user):

    return user.groups.filter(
        name='Admin'
    ).exists()


def is_employee(user):

    return user.groups.filter(
        name='Employee'
    ).exists()