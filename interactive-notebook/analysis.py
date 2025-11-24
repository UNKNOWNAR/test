import marimo

__generated_with = "0.1.0"
app = marimo.App()

@app.cell
def __(mo):
    mo.md(
        """
        # Interactive Data Analysis
        
        **Author Email:** 24f3001857@ds.study.iitm.ac.in
        
        This notebook demonstrates reactive data flow using Marimo.
        """
    )
    return

@app.cell
def __():
    import marimo as mo
    return mo,

@app.cell
def __(mo):
    # Create an interactive slider widget
    # This widget controls the input variable 'x' for our analysis
    slider = mo.ui.slider(start=1, end=100, value=50, label="Select Input Value (x)")
    return slider,

@app.cell
def __(mo, slider):
    # This cell depends on 'slider'
    # It updates automatically whenever the slider value changes
    x = slider.value
    
    # Calculate a derived value (y = x^2)
    y = x ** 2
    
    # Display the result dynamically
    mo.md(
        f"""
        ### Reactive Output
        
        You selected **x = {x}**.
        
        The calculated value **y (x²)** is: **{y}**
        
        Visualization:
        {'🟦' * (x // 5)} ({x})
        """
    )
    return x, y

@app.cell
def __(mo, slider):
    # Display the slider widget itself
    mo.md(f"Adjust the parameter: {slider}")
    return

if __name__ == "__main__":
    app.run()
