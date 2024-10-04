# BlockWave
This project demonstrates the integration of R with Python to create visualizations using the ggplot2 package. It generates a scatter plot of the `mtcars` dataset.

## Features
- Integrates R's ggplot2 library for data visualization.
- Generates and saves a scatter plot comparing weight (wt) and miles per gallon (mpg) from the mtcars dataset.
- Displays the generated plot using Python.

## Usage
### All required libraries can be installed using a single-line command:
```bash
pip install -r requirements.txt
```

### While to run the code:
#### Console-based version:
```bash
python main.py
```

#### Streamlit-based version:
```bash
streamlit run app.py
```

## Description about various files:
- **app.py:** Contains a Streamlit-based version of the main code.
- **main.py:** Main script for R and Python integration to create visualizations.
- **requirements.txt:** File containing all required Python modules.
