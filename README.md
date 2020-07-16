# CNC-Mining-tool-classification
CNC mining tool classification using streamlit

#### Organization of the code repository
1. Data folder contains all the experiment files and the train.csv file
2. **filename.pickle** has the models stored as a pickle dictionary for Result section in the GUI/Interface.
3. **print_utils.py** contains all the textual material that has been written on the website. 
4. **utils.py** contains all the helper functions that are required for the **data_analysis.py** file.
5. **data_analysis.py** file has the main code for the application. 

###### data_analysis.py 
    [x] main_app() is the main function of the application, where we have four sections described by `st.sidebar.radio`

#### If you want to run on local machine 
1. install streamlit
2. git clone repository
3. change directory to the repository
4. execute command: streamlit run data_analysis.py

#### To run on web
go to **cnctool.herokuapp.com**