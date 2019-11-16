### Predicting Voter Turnout

Last fall, 2018, the State of Georgia experienced a divisive gubernatorial election between Stacey Abrams and Brian Kemp fraught with explicit and systematic voter suppression [[1]](https://www.nytimes.com/2019/03/06/us/politics/governor-brian-kemp-voter-suppression.html?partner=IFTTT). The tactics employed by Brian Kemp and republican operatives included exact-match purging of voters from rolls and premature closure of polling locations. These tactics saw $85,000$ voters removed from the rolls in the three months leading up to the election and $667,000$ removed during 2017 [[]](). All told, more than 10% of eligible, primarily black, voters were removed from the rolls [[]](). The systematic and widespread suppression netted Brian Kemp a victory while inspiring the Fair Fight movement. In the spirit of Fair Fight, this project endeavors to predict voter turnout using machine learning techniques based on district-level infrastructure data.

### Dataset
![2018 Turnout for Most USA Counties](plots/Choropleth/counties.png)

Description to be added
  
![2018 State Turnout](plots/Choropleth/usa.png){:width="90%"}

![2018 Turnout](plots/Choropleth/GA.png){:height="50%" width="50%"}
![2018 Turnout](plots/Choropleth/AZ.png){:height="50%" width="50%"}

### Unsupervised Learning

#### K-means

We performed K-means clustering on the state election policy dataset and employed the elbow method to determine the ideal number of clusters:

![Elbow Method](plots/Kmeans/output_6_0.png)

Ideal number of clusters = 3.

![K-means](plots/Kmeans/newplot.png)

Silhouette Score (higher is better) = 0.538

#### Feature Extraction

Further, to determine which policies have the most impact on voter turnout, we performed Feature Extraction using the SelectKBest method which outputs the K features with the highest scores.

![Feature Extraction](plots/Kmeans/output_10_0.png)

### Supervised Learning

We used the county election infrastructure dataset to perform linear and lasso regression to predict voter turnout.

**Insert visualization for linear regression **Insert score for linear regression
![LR](plots/Linear_Lasso_Ridge/output_11_1.png)
![LR](plots/Linear_Lasso_Ridge/output_11_2.png)

LR training score: 0.014746881224901422
LR testing score: 0.000984805211150186

![LR](plots/Linear_Lasso_Ridge/test_actual.png){:height="80%" width="80%"}
![LR](plots/Linear_Lasso_Ridge/test_pred_linear.png){:height="80%" width="80%"}

**Insert visualization for lasso regression **Insert score for lasso regression

![Lasso](plots/Linear_Lasso_Ridge/output_12_1.png)
![Lasso](plots/Linear_Lasso_Ridge/output_16_1.png)

training score: 0.01418841818201566
test score:  -0.0006256370906636555
number of features used:  5
training score for alpha=0.001: 0.01418841818201566
number of features used: for alpha =0.001: 5
training score for alpha=0.0001: 0.014741296015963301
number of features used: for alpha =0.0001: 5
LR training score: 0.014746881224901422

![LR](plots/Linear_Lasso_Ridge/test_actual.png){:height="80%" width="80%"}
![Lasso](plots/Linear_Lasso_Ridge/test_pred_lasso.png){:height="80%" width="80%"}


### Related Work
Keeter et al. predicted voter turnout based on interviews, voter history, and demographics using random forest and logistic regression [[]](). Challenor predicted voter turnout using labor force demographics in [[]](). Unlike their work, we propose to predict voter turnout based on local infrastructure, including but not limited to distance from polling stations, as examined by [[]]().

### References
[1]  M. Astor, “Georgia governor brian kemp faces investigation by house panel,” 2019.

[2]  K. Shah, “Textbook voter suppression:  Georgia’s bitter election a battle years in the making,”TheGuardian, 2018.

[3]  S. Keeter, R. Igielnik, and R. Weisel, “Can likely voter models be improved?”Pew Research Center,2016.

[4]  T. Challenor, “Predicting votes from census data,” 2017.

[5]  M.  Haspel  and  H.  G.  Knotts,  “Location,  location,  location:   Precinct  placement  and  the  costs  ofvoting,”The Journal of Politics, 2005.
