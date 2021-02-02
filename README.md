How to run:

============== SETUP ==============

=== REGULAR SETUP ===

1. install python: <br/>
  macos - https://www.youtube.com/watch?v=sajO8JHn7DU<br/>
  windows - https://www.youtube.com/watch?v=IDo_Gsv3KVk
  
2. create and activate virtual environment:     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         <-- (Do this in step 6)<br/>
  macos - https://www.youtube.com/watch?v=Kg1Yvry_Ydk<br/>
  windows - https://www.youtube.com/watch?v=APOPm01BVrk
  
=== RECOMMENDED SETUP ===

1. install python with Miniconda:<br/>
  macos - https://www.youtube.com/watch?v=bbIG5d3bOmk<br/>
  windows - https://www.youtube.com/watch?v=tXgPY4lc6fo
 
 2. create conda environment<br/>
    https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
   
    [terminal/cmd]:<br/>
   % **conda create --name myenv**<br/>
    **proceed ([y]/n)? % Y**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                 <-- (enter y)<br/>
    
    
======================================

3. create github account<br/>
4. install git<br/>
  macos - https://www.youtube.com/watch?v=y2xkghn2X00&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <-- (Homebrew recommended! Install with: https://www.youtube.com/watch?v=31eTw5xRHBA) <br/>
  windows - https://www.youtube.com/watch?v=nbFwejIsHlY
  
5. Create/open a folder and open a terminal window inside the folder (right click folder and look for option to do so)<br/>
6. Enter the following commands in the terminal/cmd:

  % **git clone https://github.com/ordovezazek/PSE_SP_DB.git**<br/>
  % **cd PSE_SP_DB**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                            <-- (make sure to be inside this folder directory)<br/>
  % **conda activate myenv**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                                      <-- (only for recommended setup)<br/>
                                                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(**do step 2 of regular setup now**)<br/>
%  **pip install -r requirements.txt**
  
7. Open the parent folder in the code editor of your choice

============== RUN ================

8. Enter the following commands in the terminal/cmd:

  % **python3 priceCollect.py**
  
    
