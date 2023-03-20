riemann_sum <- function(n, a, b, fx, ...) {
    intervals <- seq(a, b, length = n)
    ci <- c()
    sum_value <- c()

    for(i in 1:c(n-1)) {
        delta_i <- (intervals[i+1] - intervals[i])
        ci[i] <- (intervals[i+1] + intervals[i]) / 2
        sum_value[i] <- fx(ci[i]) * delta_i
    }
    
    return(sum(sum_value))
}

riemann_sum <- Vectorize(riemann_sum, 'n')
riemann_sum(n=100, a=1, b=2, fx=function(x) x^2)