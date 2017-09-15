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
savepath = '/Users/jameswilmott/Documents/Python/ratio_nt/figures/'; # '/Users/james/Documents/Python/ratio_nt/figures/'; #

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'ratio_nt_data');
individ_subject_data = shelve.open(shelvepath+'individ_ratio_nt_data');

ids=['1']; #'jpw'

id = raw_input('Input I.D. [agg for all subjects, otherwise specify a single subject]:   ');

if id=='agg':
    db = subject_data;
else:
    db = individ_subject_data; 

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

## plot ratios on X axis
# RT
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
#first off get both number of targets search functions together
st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
mt_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
    ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0);
#plot errorbars if more than 1 subject
if id=='agg':
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
    for x,y,yerrors,c in zip([st_x, mt_x],[st_rts, mt_rts],[st_bsems, mt_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# figure NT legend for reference
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_nrstimXnrdist_nrstim_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_nrstimXnrdist_nrstim_rt';
# savefig(savepath+filename+'.eps',dpi=400);
show();



# PC
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05));
ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
#first off get both number of targets search functions together
st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
mt_pcs = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
mt_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_pcs, mt_pcs], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
    for x,y,yerrors,c in zip([st_x, mt_x],[st_pcs, mt_pcs],[st_bsems, mt_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_nrstimXnrdist_nrstim_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_nrstimXnrdist_nrstim_pc';
# savefig(savepath+filename+'.eps',dpi=400);
show();

## Plot with nr stim on x axis

# RT
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = 1 + array([2,3,5,10,14]);
mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
mt_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
    ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0);
#plot errorbars if more than 1 subject
if id=='agg':
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
    for x,y,yerrors,c in zip([st_x, mt_x],[st_rts, mt_rts],[st_bsems, mt_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# figure NT legend for reference
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_nrstimXnrdist_nrstim_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_nrstimXnrdist_nrstim_rt';
# savefig(savepath+filename+'.eps',dpi=400);
show();



# PC
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = 1 + array([2,3,5,10,14]);
mt_pcs = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
mt_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['limegreen','mediumpurple'];
for x,y,c in zip([st_x, mt_x],[st_pcs, mt_pcs], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
    for x,y,yerrors,c in zip([st_x, mt_x],[st_pcs, mt_pcs],[st_bsems, mt_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_nrstimXnrdist_nrstim_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_nrstimXnrdist_nrstim_pc';
# savefig(savepath+filename+'.eps',dpi=400);
show();


# ## Plot with nr distractors on x axis
# 
# # RT
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# ax1.set_xlim([1, 15]);  ax1.set_xticks([2,3,4,5,6,7,8,9,10,11,12,13,14]);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# #first off get both number of targets search functions together
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# st_x = array([2,3,5,10,14]);
# mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# mt_x = array([3,4,6,10,13]);
# #plot them
# colors=['limegreen','mediumpurple'];
# for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
#     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# if id=='agg':
#     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
#     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
#     for x,y,yerrors,c in zip([st_x, mt_x],[st_rts, mt_rts],[st_bsems, mt_bsems],colors):
#         for i,yerr in enumerate(yerrors):
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# #assign some configurations to the plots
# title('Reaction Time by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_nrstimXnrdist_nrdist_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_nrstimXnrdist_nrdist_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# show();
# 
# 
# # PC
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# ax1.set_xlim([1, 15]);  ax1.set_xticks([2,3,4,5,6,7,8,9,10,11,12,13,14]);
# ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# #first off get both number of targets search functions together
# st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# st_x = array([2,3,5,10,14]);
# mt_pcs = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# mt_x = array([3,4,6,10,13]);
# #plot them
# colors=['limegreen','mediumpurple'];
# for x,y,c in zip([st_x, mt_x],[st_pcs, mt_pcs], colors):
#     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# if id=='agg':
#     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
#     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
#     for x,y,yerrors,c in zip([st_x, mt_x],[st_pcs, mt_pcs],[st_bsems, mt_bsems],colors):
#         for i,yerr in enumerate(yerrors):
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# #assign some configurations to the plots
# title('Accuracy by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_nrstimXnrdist_nrdist_pc_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_nrstimXnrdist_nrdist_pc';
# # savefig(savepath+filename+'.eps',dpi=400);
# show();


##########################################################################################################################################################
# HF relation Analyses
##########################################################################################################################################################

## Plot with nr stim on x axis

# RT
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
same_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
same_x = 2 + array([3,4,6,10,13]);
diff_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
diff_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['dodgerblue','darkorange'];
for x,y,c in zip([same_x, diff_x],[same_rts, diff_rts], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
    diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
    for x,y,yerrors,c in zip([same_x, diff_x],[same_rts, diff_rts],[same_bsems, diff_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_hfXnrdist_nrstim_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_hfXnrdist_nrstim_rt';
# savefig(savepath+filename+'.eps',dpi=400);


# PC
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
same_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
same_x = 2 + array([3,4,6,10,13]);
diff_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
diff_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['dodgerblue','darkorange'];
for x,y,c in zip([same_x, diff_x],[same_pcs, diff_pcs], colors):
    ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
if id=='agg':
    same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
    diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
    for x,y,yerrors,c in zip([same_x, diff_x],[same_pcs, diff_pcs],[same_bsems, diff_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_hfXnrdist_nrstim_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_hfXnrdist_nrstim_pc';
# savefig(savepath+filename+'.eps',dpi=400);
show();

# ## Plot with nr distractors on x axis
# 
# # RT
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# #first off get both number of targets search functions together
# same_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# same_x = array([3,4,6,10,13]);
# diff_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# diff_x = array([3,4,6,10,13]);
# #plot them
# colors=['dodgerblue','darkorange'];
# for x,y,c in zip([same_x, diff_x],[same_rts, diff_rts], colors):
#     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# if id=='agg':
#     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
#     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
#     for x,y,yerrors,c in zip([same_x, diff_x],[same_rts, diff_rts],[same_bsems, diff_bsems],colors):
#         for i,yerr in enumerate(yerrors):
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# #assign some configurations to the plots
# title('Reaction Time by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_hfXnrdist_nrdist_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_hfXnrdist_nrdist_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# 
# 
# # PC
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# #first off get both number of targets search functions together
# same_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# same_x = array([3,4,6,10,13]);
# diff_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# diff_x = array([3,4,6,10,13]);
# #plot them
# colors=['limegreen','mediumpurple'];
# colors=['dodgerblue','darkorange'];
# for x,y,c in zip([same_x, diff_x],[same_pcs, diff_pcs], colors):
#     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# if id=='agg':
#     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
#     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
#     for x,y,yerrors,c in zip([same_x, diff_x],[same_pcs, diff_pcs],[same_bsems, diff_bsems],colors):
#         for i,yerr in enumerate(yerrors):
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# #assign some configurations to the plots
# title('Accuracy by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_hfXnrdist_nrdist_pc_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_hfXnrdist_nrdist_pc';
# # savefig(savepath+filename+'.eps',dpi=400);
# show();


##########################################################################################################################################################
# Target Shapes Match Analyses
##########################################################################################################################################################

## Plot with nr stim on x axis

# RT
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = 1 + array([2,3,5,10,14]);
nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
nomatch_x = 2 + array([3,4,6,10,13]);
match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
match_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['lightsteelblue','dimgrey','limegreen'];
for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
    match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_tsmXnrdist_nrstim_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_tsmXnrdist_nrstim_rt';
# savefig(savepath+filename+'.eps',dpi=400);


fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
#first off get both number of targets search functions together
st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
nomatch_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
match_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
#plot them
colors=['lightsteelblue','dimgrey','limegreen'];
for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
    match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Reaction Time by Ratio', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);

#PC
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Accuracy',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
nomatch_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
match_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
colors=['lightsteelblue','dimgrey','limegreen'];
for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
    match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs],[nomatch_bsems, match_bsems, st_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);


fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
#first off get both number of targets search functions together
st_x = 1 + array([2,3,5,10,14]);
st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
nomatch_x = 2 + array([3,4,6,10,13]);
match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
match_x = 2 + array([3,4,6,10,13]);
#plot them
colors=['lightsteelblue','dimgrey','limegreen'];
for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
    match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];    
    for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs],[nomatch_bsems, match_bsems, st_bsems,],colors):
        for i,yerr in enumerate(yerrors):    
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Accuracy by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_tsmXnrdist_nrstim_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# filename = 'ratio_nt_tsmXnrdist_nrstim_pc';
# savefig(savepath+filename+'.eps',dpi=400);


## Plot with nr distractors on x axis

# # RT
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Distractors', size=18);
# #first off get both number of targets search functions together
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# nomatch_x = array([3,4,6,10,13]);
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# match_x = array([3,4,6,10,13]);
# #plot them
# colors=['lightsteelblue','dimgrey'];
# for x,y,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts], colors):
#     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# if id=='agg':
#     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
#     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
#     for x,y,yerrors,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts],[nomatch_bsems, match_bsems],colors):
#         for i,yerr in enumerate(yerrors):
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# #assign some configurations to the plots
# title('Reaction Time by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_tsmXnrdist_nrdist_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_tsmXnrdist_nrdist_rt';
# # savefig(savepath+filename+'.eps',dpi=400);

# #PC
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# #first off get both number of targets search functions together
# nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# nomatch_x = array([3,4,6,10,13]);
# match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# match_x = array([3,4,6,10,13]);
# #plot them
# colors=['lightsteelblue','dimgrey'];
# for x,y,c in zip([nomatch_x, match_x],[nomatch_pcs, match_pcs], colors):
#     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# if id=='agg':
#     nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
#     match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
#     for x,y,yerrrs,c in zip([nomatch_x, match_x],[nomatch_pcs, match_pcs],[nomatch_bsems, match_bsems],colors):
#         for i,yerr in enumerate(yerrors):    
#             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none'); 
# #assign some configurations to the plots
# title('Accuracy by Number of Distractors', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_tsmXnrdist_nrdist_pc_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_tsmXnrdist_nrdist_pc';
# # savefig(savepath+filename+'.eps',dpi=400);

##########################################################################################################################################################
# Target Shapes Match By Hemifield Analyses
#########################################################################################################################################################

fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; 
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
#first off get both number of targets search functions together
x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
nomatch_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
match_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
nomatch_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
match_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
#plot them
colors=['lightsteelblue','dimgrey','limegreen'];

#from here below I need to figure out the color/linestyle scheme I want to use for the plotting here. DO I want to do two toned, or do I want to do two colors with two linestyles?
# here's multiple colors for the same line: http://matplotlib.org/examples/pylab_examples/multicolored_line.html


for y,c in zip([nomatch_rts, match_rts, st_rts], colors):
    ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
if id=='agg':
    nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
    match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
    st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
    for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
        for i,yerr in enumerate(yerrors):
            ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
#assign some configurations to the plots
title('Reaction Time by Ratio', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);

