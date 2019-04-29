Helena Kwiat
Allison MacMillan
Final Project- Explanation of Idea

	We have created a statistic Defense Offense Weighted(DOW) that combines both the offensive and defensive abilities of a team. This information is relevant because this statistic fills the need for a meaure of weighting of abilities on a team, there currently only exists measures of how offensive or defensive a player​is but there are no sliding scale combination evaluations, or team evaluations. We have evaluated where a teams strengths and weaknesses lie in terms of offensive and defensive abilities by combining those of its players. Is a team extremely offensively heavy? Or do they spend all their money on pitchers? etc. In order to determine this we used fangraphs data and lahman data to comb through and combine the existing offensive and defensive statistics. We normalized and combine these existing statistics for offensive and defensive ability for the individual players. After creating our own version of individual player offensive and defensive statistics we normalized each of these respective values and added and averaged them all together to determine whether the weighting of an entire team is more heavily offensive or defensive. With this data we created a multitude of analysis’ about how weighting of ability affects wins. How attendance and salary can correspond to weighting of ability. How a teams weighting of ability can be attractive or unattractive to free agents.  etc...
In doing this we used the Off and Def statistics from Fangraphs. Off is a value that fangraphs uses to determine the value of a player offensively, using his batting runs and base running runs.
Off = Batting Runs Above Average + Base Running Runs Above Average
To calculate Batting Runs Above Average, we will use the Weighted Runs Above Average (wRAA) and adjust it based off of park using the following equations:
wRAA = ((wOBA – lgwOBA)/wOBA Scale)*PA
Batting Runs = wRAA + (lgR/PA – (PF*lgR/PA))*PA + (lgR/PA – (Specific League
non-pitcher wRC / Specific League non-pitcher PA))*PA
Base Running Runs Above Average is equal to ​BsR​. BsR = wSB + UBR + wGDP
Def is a statistic to measure how defensive a player is compared to an average player in the league. It takes into account both averages of other players in the same position as well as other positions. This is the equation for Def:
Def = Fielding Runs Above Average + positional adjustment
Fielding Runs Above Average is calculated using Ultimate Zone Rating (UZR), which is a statistic that fangraphs uses in calculating WAR. We must include positional adjustment because some positions have more opportunity for a player to act defensively than others.
After we calculated Off and Def for every player on a team, we averaged these on a per team basis to get a collective Off and Def for the whole team. We then normalized these to be in between a certain range, fliped def to be a negative value and combined them to create one statistic for the whole team. We beleive this statistic will be helpful to opposing teams when they want to learn what the strengths of the team are. It does not, however, tell you just how good a team is at offense or defense; just which one is favored by the team.
References: ​https://www.fangraphs.com/






HOSTED ON HEROKU:

https://sabermetrics-final-project.herokuapp.com

All we have left to do is format the graphs with javascript!
