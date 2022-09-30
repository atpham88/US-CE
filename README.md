# ASSET Lab macro power system capacity expansion model
Key contributors: Michael Craig & An Pham at the University of Michigan.
The capacity expansion (or planning model) is formulated in GAMS (gams.com). The rest of the code, which processes inputs and outputs and runs the GAMS model, is written in Python. 
The model runs with Python version 3.7 or more recent. Several Python packages are required in addition to the anaconda distribution - see https://docs.google.com/document/d/1KPp2_wskzxDN-fcjcDMen4qCwcCDc1mkLoAPXx5-90c/edit.
Several data sets are too large to upload to Github. Those datasets are available here: https://drive.google.com/drive/folders/1F9WyWkhWUlKuXDy-2ryh_eYZhwxeZBCf?usp=sharing. 
To run the model, you will need to update directory pointers in the function createGAMSWorkspaceAndDatabase(). The flag indicates whether you are running locally or on a supercomputer.
For a model description, see "Cost and Deployment Consequences of Advanced Planning for Negative Emissions U.S. Power Systems" (in review at One Earth). 
For instructions on running the model on UM's Great Lakes, see https://docs.google.com/document/d/1KPp2_wskzxDN-fcjcDMen4qCwcCDc1mkLoAPXx5-90c/edit.

