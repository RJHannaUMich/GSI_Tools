# GSI_Tools

These are the tools that I use for getting the Canvas page and Gradescope page up and running. 

## How to use the Gradescope Roster Fixer 

When the Gradescope course roster is synced with the Canvas page, you will notice that the students' section will read like physics-251-section-010 or biophys-251-section-010. This effectively duplicates the amount of sections. To merge the physics and biophysics sections, first download the roster from the roster tab in gradescope (there will be a button ribbon at the bottom of the screen that will look like the following). 

![image](https://github.com/user-attachments/assets/b3e5a203-d602-4088-99c0-7859f6603df6)

This will download the .csv file that you will modify with the gradescope-roster-fixer.py file. Running it will open a TK window where you will select the .csv file. Then, a window will prompt you to name and save the edited roster. You can name it anything. You will then need to upload it by selecting the add students or staff button in the lower right-hand corner of the roster tab. 

## How to use the Canvas Group Maker 

Because each Canvas course section is merged into one page, Canvas' auto group maker will put students from different sections into groups! To get around this, navigate to the People tab on Canvas, create a Group Set for the current lab, and download the course roster from the import groups button. Then, run canvas-groups.py, and a new .csv file will be created with the randomized groups of either 3 or 2. Finally, you will need to upload the groups by clicking on the import groups button. 

## How to use the Canvas Grading Updates
