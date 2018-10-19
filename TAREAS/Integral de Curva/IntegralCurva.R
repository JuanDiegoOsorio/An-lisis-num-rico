deg2rad <- function(deg) {
  return((deg * pi) / (180))
  }


LongitudCurva <- function(funcion, ex1, ex2){

  
  return(integrate( function(x) {sqrt( 1 + cos(x)*cos(x))}, lower = ex1, upper = ex2))
  
}


exp1 <- 0
exp2 <- 2
funcion <- expression(sin(x))
x <- D(funcion,"x")
resul <- LongitudCurva(x, exp1, exp2)

resul

resultadof <- resul[["value"]]
deg2rad(resultadof) 