from guizero import App, Text

app = App(title="Hello world")

welcome_message = Text(app, text="Welcome to my app", size=40, font="times new roman", color="red")

app.display()

# https://projects.raspberrypi.org/en/projects/getting-started-with-guis/7