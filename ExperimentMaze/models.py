from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
import itertools


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants): 
    name_in_url = 'ExperimentMaze'  ##Name of exp
    players_per_group = None
    num_rounds = 1
    payratio= None


class Subsession(BaseSubsession): ## Randomization to groups
     def creating_session(subsession):
    # randomize to treatments
        for player in subsession.get_players():
            player.condition=random.choice(["Base","KM","KLM"])
        condition=itertools.cycle(["Base","KM","KLM"])
        for player in subsession.get_players():
            player.condition=next(condition)
            
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender=models.StringField(choices=["Male","Female","Other"])
    education=models.StringField(blank=True)
    score1=models.IntegerField(initial=999)
    score2=models.IntegerField(initial=999)
    score3=models.IntegerField(initial=999)
    score4=models.IntegerField(initial=999)
    score5=models.IntegerField(initial=999)
    residence=models.StringField()
    age=models.IntegerField(min=18, max=99)
    condition=models.StringField(choices=["Base","KM","KLM"])

            