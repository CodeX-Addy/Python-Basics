from functools import wraps

def user_role(func):
    @wraps(func)
    def wrapper(role):
        if role != 'admin':
            print("Access denied..")
        else:
            return func(role)
    return wrapper
    
@user_role
def access_role(role):
    print(f"Access granted to admin..")
    
role = access_role('admin')
role = access_role('user')

"""
Access granted to admin..
Access denied..
"""
