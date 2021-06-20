##הלוגיקה של המעבר בין הדפים

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player
import numpy as np


            
class Intro(Page):  ###class pagename(Page) 
    def is_displayed(self):
        return self.round_number==1
    
class Demographics(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields=['age','gender','residence','education']    
    def is_displayed(self):
        return self.round_number==1
    
class MainBASE(Page):  ###class pagename(Page) 
    def is_displayed(self):
         if self.player.condition=="Base":
             return self.round_number==1
         else:
             return False
         
class MainKM1(Page):  ###class pagename(Page) 
    def is_displayed(self):
         if self.player.condition=="KM":
             return self.round_number==1
         else:
             return False
         
class MainKLM2(Page):  ###class pagename(Page) 
    def is_displayed(self):
         if self.player.condition=="KLM":
             return self.round_number==1
         else:
             return False
    
class MazeKM1(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score1','time1']  
    def is_displayed(self):
         if self.player.condition=="KM":
             return self.round_number==1
         else:
             return False
    
class MazeKM2(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score2']
    def is_displayed(self):
         if self.player.condition=="KM":
             return self.round_number==1
         else:
             return False
    
class MazeKM3(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score3']
    def is_displayed(self):
       if self.player.condition=="KM":
           return self.round_number==1
       else:
             return False
         
class MazeKM4(Page):  ###class pagename(Page)
    form_model='player'
    form_fields = ['score4']
    def is_displayed(self):
        if self.player.condition=="KM":
            return self.round_number==1
        else:
             return False
    
class MazeKM5(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score5']
    def is_displayed(self):
      if self.player.condition=="KM":
          return self.round_number==1
      else:
             return False

class MazeKLM1(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score1']
    def is_displayed(self):
         if self.player.condition=="KLM":
             return self.round_number==1
         else:
             return False
    
class MazeKLM2(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score2']
    def is_displayed(self):
         if self.player.condition=="KLM":
             return self.round_number==1
         else:
             return False
    
class MazeKLM3(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score3']
    def is_displayed(self):
        if self.player.condition=="KLM":
            return self.round_number==1
        else:
             return False

class MazeKLM4(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score4']
    def is_displayed(self):
        if self.player.condition=="KLM":
            return self.round_number==1
        else:
             return False
    
class MazeKLM5(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score5']
    def is_displayed(self):
        if self.player.condition=="KLM":
            return self.round_number==1
        else:
             return False
         
class MazeMM1(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score1']    
    def is_displayed(self):
        if self.player.condition=="Base":
            return self.round_number==1
        else:
             return False

    
class MazeMM2(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score2']
    def is_displayed(self):
       if self.player.condition=="Base":
           return self.round_number==1
       else:
           return False
    
class MazeMM3(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score3']
    def is_displayed(self):
       if self.player.condition=="Base":
           return self.round_number==1
       else:
           return False

class MazeMM4(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score4']
    def is_displayed(self):
        if self.player.condition=="Base":
           return self.round_number==1
        else:
           return False
    
class MazeMM5(Page):  ###class pagename(Page) 
    form_model='player'
    form_fields = ['score5']
    def is_displayed(self):
       if self.player.condition=="Base":
           return self.round_number==1
       else:
           return False
 
class End(Page):
    def is_displayed(self):
        return self.round_number==1


page_sequence = [Intro, Demographics, MainKLM2, MainBASE, MainKM1, MazeKLM1, MazeKLM2, MazeKLM3, MazeKLM4, MazeKLM5, MazeMM1,MazeMM2,MazeMM3,MazeMM4,MazeMM5, MazeKM1, MazeKM2, MazeKM3, MazeKM4, MazeKM5, End]


#document.getElementById('score').value = heroScore();
