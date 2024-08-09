def basic_user_helper(user: dict) -> dict:
    '''
    Helper to return basic user information
    '''
    return {
        'id': str(user['_id']),
        'first_name': user['first_name'],
        'last_name': user['last_name']
    }