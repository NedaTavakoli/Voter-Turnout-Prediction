### Predicting Voter Turnout

Last fall, 2018, the State of Georgia experienced a divisive gubernatorial election between Stacey Abrams and Brian Kemp fraught with explicit and systematic voter suppression [[1]](https://www.nytimes.com/2019/03/06/us/politics/governor-brian-kemp-voter-suppression.html?partner=IFTTT). The tactics employed by Brian Kemp and republican operatives included exact-match purging of voters from rolls and premature closure of polling locations. These tactics saw $85,000$ voters removed from the rolls in the three months leading up to the election and $667,000$ removed during 2017 [[]](). All told, more than 10% of eligible, primarily black, voters were removed from the rolls [[]](). The systematic and widespread suppression netted Brian Kemp a victory while inspiring the Fair Fight movement. In the spirit of Fair Fight, this project endeavors to predict voter turnout using machine learning techniques based on district-level infrastructure data.

### Dataset
<!---
![2018 Turnout for Most USA Counties](plots/Choropleth/counties.png)-->

Description to be added
  
![2018 State Turnout](plots/Choropleth/usa.png) 

<img src="plots/Choropleth/GA.png" alt="GA" width="400"/>

<!---![2018 Georgia Turnout](plots/Choropleth/GA.png)-->



### Unsupervised Learning

We performed clustering on the state-wise voter turnout dataset across two dimensions: first we merged together similar features using FeatureAgglomeration for dimensionality reduction; next, we clustered together similar states based on election policy using k-means.

#### K-means

We employed the elbow method to determine the ideal number of clusters and then performed k-means on the state voter-turnout dataset:

![Elbow Method](plots/Kmeans/output_6_0.png)

Ideal number of clusters = 3.

![K-means](plots/Kmeans/newplot.png)

Silhouette Score (higher is better) = 0.538

#### Feature Extraction

Further, to determine which policies have the most impact on voter turnout, we performed Feature Extraction using the SelectKBest method which outputs the K features with the highest scores.

![Feature Extraction](plots/Kmeans/output_10_0.png)

### Supervised Learning

We used the county election infrastructure dataset to perform linear and lasso regression to predict voter turnout.
Lasso regression is used to reduce model complexity and prevent over-fitting which may result from simple linear regression.

So lasso regression puts constraint on the coefficients (w). A penalty term (lambda) regularizes the coefficients such that if the coefficients take large values the optimization function is penalized. So, lasso regression shrinks the coefficients and it helps to reduce the model complexity and multi-collinearity. In addition, Lasso uses regularization (L1) that can lead to zero coefficients i.e. some of the features are completely neglected for the evaluation of output. So Lasso regression not only helps in reducing over-fitting but it can help us in feature selection.

#### LINEAR REGRESSION

![Linear](plots/Linear_Lasso_Ridge/LinearRegression.PNG)

| Training score | Test score:  |
|----------------|--------------|
|    0.01477     |   0.00256    | 


<!---![LR](plots/Linear_Lasso_Ridge/test_actual.png){{height="500px" width="400px"}
![LR](plots/Linear_Lasso_Ridge/test_pred_linear.png){height="500px" width="400px"}-->


#### LASSO REGRESSION
The following plots show lasso regression results:

![Lasso](plots/Linear_Lasso_Ridge/LassoRegression.PNG)


  |     Alpha     | Training score|  Test score    |# Features used|
  |:-------------:|:-------------:|:--------------:|:-------------:| 
  |     0.001     |   0.0138      |    0.01047     |        5      |
  |    0.0001     |   0.0138      |    0.01047     |        5      |
  |    0.00001    |   0.0144      |    0.01185     |        5      |

<!---![LR](plots/Linear_Lasso_Ridge/test_actual.png){height="500px" width="400px"}
![Lasso](plots/Linear_Lasso_Ridge/test_pred_lasso.png){height="500px" width="400px"}-->

<!---Feature Extraction for county level dataset reveals 
![LR](plots/Linear_Lasso_Ridge/Feature_Extraction.PNG)-->

<!---Correlation between voter turnout and the different features in the dataset indicates:
![LR](plots/Linear_Lasso_Ridge/Correlation.PNG)-->

<!---We have a positive correlation between the number of voters assigned to a polling location and the voter turnout. Other features, while significant, are negetively correlated with voter turnout per our trained model.-->

### Related Work
Keeter et al. predicted voter turnout based on interviews, voter history, and demographics using random forest and logistic regression [[]](). Challenor predicted voter turnout using labor force demographics in [[]](). Unlike their work, we propose to predict voter turnout based on local infrastructure, including but not limited to distance from polling stations, as examined by [[]]().

### References
[1]  M. Astor, “Georgia governor brian kemp faces investigation by house panel,” 2019.

[2]  K. Shah, “Textbook voter suppression:  Georgia’s bitter election a battle years in the making,”TheGuardian, 2018.

[3]  S. Keeter, R. Igielnik, and R. Weisel, “Can likely voter models be improved?”Pew Research Center,2016.

[4]  T. Challenor, “Predicting votes from census data,” 2017.

[5]  M.  Haspel  and  H.  G.  Knotts,  “Location,  location,  location:   Precinct  placement  and  the  costs  ofvoting,”The Journal of Politics, 2005.
