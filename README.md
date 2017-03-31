# RL based strategy for the iterated games

This is the implementation work for results verification.



RLS4IPD is for the iterated Prisoner's Dilemma part.

* Run the [RoundrobinTour.py](https://github.com/ExperimentVerification/RLStrategy/blob/master/RLS4IPD/RoundrobinTour.py) for the round-robin tournament for the IPD. However, you will need to comment some of the lines or change the parameters according to the game settings mentioned.

* Run the [EcologicalTour.py](https://github.com/ExperimentVerification/RLStrategy/blob/master/RLS4IPD/EcologicalTour.py) for the ecological approach of evaluating the IPD strategies. It is also necessary to comment some lines and change some of the parameters if needed. 




RLS4IDGPD is for the iterated Double-Game Prisoner's Dilemma part.



[RewardFuncExample.txt](https://github.com/ExperimentVerification/RLStrategy/blob/master/RewardFuncExample.txt) compares the differences in trainig Q-tables with varying reward functions (i.e., whether both negative and non-negative rewards are needed).


Run the [Tournament.py](https://github.com/ExperimentVerification/RLStrategy/blob/master/RLS4IDGPD/Tournament.py), which is the round-robin tournament for the DGPD, implemented according to Boyd's Material Versus Social Payoff Tournament. 

Python Version used: 2.7.11
