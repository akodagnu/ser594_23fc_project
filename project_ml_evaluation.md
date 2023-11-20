#### SER594: Machine Learning Evaluation
#### Room Occupancy Estimation
#### Akshata Bharadwaj Kodagnur
#### 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error

**Choice Justification:** Since I am performing regression, MSE and R2 score are the commonly used metrics. Squaring the errors penalizes larger errors more heavily than smaller errors. MSE also provides a measure of the spread or variability of the errors.

### Metric 2
**Name:** R Squared Score

**Choice Justification:** R2 score measures the proportion of the variance in the dependent variable that is predictable from the independent variables.
This score provides a normalized measure of model performance: R2 score ranges from 0 to 1, where 1 indicates perfect predictions.

## Alternative Models
### Alternative 1
**Construction:** Used hyperparameter tuning on my original model. Changed the n_estimators to 50 and max_depth to 20.

**Evaluation:** This model does almost as well as the original model with only a few digits difference in the mse and r2 score.

### Alternative 2
**Construction:** Used hyperparameter tuning on my original model. This time I changed max_features to 2.

**Evaluation:** This model did not do as well as the original model and alternative model 1.

### Alternative 3
**Construction:** Split my dataset into two uneven subsets. 

**Evaluation:** The model that trained with the bigger of the two subsets did comparatively well. But it is still not as good as the original model.

## Best Model

**Model:** Alternative 1 performed the best with least mean squared error and highest r2 score.