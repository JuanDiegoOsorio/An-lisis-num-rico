funcion4punto <- function(x){
  exp(x) * (x^2* exp(-x) + x* exp(-x) + 1)
}


plotsish <- c(taylor(funcion4punto, x0=0, n = 3))

plot(plotsish, col = "green", main = "TAYLOR")
