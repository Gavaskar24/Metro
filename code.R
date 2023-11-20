# Read data
data <- read.csv("code.csv", header = TRUE, sep = ",")
# Consider only columns ACCESS_DIS_MAX, ACCESS_DIS_MIN, ACCESS_M, and ACCESS_TIME
data <- data[, c("ACCESS_DIS_MAX", "ACCESS_DIS_MIN", "ACCESS_M", "ACCESS_TIME")]

# Create a survival object with interval censoring
# Define upper and lower bounds for the intervals
Y <- Surv(time = data$ACCESS_DIS_MAX, time2 = data$ACCESS_DIS_MIN, event = 'interval2')

# Fit a Cox model
fit <- coxph(Y ~ ACCESS_M + ACCESS_TIME, data = data)
# Print the results
summary(fit)