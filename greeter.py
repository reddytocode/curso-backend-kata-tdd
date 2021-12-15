from datetime import datetime


class Greeter:
    def greet(self, name):
        name = name.strip().capitalize()
        now = datetime.now()
        hour = now.hour
        if 6 <= hour <= 12:
            return f"Good morning {name}"
        elif 18 <= hour < 22:
            return f"Good evening {name}"
        elif 22 <= hour <= 23 or 0 <= hour < 6:
            return f"Good night {name}"
        return f"Hello {name}"