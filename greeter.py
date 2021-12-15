from datetime import datetime


class Greeter:
    def greet(self, name):
        name = name.strip().capitalize()
        now = datetime.now()
        hour = now.hour
        if 6 < hour < 12:
            return f"Good morning {name}"
        return f"Hello {name}"