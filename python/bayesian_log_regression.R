install.packages("here")
library(here)
library(ggplot2)

df <- read.csv(here("data", "cleaned", "nyts_2021_2023_clean.csv"))

x <- sum(df$usage, na.rm = TRUE)
n <- nrow(df)

# Define the prior distribution
prior <- function(theta, alpha=2, beta = 18) {
  ifelse(theta >= 0 & theta <= 1, (theta^(alpha - 1) * (1 - theta)^(beta - 1)) / beta(alpha, beta), 0)
}

# Define the posterior distribution
good_posterior <- function(theta, x, n, alpha=2, beta=18) {
  alpha_star <- alpha + x
  beta_star <- beta + (n - x)
  
  log_post <- ifelse(theta >= 0 & theta <= 1,
                     (alpha_star - 1) * log(theta) +
                       (beta_star - 1) * log(1 - theta) -
                       log(beta(alpha_star, beta_star)), -Inf)
  
  exp(log_post)
}


sim_theta <- seq(0, 1, length.out = 1000)
prior_dist <- prior(sim_theta)
# post_dist  <- good_posterior(sim_theta, x, n)

# plot_df <- data.frame(theta = sim_theta, Prior = prior_dist, Posterior = post_dist)
# ggplot(plot_df, aes(x = theta)) +
#   geom_line(aes(y = Prior, color = 'pink')) +
#   geom_line(aes(y = Posterior, color = 'purple')) +
#   labs(x = expression(theta), y = expression(p(theta))) +
#   scale_color_manual(name = "Legend", values = c("pink" = "pink", "purple" = "purple"))
