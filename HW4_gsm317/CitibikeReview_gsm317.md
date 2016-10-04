# Gregory Mayes, HW4 Assignment #1

## a. verify that their Null and alternative hypotheses are formulated correctly

The development of their hypothesis is a little confusing in the wording. I take the alternative hypothesis to be "There is no [significant] difference in the average [mean] trip duration of subscribers in summer months as compared to the winter months." I think their null and alternative hypothesis should be reversed. Also, I'm not sure if the null hypothesis stated (H0 = u1 - u2 = 0) is falsifiable.

## b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

I don't agree with the assumption that the data contains outliers, because the Citibike website states:

*"This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure)"

Therefore, I think the outliers were already accounted for in the data source. It also technically wasn't necessary to separate the trip durations into bins, because this information won't be used to perform the statisical test.

## c. Chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or to the CSU cheat-sheet here, of Statistics in a Nutshell.

In this case, the independant variable is the time of year, specifully winter or summer, and variable type is categorical dichotomous. The dependant variable is trip duration and variable type is continuous interval. Therefore, according to the table, the most appropreiate test is the t-Test, which answers "Do differences exist between 2 or more groups on one DV?"
