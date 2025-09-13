import random
class PasswordGenerator:
    def __init__(self, length=int):
        self.length = length
        
    def generator(self):
        gibber = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ( ) _ + = - ? / : ;[ ] ~ ` '
        self.gibber_lst = gibber.split()   
        pin = '1 2 3 4 5 6 7 8 9 0'
        self.pin_lst = pin.split()

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length=int):
        super().__init__(length)
    
    def generator(self):
        super().generator()
        generated_rpassword_lst = random.sample(self.gibber_lst, self.length)
        final_random_password = ''.join(map(str, generated_rpassword_lst))
        return final_random_password
    
class PinGenerator(PasswordGenerator):
    def __init__(self, length=int):
        super().__init__(length)
    
    def generator(self):
        super().generator()
        generated_pin_lst = random.sample(self.pin_lst, self.length)
        final_pin = ''.join(map(str, generated_pin_lst))
        return final_pin
        
class CustomPasswordGenerator(PasswordGenerator):
    def __init__(self, length=int, custom_str=str):
        super().__init__(length)
        self.custom_str = custom_str
        
    def generator(self):
        super().generator()
        custom_lst = list(self.custom_str)
        if self.length > len(custom_lst):
            raise ValueError("Length exceeds the number of unique characters in the custom string.")
        generated_cpassword_lst = random.sample(custom_lst, self.length)
        final_custom_password = ''.join(map(str, generated_cpassword_lst))
        return final_custom_password

if __name__ == "__main__":
    rpassword = RandomPasswordGenerator(12)
    print("Random Password:", rpassword.generator())
    
    pin = PinGenerator(4)
    print("PIN:", pin.generator())
    
    custom_password = CustomPasswordGenerator(8, "CustomStr123!")
    print("Custom Password:", custom_password.generator())