clear, close all, clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Script outputs mesh independence graphs of desired quantities %%
%% Written in:              Octave 6.4.0                         %%
%%%%%%%%%%%%%%%%%%%%%%  Author: Matej Tomić  %%%%%%%%%%%%%%%%%%%%%%


%% Load all packages, plotting settings, etc.
pkg load io;                                        % Loads the necessary package
graphics_toolkit("gnuplot");                        % Choose the graphics toolkit

%% Load all the variables from the csv file format
all = xlsread('forOctave_Smagorinsky1095.ods');     % Creates a matrix of desired quantities
                                                    % a bit slow for .ods file format
ux1_paper = xlsread('ux1_rad.ods');
ux2_paper = xlsread('ux2_rad.ods');
ux3_paper = xlsread('ux3_rad.ods');
ux4_paper = xlsread('ux4_rad.ods');


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

%% Extract u, eps, k, and p from different mesh configurations
for i = 1:4
  column_ux1 = all(:, (i-1)*4 + 1);
  eval(sprintf("ux1%d = column_ux1", i));
  column_ux2 = all(:, (i-1)*4 + 2);
  eval(sprintf("ux2%d = column_ux2", i));
  column_ux3 = all(:, (i-1)*4 + 3);
  eval(sprintf("ux3%d = column_ux3", i));
  column_ux4 = all(:, (i-1)*4 + 4);
  eval(sprintf("ux4%d = column_ux4", i));
end


%% Let the plotting begin
% Plot the velocity profile u @ x1
figure(1)
figure("visible","off")
for i = 1:4
  ux1_var = sprintf('ux1%d', i);
  plot(eval(ux1_var),H/2+5.2);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  xlabel('$u$ [m/s]');
  ylim([0 11]);
  hold on;
end
hold all;
plot(ux1_paper(:,1), ux1_paper(:,2),'o r');
legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$","$u_{r}");
legend boxoff;
print -depsc ux1_SmSm1095.eps;
print -depslatex ux1_SmSm1095.tex;

% Plot the velocity profile u @ x2
figure(2)
figure("visible","off")
for i = 1:4
  ux2_var = sprintf('ux2%d', i);
  plot(eval(ux2_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  ylim([0 11]);
  xlabel('$u$ [m/s]');
  hold on;
end
hold all;
plot(ux2_paper(:,1), ux2_paper(:,2),'o r');
legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$","$u_{r}");
legend boxoff;
print -depsc ux2_Sm1095.eps;
print -depslatex ux2_Sm1095.tex;

% Plot the velocity profile u @ x3
figure(3)
figure("visible","off")
for i = 1:4
  ux3_var = sprintf('ux3%d', i);
  plot(eval(ux3_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  ylim([0 11]);
  xlabel('$u$ [m/s]');
  hold on;
end
hold all;
plot(ux3_paper(:,1), ux3_paper(:,2),'o r');
legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$","$u_{r}");
legend boxoff;
print -depsc ux3_Sm1095.eps;
print -depslatex ux3_Sm1095.tex;

% Plot the velocity profile u @ x2
figure(4)
figure("visible","off")
for i = 1:4
  ux4_var = sprintf('ux4%d', i);
  plot(eval(ux4_var),H);
  set(gca,'XAxisLocation','top','YAxisLocation','left');
  ylabel('$y$ [mm]');
  ylim([0 11]);
  xlabel('$u$ [m/s]');
  hold on;
end
hold all;
plot(ux4_paper(:,1), ux4_paper(:,2),'o r');
legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$","$u_{r}");
legend boxoff;
print -depsc ux4_Sm1095.eps;
print -depslatex ux4_Sm1095.tex;

% Plot the average velocity - ux1_ave vs mesh size
figure(5)
figure("visible","off")
for i = 1:4
  ux1_ave(1,i) = mean(eval(sprintf('ux1%d', i)));
  plot(mesh,ux1_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
  ylim([0 10]);
end
print -depsc ux1_aveSm1095.eps;
print -depslatex ux1_aveSm1095.tex;

% Plot the average velocity - ux2_ave vs mesh size
figure(6)
figure("visible","off")
for i = 1:4
  ux2_ave(1,i) = mean(eval(sprintf('ux2%d', i)));
  plot(mesh,ux2_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
  ylim([0 10]);
end
print -depsc ux2_aveSm1095.eps;
print -depslatex ux2_aveSm1095.tex;

% Plot the average velocity - ux3_ave vs mesh size
figure(7)
figure("visible","off")
for i = 1:4
  ux3_ave(1,i) = mean(eval(sprintf('ux3%d', i)));
  plot(mesh,ux3_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
  ylim([0 10]);
end
print -depsc ux3_aveSm1095.eps;
print -depslatex ux3_aveSm1095.tex;

% Plot the average velocity - ux4_ave vs mesh size
figure(8)
figure("visible","off")
for i = 1:4
  ux4_ave(1,i) = mean(eval(sprintf('ux4%d', i)));
  plot(mesh,ux4_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
  ylim([0 10]);
end
print -depsc ux4_aveSm1095.eps;
print -depslatex ux4_aveSm1095.tex;
