from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700) # Size of apps

Builder.load_file('calc.kv') # Design kv file baseline

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0' # Clear function into 0

    def button_press(self, button):
        # Variable that ocntains with buttons
        prior = self.ids.calc_input.text

        if "ERROR!" in prior:
            prior = ''
        # When 0 occured
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def remove(self):
        prior = self.ids.calc_input.text
        # Remove last character functions
        prior = prior[:-1]
        # Output the rest
        self.ids.calc_input.text = prior

    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split text box by +
        num_list = prior.split("+")
        num_list[-1]

        if "+" in prior and '.' not in num_list[-1]:
            # Add a dcimal to the end of the text
            prior = f"{prior}."
            # Output back
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass

        else:
            # Add a dcimal to the end of the text
            prior = f"{prior}."
            # Output back
            self.ids.calc_input.text = prior

    # Function for adding sign to the numbers
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # See the sign is it '-' already
        if '-' in prior:
            self.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.calc_input.text = f'-{prior}'


    def math_sign(self, sign):
        # additions
        prior = self.ids.calc_input.text

        # Giving plus sign
        self.ids.calc_input.text = f"{prior}{sign}"

    def equals(self):
        # equals
        prior = self.ids.calc_input.text
        # Error handling
        try:
            # Evaluate math from the text box
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "ERROR!"


        '''
        # adition
        if "+" in prior:
            num_list = prior.split("+")
            # print(num_list)
            answer = 0.0
            # loop through list
            for number in num_list:
                answer = answer + float(number)
        
        # Print answer to textbox
        self.ids.calc_input.text = str(answer)
        '''

class MyApps(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApps().run()