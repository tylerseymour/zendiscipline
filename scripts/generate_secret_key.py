from django.core.management.utils import get_random_secret_key

print("")
print("Copy this value to your .env file as the SECRET_KEY")
print("")
print(get_random_secret_key())
print("")
