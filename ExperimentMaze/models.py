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
    score1=models.IntegerField()
    score2=models.IntegerField()
    score3=models.IntegerField()
    score4=models.IntegerField()
    score5=models.IntegerField()
    time1=models.FloatField()
    time2=models.FloatField()
    time3=models.FloatField()
    time4=models.FloatField()
    time5=models.FloatField()
    residence=models.StringField()
    age=models.IntegerField(min=18, max=99)
    condition=models.StringField(choices=["Base","KM","KLM"])

            