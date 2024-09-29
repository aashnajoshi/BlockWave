import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
import pandas as pd

# Activate pandas-to-R conversion
pandas2ri.activate()

# Import R's ggplot2 package
ggplot2 = importr('ggplot2')

# Run R code
ro.r('''
library(ggplot2)
data(mtcars)
plot <- ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
ggsave(filename="plot.png", plot=plot)
''')

# Load the plot into Python if needed
from PIL import Image
img = Image.open("plot.png")
img.show()
