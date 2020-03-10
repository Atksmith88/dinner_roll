# Dinner Roller

This little project is designed to create a random roller to select a dinner option for a potential date night. My girlfriend and I frequently cannot decide where to go, so we came up with these lists to allow us to roll dice to select. This project can be used both with physical dice, or by using the random rolling options within the program here.

Note: Many of the restaurants show up multiple times in multiple lists. This is due to those restaurants having a varied menu. Because of this, the idea is that you must select something at that restaurant from the category that was originally rolled. For example, Kerbey Lane Cafe shows up in Breakfast, American, Bakery/Cafe, and Burgers, so if you rolled Kerbey Lane in Breakfast, you would need to order something from their breakfast menu, while if you rolled it within Burgers, you would have to order a burger.

Second Note: Something New is pretty self-explanatory, it means ya'll get to go somewhere that neither of you have been before. Who knows, you might find a place you both really like!

Final Note: These lists were created for the North Austin Texas area. If you want to change the lists, you can clone your own copy of this repository and change the lists within the lists.py file.


```python
from lists import *
import random
from roller_function import roll
from IPython.display import clear_output
roll()
```
