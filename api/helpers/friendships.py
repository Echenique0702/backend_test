def basic_friendship_helper(friendship: dict) -> dict:
    '''
    Helper to return basic frienship information
    '''
    return {
        'id': str(friendship['_id']),
        'first_user_id': friendship['first_user_id'],
        'second_user_id': friendship['second_user_id']
    }