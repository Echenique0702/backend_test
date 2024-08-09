import sys
import random
import os
from requests import post, RequestException

# Variables configurations
BASE_URL = os.getenv('BASE_URL')


def log(message: str):
    """
    Simple logging function to print messages in a consistent format.

    Params:
        message (str): The message to log.
    """
    print(f"[LOG] {message}")


def generate_profile(profiles_amount: int):
    '''
    Generate automatic profiles based on the number of profiles specified.

    Params:
        profiles_amount (int): The number of profiles to create.

    Return:
        bool: Indicates whether the operation was successful.
    '''
    log(f"Starting profile generation for {profiles_amount} profiles.")
    
    profiles = []
    
    for i in range(profiles_amount):
        profile_data = {
            "img": "https://example.com/image.jpg",
            "first_name": f"First{random.randint(1, 10000)}",
            "last_name": f"Last{random.randint(1, 10000)}",
            "phone": f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "address": f"{random.randint(100, 9999)} Example St.",
            "city": "ExampleCity",
            "state": "TX",
            "zipcode": random.randint(10000, 99999),
            "available": True
        }

        log(f"Creating profile {i+1}/{profiles_amount} with data: {profile_data}")

        try:
            response = post(f"{BASE_URL}/users", json=profile_data)
            response.raise_for_status()

            profile_id = response.json().get('id')
            profiles.append(profile_id)
            log(f"Profile {i+1} created successfully with ID: {profile_id}")
        except RequestException as e:
            log(f"Error creating profile {i+1}: {e}")
            return False
        except Exception as e:
            log(f"Unexpected error: {e}")
            return False

    log(f"Successfully created {len(profiles)} profiles.")
    return True


if __name__ == "__main__":
    if BASE_URL is None:
        log("BASE_URL environment variable not set.")
        sys.exit(1)

    try:
        profiles_amount = int(sys.argv[1])
        log(f"Received input for profiles_amount: {profiles_amount}")
        
        if profiles_amount <= 0:
            raise ValueError("The number of profiles must be a positive integer.")

        success = generate_profile(profiles_amount=profiles_amount)
        
        if success:
            log("Profile generation completed successfully.")
        else:
            log("Profile generation encountered errors.")
            sys.exit(1)

    except ValueError as error:
        log(f"Invalid input: {error}")
        sys.exit(1)
    except IndexError:
        log("No input provided for the number of profiles. Please specify the number of profiles to create.")
        sys.exit(1)
    except Exception as error:
        log(f"An unexpected error occurred: {error}")
        sys.exit(1)
