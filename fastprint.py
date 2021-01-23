import time
import threading


# printer = Printer(5)
# printer.print("Hello")  # Prints "Hello" every 5 seconds until printer.stop() called.

# printer = Printer(1, until=10)
# printer.print("Sup")  # Prints "Sup" every 1 seconds 10 times.


class Printer(threading.Thread):
    def __init__(self, delay: int, until=0):  # until = steps, 0 default until .stop() called
        self.delay = delay
        self.step = 0
        self.until = until
        self.text = None
        self.active = 1
        threading.Thread.__init__(self)

    def print(self, text):
        self.text = text
        self.start()

    def run(self):
        print(f"Printer {self} started.")
        if not self.text:
            print(f"Text missing. Assign text to .text property.")
        threading.Thread.__init__(self)
        while self.active:
            if self.until:
                if self.step >= self.until:
                    break
            self.step += 1
            print(self.text)
            time.sleep(self.delay)

    def stop(self):
        self.active = 0

    def __str__(self):
        # Human representation of current Printer object.
        return f"<Printer <{self.delay}:{self.until}>"


printer = Printer(5)
printer.print("Printing every 5 seconds until .stop() called.")

printer2 = Printer(1, 10)
printer2.print("Stopping after 10 prints.")

time.sleep(30)

printer.stop()
print(f"Printer {printer} stopped.")
