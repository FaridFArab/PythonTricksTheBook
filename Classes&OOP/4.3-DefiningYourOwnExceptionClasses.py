"""
Defining custom exception classes makes it easier for your users to adopt, and it's easier to ask for forgiveness than
permission (EAFP) coding style that’s considered more Pythonic.

"""

def validate(name):
    if len(name) < 10:
        # raise ValueError
        raise NameTooShortError(name)


class NameTooShortError(ValueError):
    pass

validate("Joe")



class BaseValidationError(ValueError):
    pass
class NameTooLongError(BaseValidationError):
    pass
class NameTooCuteError(BaseValidationError):
    pass

"""
This is generally considered an anti-pattern—it can silently swallow and hide unrelated errors and make your programs 
much harder to debug. Be careful—it’s easy to introduce unnecessary complexity by going overboard with this.
"""