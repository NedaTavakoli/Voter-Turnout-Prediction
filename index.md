### Voter Turnout Prediction.
Last fall, 2018, the State of Georgia experienced a divisive gubernatorial election between Stacey Abrams and Brian Kemp fraught with explicit and systematic voter suppression [[1]](https://www.nytimes.com/2019/03/06/us/politics/governor-brian-kemp-voter-suppression.html?partner=IFTTT). The tactics employed by Brian Kemp and republican operatives included exact-match purging of voters from rolls and premature closure of polling locations. These tactics saw $85,000$ voters removed from the rolls in the three months leading up to the election and $667,000$ removed during 2017 [[]](). All told, more than 10% of eligible, primarily black, voters were removed from the rolls [[]](). The systematic and widespread suppression netted Brian Kemp a victory while inspiring the Fair Fight movement. In the spirit of Fair Fight, this project endeavors to predict voter turnout using machine learning techniques based on district-level infrastructure data.

### Dataset


### Methods
 We will leverage three machine learning methods, one supervised and two unsupervised methods. More specifically, we plan to apply logistic regression, k-means clustering and Principle Component Analysis (PCA) on our dataset. We shall use logistic regression to determine which dependent features have more effect on voter turnout.

### Results and discussions



### Related works
Keeter et al. predicted voter turnout based on interviews, voter history, and demographics using random forest and logistic regression [[]](). Challenor predicted voter turnout using labor force demographics in [[]](). Unlike their work, we propose to predict voter turnout based on local infrastructure, including but not limited to distance from polling stations, as examined by [[]]().

### References
[1]  M. Astor, “Georgia governor brian kemp faces investigation by house panel,” 2019.

[2]  K. Shah, “Textbook voter suppression:  Georgia’s bitter election a battle years in the making,”TheGuardian, 2018.

[3]  S. Keeter, R. Igielnik, and R. Weisel, “Can likely voter models be improved?”Pew Research Center,2016.

[4]  T. Challenor, “Predicting votes from census data,” 2017.

[5]  M.  Haspel  and  H.  G.  Knotts,  “Location,  location,  location:   Precinct  placement  and  the  costs  ofvoting,”The Journal of Politics, 2005.
