# redis_utils.py
import redis
import streamlit_authenticator as stauth

hostname = 'redis-14937.c263.us-east-1-2.ec2.cloud.redislabs.com'
portnumber = 14937
password = 'ZM69jXWDAAKmc1fjxmrQIvJgg7ALdlSS'

r = redis.StrictRedis(host=hostname, port=portnumber, password=password)
hashed_password = stauth.Hasher([password]).generate()[0]

def insert_user(email, username, password, role="Student"):
    user_key = f"student:{email}"
    r.hset(user_key, "email", email)
    r.hset(user_key, "username", username)
    r.hset(user_key, "password", password)
    r.hset(user_key, "role", role)
    return user_key

def validate_credentials(email, password):
    user_key = f"student:{email}"
    stored_password_bytes = r.hget(user_key, "password")

    if stored_password_bytes:
        stored_password = stored_password_bytes.decode('utf-8')  # Convert bytes to string
        hashed_password = stauth.Hasher([password]).generate()[0]

        if stored_password == hashed_password:
            return user_key

    return None, None
