library(devtools)
install.packages("devtools")
devtools::install_github("ProjectMOSAIC/fetch")
require("ProjectMOSAIC/fetch")
fetch::fetchData("mPP.R")
fetch::fetchData("DiffEQ.R")

SIR = function(S, I){ a =0.0026; b=0.5
                    dS = -a*S;
                    dI = a*S*I - b*I
                    return (c(dS,dI))}

mPP (DE= SIR, xlim = c(0,1000), ylim = c(0,1000))
