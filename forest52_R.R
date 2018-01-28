#Data processing 
# for machine learning course A-Z


#importing dataset
dataset = read.csv('Salary_Data.csv')

#dealing with missing values
"""dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

#Encoding Categorical data (C is a vector)
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(1, 0))"""

##splitting dataset into training and test set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset (dataset, split == TRUE)
test_set     = subset (dataset, split == FALSE)

#Feature Scaling
#No need to apply for linear regression as R package does it byself
"""training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])#"""

#Fitting Simple linear regression on training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)
#if you need some info about regressor type it in console     summary (regressor)

#Predicting the test set result
y_pred = predict(regressor, newdata = test_set)
#Visualising the Training set results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary Vs Experieince(Training Set)') +
  xlab('Years of Experieince') +
  ylab('Salary')

#Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary Vs Experieince(Test Set)') +
  xlab('Years of Experieince') +
  ylab('Salary')