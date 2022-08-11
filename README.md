# NYC Home Prices/Inflation 
A link to the main repository: 
## NYC Home Valuator:
+ (Compare home price increase to increase of inflation)
In this application we developed a tool for used to select a NYC neighborhood, average the neighborhood’s YOY change in prices and compare that to inflation. 
We also identify if the area is overvalued, undervalued, or fairly valued based on the average YOY neighborhood price changes adjusted for inflation. 
## Purpose
The purpose of this tool is to be used to assist NYC home buyers in their pursuit of best prices relative to inflation increases. The developer used basic Python code with a dropdown for user selection and comparison charts and a valuation notice to assist users in their NYC home search. 
## Setup 
+ Run the application
+ Select the neighborhood of interest 
+ Press Display Result 
Optionally fork this [remote depository]( https://github.com/drc9472/freestyle-project), to create a copy under your own control. Then “clone” or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop or C Drive (example below). Then navigate to wherever you downloaded the repo. 
```sh
cd ~/Documents/GitHub/freestyle-project
```
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file. 

Create a virtual environment:
```sh
conda create -n freestyle-env python=3.8
```
Activate the virtual environment:
```sh
conda activate freestyle-env
```
Install package dependencies (mainly for testing):
```sh
pip install -r requirements.txt
```
## Testing
Run tests:
```sh
pytest
```
# Environmental Setup
Check for Anaconda installation in the command-line to ensure Anaconda has been installed:
```sh
conda --version
```
If an error message populates, please install:
[Anaconda](https://www.anaconda.com/products/distribution) to successfully play a game of rock, paper, scissors. 
## Usage
After the setup is complete, please demonstrate your ability to run the Python script from the command-line.
## NYC Home Valuator Application
Navigate to APP folder
```sh
~/Documents/GitHub/freestyle-project/APP
```
Run the application
```sh
python dashboard.py
```
You will be prompted to make a selection of (from a dropdown of neighborhoods). If you run into any pull errors, you will be prompted with an "Not Enough Data" message. In this case, please re-run the below and select a different neighborhood (as there was not multiple years of data to show a year-over-year price change):
```sh 
python dashboard.py
```
Select the appropriate neighborhood option to successfully use the application to help in your research for your next NYC residence!
This is a one-time use application. To use the application multiple times please re-run the below (or press the up arrow if already played) and follow the steps listed above:
```sh
python dashboard.py
##HAPPY HOUSE HUNTING!

