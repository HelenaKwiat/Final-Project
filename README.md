# Explanation of Statistic #
### Allison MacMillan and Haley Kwiat ###

Our statistic, Defense Offense Weighted (DOW), measures how defensive or offensive a team is overall. Instead of measuring each skill respectively like statistics like Off and Def do, DOW represents where a team’s strengths lie. This information is relevant because this statistic fills the need for a measure of a weighting of abilities on a team. There currently only exist measures of how offensive or defensive a player ​is but there are no sliding scale combination evaluations or team evaluations. 
   
This statistic is most comparable to the other defensive and offensive statistics that exist, such as UZR, DRS, wOBA, and SLG. DOW, however, measures a team’s overall leaning to either being better at defense or offense, instead of individual skills. Because of this, DOW is a broader statistic. It would be helpful for an opposing team to look at before they play, so they know whether to focus more energy into their defense or offense.
   
In order to do this, we used the Off and Def statistics that exist in Fangraphs for 2019. We used the batting, pitching, and fielding files of data for this, which contained every player and their statistics. Since these statistics have different ranges and different calculations in order to create them, we first needed to normalize both statistics in every dataset. The following is the equation we used, with rmin equal to 0 and rmax equal to 10. 
   
Now all of our data points were between 0 and 10. After this, we needed to average each statistic (Def and Off) for each team since our goal was to have a statistic measuring teams.
It turns out that both the batting and fielding both have a Def column, while pitching is the only dataset with an Off column. In order to fix this, we treated each Def statistic in both datasets as its own player. This shouldn’t mess up our results since we are simply averaging each statistic for each team.    

After getting a normalized version of Def and Off for each team between 0 and 10, we needed to combine them. This was done by multiplying each Def by -1 and then adding this to Off for each team. This now gives us a statistic that tells us a little bit about the teams' strengths. If the number is higher, they are more offensive compared to defensive. If the number is lower, they are more defensive compared to offensive. If a team has a very negative number, however, it does not mean they are more defensive than other teams; just that their own strengths are lie in defense as opposed to offense within their own team. We then merged this statistic for each team with Lahman data for Salary, Wins, and Attendance on a per team basis in order to get an idea of how our statistic affected these measurable data points.  

After calculating the statistic we found that almost all of the teams in the league are defensively weighted, barring the Seattle Mariners who have hit an almost record-breaking 36 home runs so far this season. This could be because of many reasons, possibly because there are so few pitchers as compared to batters who tend to bring the defensive average up. Or possibly because it’s easier to be a great fielder than it is to be a great batter. This may be an outlandish claim, but with a ball coming at a batter at 95 mph I think it’s something we can all agree has some truth to it. The bottom graph on our site shows how our statistic compares to Def and Off. 
    
There is an interesting fact about this defensive weighting, concluded in our statistic, across most teams in the league. We have found through the analysis we put our statistic against, Salary, Wins, and Attendance, that there seems to be a (somewhat weak) but existent positive correlation between higher attendance, salary and wins with higher offensive weighting from our statistic. The statistic with the most obvious positive correlation to DOW was attendance. This makes sense to us because teams who are very offensive score lots of home runs. Home runs are, naturally, exciting to watch, so they can draw a larger crowd: thus attendance.

For the development of our application, we originally thought we would use Django which is supposed to allow for easy python and front end integration. However, both of us have minimal CSS development experience. We found Django to be not user-friendly at all and we ran into many problems simply trying to get the routing and templating working correctly. At this point, we decided to maybe explore another framework. We found flask which is supposed to be much more seamless and user-friendly. It absolutely was, even though there wasn’t as much documentation out there for flask as there was for Django. 

After we found flask, we were easily able to create our templates for the homepage and the button-clicked page and integrate our python code from the jupyter notebook. Our biggest challenge after this was formatting with CSS, which we did by hand: big mistake. It took us hours to get things centered correctly and even after this we still found issues when you change the size of your screen. Also, the formatting seems to work better on Safari than Chrome, so we recommend using Safari for testing. Our next big frontier was getting it hosted on Heroku, which also took an obscene amount of time. We had problems with the requirements file and getting flask properly integrated.  

## References ##   
​https://www.fangraphs.com/

## Link to Web Application ##  
https://sabermetrics-final-project.herokuapp.com 

## Link to Video Presentation ##  
https://www.youtube.com/watch?v=C380wTxqmDE&feature=youtu.be

## Contents of Repo ##  
Jupyter directory - code and CSV files used for generating the statistic  
GenerateData.py - python code copied from Jupyter notebook  
Templates directory - html files  
Static directory - CSS style and background photo  
Hello.py - index file for flask application  
Procfile - for Heroku  
Fangraphs Data  
Pybaseball Directory - pybaseball functions  
Flask App Integration  
Baseballdatabank-2017.1 - Lahman data files

