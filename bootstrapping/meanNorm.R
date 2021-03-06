# Try bootstrapping on small sample from normal distribution.

mean <- 10
sd <- 5
n <- 10
sample <- rnorm(n = n, mean = mean, sd = sd)

# Resampling.
N <- 100000
resample.means <- rep(0, N)
resample.std <- rep(0, N)
for (i in 1:N){
  # Bootstrap methods of resampling. 
  new.sample <- sample(sample, n, replace = TRUE)
  resample.means[i] <- mean(new.sample)
  resample.std[i] <- sqrt(var(new.sample))
}

par(mfrow=c(1,2))
hist(resample.means)
hist(resample.std)
mean(resample.means) # Find mean of all resampled means. 
mean(resample.std) # Find mean of all resampled std.

# Seems to work pretty well! If the mean of original distribution is unknown, 
# it can be approximated by the mean of resampled means (also get a feeling from the histogram).
# Could/should also find/plot confidence interval. 