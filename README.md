# CFD in OpenFOAM

This file serves to complement the .pdf, by providing additional information pertaining to how the directories and files are structured, as well as more comments about scripts. 

## Table of contents
1. [Files directories and sequences](#introduction)
2. [Bash scripts](#paragraph1)
    1. [masterRun](#subparagraph1)
    2. [run](#subparagraph2)
    3. [exportCSV](#subparagraph3)
3. [Python macro](#paragraph3)
4. [generatePlot.m](#paragraph4)



 ## 1 Files, directories and sequences <a name="introduction"></a>
The project contains 12 cases, there are 3 turbulence models used and for each of them, 4 different mesh configurations. This was mentioned in the .pdf file. Each directory contains 4 cases, and contains the turbulence model used in its name (kEps translates to $k-\varepsilon$ turbulence model, kOme into $k-\omega$ SST, and so on). Example of what the directories contain and how they are set up,  is shown below. 

> **Note:** In this case we are observing the directory for the $k-\varepsilon$ (**kEps**) turbulence model.

```
kEps
└───────kEps_config(1..4)
│   	│  	0
│   	│ 	constant
│   	│ 	system
│   	│ 	run.sh
│   	│
│   extractCSV.sh
│   generatePlot_1095kEps.m
│   masterRun.sh
│   
```
It is important to note the chronological order of scrpits. After creating all of the scripts, the general order is as follows:
1. masterRun.sh
    1. run.sh (run automatically by masterRun.sh)
2. Python macro (or alternatively manually export .csv files)
3. exportCSV.sh
4. generatePlot.m 

After these scripts have finished, the user will have at his disposal quality plots from the desired locations in the geometry, of the desired quantities. In the project case, these plots were used to compare the numerically obtained velocity profiles in the domain with the velocity profiles from the referenced paper. 

## 2 Bash scripts <a name="paragraph1"></a>

### 2.1. masterRun <a name="subparagraph1"></a>
This script is responsible for locating the run.sh script and executing it. It only starts the next run.sh script when the previous one has ended. We are sticking to the **kEps** directory throughout the examples, as can be seen below. The loop contains the folders in which the run.sh can be found.
```bash
#!/bin/bash
for i in kEps_config1 kEps_config2 kEps_config3 kEps_config4; do
	(
	cd $i;
	sh run.sh;
	cd ..;
	)
done	
```
The script can be executed by running the following commands in the CLI:
```console
user@PC:~$ sh masterRun.sh
```
### 2.2. run <a name="subparagraph2"></a>
The run.sh script used for the purpose of this project is an upgraded
```bash
#!/bin/bash
foamListTimes -rm		# Delete any previously simulated time steps
blockMesh | tee log.blockMesh 	# Output a mesh log
checkMesh | tee log.checkMesh	# Output a checkMesh log
pyFoamPlotRunner.py --with-courant pisoFoam	# Display residuals during the simulation 
pyFoamRedoPlot.py --pickle-file Gnuplotting.analyzed/pickledPlots --picture-prefix=kEps1095_ 	# Export the residual plots as png with the specified prefix 
postProcess -func CourantNo	# Plot the Courant number as well 
foamToVTK		        # Convert the standard data to VTK format
killall gnuplot_x11		# Close all of the residual monitors before commencing the next simulation
```

### 2.3. exportCSV <a name="subparagraph3"></a>
The following script relies on the .csv data exported from ParaView. This can be done manually, or with the help of a Python macro. Either way, this script is utilized so to avoid manual sorting of data from the .csv files.  Firstly, the script will in this case, take the 2nd column of exported .csv files, ignore the 1st row and export the data to a new .ods file. This will be done for each of the mesh configurations and each of the 4 locations in the backward-facing step (referenced from the paper). For each of the mesh configurations, there will be a total of 4 velocity profiles. The final .ods file will contain all of the 16 velocity profiles, thanks to the paste command. The last line of code will delete all of the .ods files except for the one containing all of the velocities, in order prevent over-crowding. 

> **Note:** After the final .ods file is created, it is mandatory to open it with spreadsheet software and save it again as .ods or .xlsx format. This is one bug that I haven't found a workaround. 

```bash
#!/bin/bash
for i in {1..4}; do	# Loop for each of the mesh configurations
    (	
    cd kEps_config$i;	# Change the working directory
    for j in 019 023 029 055; do	# Locations of the velocity profile sampling
        (
        awk -F',' -v OFS=, 'NR>1 {print $2}'# Ignore the 1st row and print only the 2nd column
        kEps_config${i}_${j}.csv >>../forOctave_kEps1095_${i}_${j}.ods; # Export the .csv file data to .ods file format
        )
    done
    )
done
paste *.ods >> forOctave_kEps1095.ods	# Concatenate all of the .ods files into one file
sleep 2 && find . -maxdepth 1 -type f -name '*.ods' ! -name 'forOctave_kEps1095.ods' -exec rm {} + # Keep only the final file (delete the rest after 2 sec)
```
The script can be executed by running the following commands in the CLI:
```console
user@PC:~$ source exportCSV.sh
```

## 3 Python macro <a name="paragraph3"></a>

One of the easier ways of extracting the .csv files from ParaView is to record a trace with the desired commands. I highly suggest anyone who hasn't used a trace in ParaView to take a look at Asmaa Hadane's video found in this [link](https://www.youtube.com/watch?v=h6Y7HZR_SAI).

I left one example script which can be found in the **kEps** case. Although in order for it to be applicable to the user, lots of directory names have to be adjusted. It is best for the user to create their own macro, or manually export the .csv files. 

## 4 generatePlot.m <a name="paragraph4"></a>
The Octave script takes the .ods file provided by the Python macro and the exportCSV.sh, and extracts the desired columns for plotting. The code should be pretty much self-explanatory, only thing to note is that the format in which the plot is exported is adjusted for $\LaTeX$. This can easily be changed by setting the print command output different format.  The script also features some dynamic programming, to take advantage of the for loops. 
```matlab
clear, close all, clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Script outputs mesh independence graphs of desired quantities %%
%% Written in:              Octave 6.4.0                         %%
%%%%%%%%%%%%%%%%%%%%%%  Author: Matej Tomić  %%%%%%%%%%%%%%%%%%%%%%


%% Load all packages, plotting settings, etc.
pkg load io;                                        % Loads the necessary package
graphics_toolkit("gnuplot");                        % Choose the graphics toolkit


%% Load all the variables from the csv file format
all = xlsread("forOctave_kEps1095.ods");            % Creates a matrix of desired quantities
                                                    % a bit slow for .ods file format

                                                    
%% Introduce necessary quantities 
[m n] = size(all);                                  % Dimensions of the global matrix
dt = linspace(0,0.5,m);                             % [s] Time step used in the simulation
all = [all dt'];                                    % Concatenate global matrix with the time step vector
mesh = [12000 17280 25056 37332];                   % Define a vector containing total mesh count
[p q] = size(mesh);                                 % Take its size for furhter manipulation
ux1_ave = zeros(1,q);                               % Preallocate vectors of average values of variables %
ux2_ave = zeros(1,q);                               %                                                    %
ux3_ave = zeros(1,q);                               %                                                    %
ux4_ave = zeros(1,q);                               %                                                    %
H = linspace(0,10.4,1001);                          % Total height of the geometry

%% Extract u of different locations and for various mesh configurations
for i = 1:4
  column_ux1 = all(:, (i-1)*4 + 1);                 % Extracts every 4th column, beginning from the 1st
  eval(sprintf("ux1%d = column_ux1", i));           % Assigns the variable according to the counter value i
  column_ux2 = all(:, (i-1)*4 + 2);                 % Extracts every 4th column, beginning from the 2nd
  eval(sprintf("ux2%d = column_ux2", i));           
  column_ux3 = all(:, (i-1)*4 + 3);                 % Extracts every 4th column, beginning from the 3nd
  eval(sprintf("ux3%d = column_ux3", i));
  column_ux4 = all(:, (i-1)*4 + 4);
  eval(sprintf("ux4%d = column_ux4", i));           % Extracts every 4th column, beginning from the 4nd
end


%% Let the plotting begin
% Plot the velocity profile u @ x1
figure(1)
for i = 1:4
  ux1_var = sprintf('ux1%d', i);
  plot(eval(ux1_var),H/2+5.2);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  xlabel('$u$ [m/s]');
  ylim([0 12]);
  hold on;
  legend("boxoff");
  legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$");
end
print -depsc ux1_1095.eps;
print -depslatex ux1_1095.tex;

% Plot the velocity profile u @ x2
figure(2)
for i = 1:4
  ux2_var = sprintf('ux2%d', i);
  plot(eval(ux2_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  xlabel('$u$ [m/s]');
  hold on;
  legend("boxoff");
  legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$");
end
print -depsc ux2_1095.eps;
print -depslatex ux2_1095.tex;

% Plot the velocity profile u @ x3
figure(3)
for i = 1:4
  ux3_var = sprintf('ux3%d', i);
  plot(eval(ux3_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  xlabel('$u$ [m/s]');
  hold on;
  legend("boxoff");
  legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$");
end
print -depsc ux3_1095.eps;
print -depslatex ux3_1095.tex;

% Plot the velocity profile u @ x2
figure(4)
for i = 1:4
  ux4_var = sprintf('ux4%d', i);
  plot(eval(ux4_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  xlabel('$u$ [m/s]');
  hold on;
  legend("boxoff");
  legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$");
end
print -depsc ux4_1095.eps;
print -depslatex ux4_1095.tex;

% Plot the average velocity - ux1_ave vs mesh size
figure(5)
for i = 1:4
  ux1_ave(1,i) = mean(eval(sprintf('ux1%d', i)));
  plot(mesh,ux1_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
end
print -depsc ux1_ave1095.eps;
print -depslatex ux1_ave1095.tex;

% Plot the average velocity - ux2_ave vs mesh size
figure(6)
for i = 1:4
  ux2_ave(1,i) = mean(eval(sprintf('ux2%d', i)));
  plot(mesh,ux2_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
end
print -depsc ux2_ave1095.eps;
print -depslatex ux2_ave1095.tex;

% Plot the average velocity - ux3_ave vs mesh size
figure(7)
for i = 1:4
  ux3_ave(1,i) = mean(eval(sprintf('ux3%d', i)));
  plot(mesh,ux3_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
end
print -depsc ux3_ave1095.eps;
print -depslatex ux3_ave1095.tex;

% Plot the average velocity - ux4_ave vs mesh size
figure(8)
for i = 1:4
  ux4_ave(1,i) = mean(eval(sprintf('ux4%d', i)));
  plot(mesh,ux4_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
end
print -depsc ux4_ave1095.eps;
print -depslatex ux4_ave1095.tex;
```
This script can be called from the CLI as well.

```console
user@PC:~$ octave --persist generatePlot.m
```
