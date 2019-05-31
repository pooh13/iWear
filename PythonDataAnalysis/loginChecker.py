def loginChecker(request):
    if request.user.is_authenticated():
        account =  request.user.username
        loginType = "verified"
        return (loginType, account)
    else:
        loginType = "notVerified"
        return loginType
