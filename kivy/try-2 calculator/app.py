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

        # When 0 occured
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def dot(self):
        ### For decimal
        prior = self.ids.calc_input.text

        if '.' in prior:
            pass
        else:
            # add decimal to the end of the text
            prior = f"{prior}."
            # printout into text box
            self.ids.calc_input.text = prior

    def math_sign(self, sign):
        # additions
        prior = self.ids.calc_input.text

        # Giving plus sign
        self.ids.calc_input.text = f"{prior}{sign}"

    def equals(self):
        # equals
        prior = self.ids.calc_input.text

        # adition
        if "+" in prior:
            num_list = prior.split("+")
            # print(num_list)
            answer = 0
            # loop through list
            for number in num_list:
                answer = answer + int(number)
        
        # Print answer to textbox
        self.ids.calc_input.text = str(answer)

class MyApps(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApps().run()