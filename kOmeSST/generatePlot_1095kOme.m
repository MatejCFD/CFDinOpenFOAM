clear, close all, clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Script outputs mesh independence graphs of desired quantities %%
%% Written in:              Octave 6.4.0                         %%
%%%%%%%%%%%%%%%%%%%%%%  Author: Matej Tomić  %%%%%%%%%%%%%%%%%%%%%%


%% Load all packages, plotting settings, etc.
pkg load io;                                        % Loads the necessary package
graphics_toolkit("gnuplot");                        % Choose the graphics toolkit

%% Load all the variables from the csv file format
all = xlsread('forOctave_kOme1095.ods');            % Creates a matrix of desired quantities
                                                    % a bit slow for .ods file format

                                                    
%% Introduce necessary quantities 
[m n] = size(all);                                  % Dimensions of the global matrix
dt = linspace(0,0.5,n);                             % [s] Time step used in the simulation
all = [all dt'];                                    % Concatenate global matrix with the time step vector
mesh = [12000 17280 25056 37332];                   % Define a vector containing total mesh count
[p q] = size(mesh);                                 % Take its size for furhter manipulation
u_ave = zeros(1,q);                                 % Preallocate vectors of average values of variables %
p_ave = zeros(1,q);                                 %                                                    %
k_ave = zeros(1,q);                                 %                                                    %
ome_ave = zeros(1,q);                               %                                                    %


%% Extract u, ome, k, and p from different mesh configurations
for i = 1:4
  column_u = all(:, (i-1)*4 + 1);
  eval(sprintf("u%d = column_u", i));
  column_ome = all(:, (i-1)*4 + 2);
  eval(sprintf("ome%d = column_ome", i));
  column_k = all(:, (i-1)*4 + 3);
  eval(sprintf("k%d = column_k", i));
  column_p = all(:, (i-1)*4 + 4);
  eval(sprintf("p%d = column_p", i));
end


%% Let the plotting begin
% Plot the evolution of streamwise velocity u
figure(1)
figure("visible","off")
for i = 1:4
  u_var = sprintf('u%d', i);
  plot(dt,eval(u_var));
  xlabel('$t$ [s]');
  xlim([0 max(dt)]);
  ylabel('$u$ [m/s]');
  hold on;
  legend("boxoff");
  legend("$u_{1}$","$u_{2}$","$u_{3}$","$u_{4}$");
end
print -depsc u1095.eps;
print -depslatex u1095.tex;

% Plot the evolution of kinematic pressure
figure(2)
figure("visible","off")
for i = 1:4
  p_var = sprintf('p%d', i);
  plot(dt,eval(p_var));
  xlabel('$t$ [s]');
  xlim([0 max(dt)]);
  ylabel('$p_{k}$ [m^{2}/s^{2}]');
  hold on;
  legend("boxoff");
  legend("$p_{k1}$","$p_{k2}$","$p_{k3}$","$p_{k4}$","location","southeast");
end
print -depsc p1095.eps
print -depslatex p1095.tex;

% Plot the evolution of specific TKE dissipation rate - omega
figure(3)
figure("visible","off")
for i = 1:4
  eps_var = sprintf('ome%d', i);
  plot(dt,eval(eps_var));
  xlabel('$t$ [s]');
  xlim([0 max(dt)]);
  ylabel('$\omega$ [1/s]');
  hold on;
  legend("boxoff");
  legend("$\\omega_{1}$","$\\omega_{2}$","$\\omega_{3}$","$\\omega_{4}$");
end
print -depsc ome1095.eps
print -depslatex ome1095.tex;

% Plot the evolution of TKE - k
figure(4)
figure("visible","off")
for i = 1:4
  k_var = sprintf('k%d', i);
  plot(dt,eval(k_var));
  xlabel('$t$ [s]');
  xlim([0 max(dt)]);
  ylabel('$k$ [m^{2}/s^{2}]');
  hold on;
  legend("boxoff"); 
  legend("$k_{1}$","$k_{2}$","$k_{3}$","$k_{4}$");
end
print -depsc k1095.eps
print -depslatex k1095.tex;

% Plot the average velocity - u_ave vs mesh size
figure(5)
figure("visible","off")
for i = 1:4
  u_ave(1,i) = mean(eval(sprintf('u%d', i)));
  plot(mesh,u_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{u}$ [m/s]');
  ylim([0 10]);
end
print -depsc u_ave1095.eps;
print -depslatex u_ave1095.tex;

% Plot the average kinematic pressure - p_ave vs mesh size
figure(6)
figure("visible","off")
for i = 1:4
  p_ave(1,i) = mean(eval(sprintf('p%d', i)));
  plot(mesh,p_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{p}_{k}$ [m^{2}/s^{2}]');
  ylim([-30 0]);
end
print -depsc p_ave1095.eps;
print -depslatex p_ave1095.tex;

% Plot the average TKE - k_ave vs mesh size
figure(7)
figure("visible","off")
for i = 1:4
  k_ave(1,i) = mean(eval(sprintf('k%d', i)));
  plot(mesh,k_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{k}$ [m^{2}/s^{2}]');
  ylim([0 5]);
end
print -depsc k_ave1095.eps;
print -depslatex k_ave1095.tex;

% Plot the average specific TKE dissipation rate - omega_ave vs mesh size
figure(8)
figure("visible","off")
for i = 1:4
  ome_ave(1,i) = mean(eval(sprintf('ome%d', i)));
  plot(mesh,eps_ave,'o-r');
  xlabel('Mesh count [-]');
  xlim([min(mesh) max(mesh)]);
  ylabel('$\bar{\omega}$ [1/s]');
  ylim([0 1000]);
end
print -depsc ome_ave1095.eps;
print -depslatex ome_ave1095.tex;
