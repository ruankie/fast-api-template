class Greetings():
    def __init__(self, greeting:str = "Hello World") -> None:
        self.greeting = greeting

    def do_greetings(self):
        print(self.greeting)