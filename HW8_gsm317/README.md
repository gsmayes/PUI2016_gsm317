
# Visualization by cx495
![Visualization to review by cx495](https://raw.githubusercontent.com/gsmayes/PUI2016_gsm317/master/HW8_gsm317/cx495.png)

## Review by gsm317
 - The axis tick labels for number of rides is difficult to read, as are the description labels for both axes.
 - The legend colors don't match the plot, red looks purple due to an overlap with blue.
 - The error bars are very small relative to the plot bars and are difficult to differentiate between the days of the week.
 - The customer plot bars are very small compared to subscribers and it's difficult to gauge their value against each other and the y-axis
 - The figure caption contained in the ipython notebook doesn't define rides (citibike) or the data source.
 
Overall, I think the main point of this plot is the comparison of customer rides in relation to the subscriber rides through out the week. Rather than representing total rides for both categories, maybe show total rides in thousands and the percentage of customer rides within the bar for total rides. Also, I'm not sure if there was a particular reason for selecting the month of March, but I suggest using multiple months of data during peak periods of outdoor activity (June, July and August). It would also be interesting to investigate if there is a correlation between customer rides and tourist population (or hotel occupancy rates, airport arrivals, etc.)


# Visualization by lag552
![Visualization to review by lag552](https://raw.githubusercontent.com/gsmayes/PUI2016_gsm317/master/HW8_gsm317/lag552.png)

## Review by gsm317
 - The data being used is not clear to me because I don't believe there are any prisons for violent offenders in New York City. I suspect the inmate population represents detention facilities operated by the NYC Department of Corrections, chiefly on Rikers Island and with smaller facilities in several boroughs. Traditionally, prisons are facilities for long term incarceration after conviction, while jails are temperary holding facilities for shorter sentences, people awaiting trail or court appearances on appeal. It's also not clearly stated if the population is men, women or both and what level of incarceration or security.
 - It might be helpful to represent the number of incidents as per capita against inmate population in thousands. This would make the scale of each axis more similar.
 - It's not clear to me why specifically stabbings/slashings were used rather than the overall violent incidents, which may be less random.

Overall, the plot is very clear in conveying it's point, but a more interesting analysis might be using the New York State inmate population of 55,245 for the larger sample size and breaking the data down by prison facility or even better by cell block to increase data points. Also, further specify the population by security level (maximum), gender (males are much more likely to commit violent crimes), age and/or sentence length. Also, this would allow the use of a single year of data, which would better represent the relationship between violence and inmate population by minimizing unknown variables through time (changing policies, etc.).
