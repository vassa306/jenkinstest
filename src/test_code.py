import os
class Hello: 
    
    def open_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return "Anonymous"
                
    def say_hello(self):
        file_path = os.path.join(os.path.dirname(__file__), "test.txt")
        name = self.open_file(file_path)
        print(f"Hello World! {name} its nice to meet you.")

if __name__ == "__main__":   
    hello = Hello()
    hello.say_hello()