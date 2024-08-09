import random
import os
import sys
from requests import get, post

# Variables configurations
BASE_URL = os.getenv('BASE_URL')

def log(message: str):
    """
    Simple logging function to print messages in a consistent format.

    Params:
        message (str): The message to log.
    """
    print(f"[LOG] {message}")

def generate_two_different_indexs(b):
    """
    Generate two different indices within the range from 0 to b-1.

    Params:
        b (int): The upper bound (exclusive) for generating indices.

    Returns:
        list: A list containing two different indices.

    Raises:
        ValueError: If b is less than or equal to 1.
    """
    if b <= 1:
        raise ValueError("There are None or just one user in the DB")
    
    return random.sample(range(0, b), 2)

def create_friendships(amount: int):
    """
    Generate automatic friendships based on the amount specified.

    Params:
        amount (int): The number of friendships to create.

    Returns:
        bool: Indicates whether the operation was successful.
    """
    log(f"Starting {amount} friendships automatic generation")

    try:
        response = get(f"{BASE_URL}/users")
        response.raise_for_status()

        users = response.json()
        users_id = [user['id'] for user in users]

        log(f"Retrieved {len(users_id)} users from the database.")

        for _ in range(amount):
            index = generate_two_different_indexs(len(users_id))

            friendship_response = post(
                f"{BASE_URL}/friendships/first-user/{users_id[index[0]]}/second-user/{users_id[index[1]]}"
            )
            friendship_response.raise_for_status()

            log(f"Created friendship between users {users_id[index[0]]} and {users_id[index[1]]}: {friendship_response.json()}")

        log("All friendships created successfully.")
        return True

    except Exception as e:
        log(f"An error occurred during friendship generation: {e}")
        return False

if __name__ == "__main__":
    if BASE_URL is None:
        log("BASE_URL environment variable not set.")
        sys.exit(1)

    try:
        amount = int(sys.argv[1])
        log(f"Received input for amount: {amount}")
        
        if amount <= 0:
            raise ValueError("The number of friendships must be a positive integer.")

        success = create_friendships(amount=amount)
        
        if success:
            log("Friendship generation completed successfully.")
        else:
            log("Friendship generation encountered errors.")
            sys.exit(1)

    except ValueError as error:
        log(f"Invalid input: {error}")
        sys.exit(1)
    except IndexError:
        log("No input provided for the number of friendships. Please specify the number of friendships to create.")
        sys.exit(1)
    except Exception as error:
        log(f"An unexpected error occurred: {error}")
        sys.exit(1)
