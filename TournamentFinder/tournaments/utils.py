def get_login_status(request):
    return True if request.user.username is not '' else False