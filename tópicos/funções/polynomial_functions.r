linear_function <- function(x){
    y <- 5*x
    return(y)
}

quadratic_function <- function(x) {
    y <- x^2
    return(y)
}

exponential_function <- function(x){
    y <- 2^x
    return(y)
}

x_vec <- -5:5
# x_vec <- -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

print(linear_function(2))
print(linear_function(x_vec))
