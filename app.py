import streamlit as st
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from PIL import Image

pandas2ri.activate()
ggplot2 = importr('ggplot2')
st.title("R Plot with ggplot2")

# Create a button to generate the plot
if st.button('Generate Plot'):
    ro.r('''
    library(ggplot2)
    data(mtcars)
    plot <- ggplot(mtcars, aes(x=wt, y=mpg)) + geom_point()
    ggsave(filename="plot.png", plot=plot)''')
    
    img = Image.open("plot.png")
    st.image(img, caption='Scatter plot of mtcars dataset', use_column_width=True)
