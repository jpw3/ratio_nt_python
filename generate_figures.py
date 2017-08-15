#This code is designed to generate plots that can be used for presentation and manuscript creation for the ratio by nuber of targets experiment

#Designed to plot data from a persistent database
from pylab import *
from matplotlib import patches
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.lines as mlines
import shelve #for database writing and reading

#screen dimensions for the office ocmputer = (19.2,10.44)

datapath = '/Users/jameswilmott/Documents/MATLAB/data/ratio_nt_data/'; #'/Users/james/Documents/MATLAB/data/ratio_nt_data/'; #
shelvepath =  '/Users/jameswilmott/Documents/Python/ratio_nt/data/'; # '/Users/james/Documents/Python/ratio_nt/data/'; #  

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'ratio_nt_data');
individ_subject_data = shelve.open(shelvepath+'individ_ratio_nt_data');
db = subject_data; i_db = individ_subject_data; id = 'agg';

ids=['jpw'];


## Create the plots and save them ####
#Note, all plots are means of aggregate data
#set parameters for plots
matplotlib.rcParams['ytick.labelsize']=20; matplotlib.rcParams['xtick.labelsize']=20; #30;
matplotlib.rcParams['xtick.major.width']=2.0; matplotlib.rcParams['ytick.major.width']=2.0;
matplotlib.rcParams['xtick.major.size']=10.0; matplotlib.rcParams['ytick.major.size']=10.0; #increase the length of the ticks
matplotlib.rcParams['hatch.linewidth'] = 9.0; #set the hatch width to larger than the default case
matplotlib.rcParams['hatch.color'] = 'black';
matplotlib.pyplot.rc('font',weight='bold');


##########################################################################################################################################################
# Number of Stimuli Analyses
##########################################################################################################################################################
# RT
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(400,800); ax1.set_yticks(arange(450,801,50));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_rts = [db['1_targs_%s_dists_%s_nr_stim_mean_rt'%(d,(1+d))] for d in [2,3,5,10,14]];
st_x = 1 + array([2,3,5,10,14]);
mt_rts = [db['2_targs_%s_dists_%s_nr_stim_mean_rt'%(d,(2+d))] for d in [3,4,6,10,13]];
mt_x = 2 + array([3,4,6,10,14]);

#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
    ax1.plot(x, y, color = c, lw = 5.0);

#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# figure NT legend for reference
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
show();



# PC
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.0); ax1.set_yticks(arange(0.8, 1.01, 0.05));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_rts = [db['1_targs_%s_dists_%s_nr_stim_pc'%(d,(1+d))] for d in [2,3,5,10,14]];
st_x = 1 + array([2,3,5,10,14]);
mt_rts = [db['2_targs_%s_dists_%s_nr_stim_pc'%(d,(2+d))] for d in [3,4,6,10,13]];
mt_x = 2 + array([3,4,6,10,14]);

#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
    ax1.plot(x, y, color = c, lw = 5.0);

#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
show();



