# Define data
Price <- c(9,12,15,6,10,8,45,17,10,7,6,20,7,40,15,10,10,18,19,10,10,7,55,7,55,7,9,10,10,8,7,
           6,7,40,17,7,6,11,50,7,6,40,7,17,70,7,10,55,48,7,10,7,48,7,60,15,8,7,7,7,15,12,6,20,55,20,
           8,25,15,7,6,6,6,7,6,7,20,10,49,15,14,10,7,10,7,10,19,9,7,15,9,10,9,9,15,15,55,10,9,9)

# Calculate basic statistics
num <- length(Price)
sprintf("Amount of data is %d", num)

print("Price")
Price

# Mean and Standard Deviation
meanData <- mean(Price)
sdData <- sd(Price)
sprintf("Mean of Data is %.4f", meanData)
sprintf("Standard deviation is %.4f", sdData)

# Median
medianData <- median(Price)
sprintf("Median of Data is %.4f", medianData)

# Standard Error and Margin of Error
SE <- sdData / sqrt(num)
sprintf("Standard Error is %f", SE)
E <- qt(0.975, df = num - 1) * SE
E # Margin of Error
meanData + c(-E, E)

# Plot histogram
hist(Price, probability = TRUE, main = "Histogram of Price", xlab = "Price")

# Normality test (Shapiro-Wilk)
shapiro.test(Price)

# Compute Z-value
mufood <- 2.6 # Hypothesized value
z <- (meanData - mufood) / SE
z

# Compute Critical Z-value
alpha <- 0.05
z.half.alpha <- qnorm(1 - alpha / 2)
c(-z.half.alpha, z.half.alpha)

# Compute p-value
pvalDataFood <- 2 * pnorm(z)
pvalDataFood

# Correlation analysis
Data2 <- rep(1, 90)
Data2[91:96] <- 2
Data2[97:99] <- 3
Data2[100:101] <- 4

Data3 <- c(4,5,4,5,2,3,3,4,5,4,4,4,4,4,3,3,4,5,5,4,5,5,5,5,5,3,4,4,4,4,5,5,4,4,4,3,4,4,
           5,4,3,5,4,4,2,5,2,5,3,4,1,3,3,1,5,5,4,5,4,4,5,5,5,5,4,5,4,5,5,5,3,4,1,3,3,4,3,5,5,3,4,4,
           5,4,5,5,5,5,3,5,5,5,5,3,5,5,5,5,2,5)

print("Data2")
Data2

correlation <- cor(Price, Data3)
sprintf("Correlation between groups is %f", correlation)

# Linear Regression
grade.lm <- lm(Price ~ Data3)
coeffs <- coefficients(grade.lm)
sprintf("Simple regression equation coefficients: %s", coeffs)

r_squared <- summary(grade.lm)$r.squared
sprintf("Coefficient of determination is %f", r_squared)

# T-test
meanData3 <- mean(Data3)
print("Data3")
Data3

muStore <- 15.4 # Hypothesized value
s <- 2.5 # Sample standard deviation
t <- (meanData3 - muStore) / (s / sqrt(num))
t

# Compute Critical T-value
alpha <- 0.05
t.half.alpha <- qt(1 - alpha / 2, df = num - 1)
c(-t.half.alpha, t.half.alpha)

# Compute p-value
pvalDataStore <- 2 * pt(t, df = num - 1)
sprintf("P-value of DataStore is %.4f", pvalDataStore)