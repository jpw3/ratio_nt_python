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

second_shelvepath = '/Users/jameswilmott/Documents/Python/et_mt/data/'; #	'/Users/james/Documents/Python/et_mt/data/'; #

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'ratio_nt_data');
individ_subject_data = shelve.open(shelvepath+'individ_ratio_nt_data');

id = 'agg'; #raw_input('Input I.D. [agg for all subjects, otherwise specify a single subject]:   ');

if id=='agg':
    db = subject_data;
    db2 = shelve.open(second_shelvepath+'mt_data.db');
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



### Plot the previous trial response repetition analyses here

# fig , ax1 = subplots(1,1,figsize = (12.8,7.64)); fig.suptitle('Experiment 2 (RATIO EXPERIMENT) previous trial type analysis, response repetition, subject %s'%id, size = 22);
# colors = ['dodgerblue',(75/255.0,0/255.0,130/255.0),(186/255.0,85/255.0,212/255.0)];
# ax1.set_ylim(550,900); ax1.set_yticks(arange(600,901,50)); ax1.set_xlim([0.5,3.5]); ax1.set_xticks([1.0, 2.0, 3.0]);
# ax1.set_ylabel('Response time',size=18); #ax1.set_xlabel('Current Trial Type ',size=18);
# ax1.set_xticklabels(['One target','Same shapes','Different shapes']);
# #single target first
# ax1.plot(1.3, db['%s_%s_targs_mean_rt'%(id,1)], 'black', markersize = 12.0, marker = 'o', alpha = 1.0);
# ax1.errorbar(1.3,db['%s_%s_targs_mean_rt'%(id,1)],yerr=[[db['%s_%s_targs_rt_SEMs'%(id,1)]],[db['%s_%s_targs_rt_SEMs'%(id,1)]]],color='black',capsize = 12,lw=6.0);
# for type, c, ex in zip(['one_target','cong_percept_cong_resp','incong_percept_incong_resp'], colors, [0.7, 0.9, 1.1, 1.3]):
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'one_target',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'one_target',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'one_target',type,'congruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'one_target',type,'congruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'one_target',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'one_target',type,'incongruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'one_target',type,'congruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'one_target',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #next do the same shape trials
# ax1.plot(2.3,db['%s_2_targs_shapes_%s_mean_rt'%(id,'match')],color='black',markersize = 12.0, marker = 'o',); #,edgecolor='black'
# ax1.errorbar(2.3,db['%s_2_targs_shapes_%s_mean_rt'%(id,'match')],yerr = [[db['%s_2_targs_shapes_%s_rt_SEMs'%(id,'match')]],[db['%s_2_targs_shapes_%s_rt_SEMs'%(id,'match')]]],color='black',capsize = 12, lw=6.0);
# for type, c, ex in zip(['one_target','cong_percept_cong_resp','incong_percept_incong_resp'], colors, [1.7, 1.9, 2.1, 2.3]):  
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_percept_cong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_percept_cong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_percept_cong_resp',type,'congruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_percept_cong_resp',type,'congruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_percept_cong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'cong_percept_cong_resp',type,'incongruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_percept_cong_resp',type,'incongruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'cong_percept_cong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# #different shape trials
# ax1.plot(3.3,db['%s_2_targs_shapes_%s_mean_rt'%(id,'not_match')],color='black',markersize = 12.0, marker = 'o',); #,edgecolor='black'
# ax1.errorbar(3.3,db['%s_2_targs_shapes_%s_mean_rt'%(id,'not_match')],yerr = [[db['%s_2_targs_shapes_%s_rt_SEMs'%(id,'not_match')]],[db['%s_2_targs_shapes_%s_rt_SEMs'%(id,'not_match')]]],color='black',capsize = 12, lw=6.0);
# for type, c, ex in zip(['one_target','cong_percept_cong_resp','incong_percept_incong_resp'], colors, [2.7, 2.9, 3.1, 3.3]):  
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_percept_incong_resp',type,'congruent')],color = c, markersize = 12.0, marker = 'o', alpha = 1.0);
#     ax1.plot(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_percept_incong_resp',type,'incongruent')],color = c, markersize = 12.0, marker = 'o', alpha = 0.3);
#     if id=='agg':
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_percept_incong_resp',type,'congruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_percept_incong_resp',type,'congruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_percept_incong_resp',type,'congruent')]]],color=c,lw=6.0,capsize = 12, alpha = 1.0);
#         ax1.errorbar(ex, db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_mean_rt'%(id,'incong_percept_incong_resp',type,'incongruent')], yerr = [[db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_percept_incong_resp',type,'incongruent')]],
#             [db['%s_Discrim_%s_%s_prev_trialtype_%s_actualresponse_rt_bs_sems'%(id,'incong_percept_incong_resp',type,'incongruent')]]],color=c,lw=6.0,capsize = 12, alpha = 0.3);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='One target'); ssline=mlines.Line2D([],[],color=(75/255.0,0/255.0,130/255.0),lw=6,label='Same shapes');
# ddline=mlines.Line2D([],[],color=(186/255.0,85/255.0,212/255.0),lw=6,label='Different shapes'); allline=mlines.Line2D([],[],color='black',lw=6,label='Trial type average');
# ax1.legend(handles=[oneline,ssline,ddline,allline],loc = 2, ncol=2, fontsize = 18);
# show();
# 
# 1/0

# ##########################################################################################################################################################
# # Number of Stimuli Analyses
# ##########################################################################################################################################################



#first plot all of the data points together
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,850); ax1.set_yticks(arange(650,851,50));    #ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim(4,16); ax1.set_xticks(2+array([3,4,6,10,13]));   #ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
#labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
#ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Set Size', size=18);
#first off get both number of targets search functions together
#st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
#st_x = 1+array([2,3,5,10,14]);
mt_x = 2+array([3,4,6,10,13]);
#get the target shapes match and nonmatch data together
nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
#get errorbars together for all of the data as well
#st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
#plot everything together
colors=['indigo','orchid'];  #'steelblue',
for x,y,yerrors,c,alph in zip([ mt_x, mt_x],[match_rts, nomatch_rts], [match_bsems, nomatch_bsems], colors, [1,1]): #st_x,    st_rts,  st_bsems,  ,1]
    ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 0, alpha = alph);
    for i,yerr in enumerate(yerrors):
        ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# figure NT legend for reference
oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); #twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,alpha = 0.4,label='Two Targets');
matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
ax1.legend(handles=[oneline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
#save the labeled figure as a .png	
filename = 'ratio_nt_allratios_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
#labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; #labels[5]=''; labels[6]='';
ax1.set_xticklabels(labels);
ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
ax1.legend([]);
filename = 'ratio_TSM_allratios_rt';
savefig(savepath+filename+'.eps',dpi=400);
# show();


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # RT
# #plot various aggregations of the data, all with ratio on the x-axis
# 
# #first plot all of the data points together
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(600,800); ax1.set_yticks(arange(650,801,50));    #ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
# ax1.set_xticklabels(labels,size = 12);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# #first off get both number of targets search functions together
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
# mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# mt_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# #get the target shapes match and nonmatch data together
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #get errorbars together for all of the data as well
# st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #plot everything together
# colors=['steelblue','mediumpurple','indigo','orchid']; 
# for x,y,yerrors,c,alph in zip([st_x, mt_x, mt_x, mt_x],[st_rts, mt_rts, match_rts, nomatch_rts], [st_bsems, mt_bsems, match_bsems, nomatch_bsems], colors, [1,0.5,1,1]):
#     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0, alpha = alph);
#     for i,yerr in enumerate(yerrors):
#         ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
# #assign some configurations to the plots
# title('Reaction Time by Number of Stimuli', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,alpha = 0.4,label='Two Targets');
# matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
# ax1.legend(handles=[oneline,twoline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_allratios_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
# ax1.legend([]);
# filename = 'ratio_nt_allratios_rt';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
# 

#then plot the data with only the common ratios together
fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
ax1.set_ylim(600,850); ax1.set_yticks(arange(650,851,50));    #ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
ax1.set_xticklabels(labels,size = 12);
ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
#first off get both number of targets search functions together
x = array([1.0/2,1.0/3,1.0/5]); #they all have the same x for the common ratio stuff
st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5]];
mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [4,6,10]];
#nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
#match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
#get errorbars together for all of the data as well
st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [4,6,10]];
#nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
#match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
#plot everything together
colors=['steelblue','mediumpurple']; #,'indigo','orchid']; 
for y,yerrors,c,alph in zip([st_rts, mt_rts], [st_bsems, mt_bsems], colors, [1,1]): #, match_bsems, nomatch_bsems    , match_rts, nomatch_rts ,1,1
    ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 0, alpha = alph);
    for i,yerr in enumerate(yerrors):
        ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
#assign some configurations to the plots
title('Reaction Time by Number of Stimuli', fontsize = 22);
ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# figure NT legend for reference
oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6, alpha = 0.4,label='Two Targets');
matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
ax1.legend(handles=[oneline,twoline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
#save the labeled figure as a .png	
filename = 'ratio_nt_commonratios_rt_labeled';
savefig(savepath+filename+'.png',dpi=400);
#then get rid of labels and save as a .eps
title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; 
ax1.set_xticklabels(labels);
ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
ax1.legend([]);
filename = 'ratio_nt_commonratios_rt';
savefig(savepath+filename+'.eps',dpi=400);
show();


1/0


# 
# 
# #finally only plot single target with target shapes match and notmatch pulled out from each other 
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(600,850); ax1.set_yticks(arange(650,851,50));    #ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
# ax1.set_xticklabels(labels,size = 12);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# #first off get both number of targets search functions together
# x = array([1.0/2,1.0/3,1.0/5]); #they all have the same x for the common ratio stuff
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5]];
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #get errorbars together for all of the data as well
# st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
# nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #plot everything together
# colors=['steelblue','indigo','orchid']; 
# for y,yerrors,c,alph in zip([st_rts, match_rts, nomatch_rts], [st_bsems, match_bsems, nomatch_bsems], colors, [1,1,1]):
#     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 0.0, alpha = alph);
#     for i,yerr in enumerate(yerrors):
#         ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
# #assign some configurations to the plots
# title('Reaction Time by Number of Stimuli', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); 
# matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
# ax1.legend(handles=[oneline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_tsm_commonratios_rt_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
# ax1.legend([]);
# filename = 'ratio_nt_tsm_commonratios_rt';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
# # 
# ############## Accurcy ###########
# #now do the same as above for accuracy
# 
# #first plot all of the data points together
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05)); 
# ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
# ax1.set_xticklabels(labels,size = 12);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# #first off get both number of targets search functions together
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
# mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# mt_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# #get the target shapes match and nonmatch data together
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #get errorbars together for all of the data as well
# st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #plot everything together
# colors=['steelblue','mediumpurple','indigo','orchid']; 
# for x,y,yerrors,c,alph in zip([st_x, mt_x, mt_x, mt_x],[st_rts, mt_rts, match_rts, nomatch_rts], [st_bsems, mt_bsems, match_bsems, nomatch_bsems], colors, [1,0.5,1,1]):
#     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0, alpha = alph);
#     for i,yerr in enumerate(yerrors):
#         ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
# #assign some configurations to the plots
# title('Reaction Time by Number of Stimuli', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,alpha = 0.4,label='Two Targets');
# matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
# ax1.legend(handles=[oneline,twoline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_allratios_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
# ax1.legend([]);
# filename = 'ratio_nt_allratios_pc';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
# 
# #then plot the data with only the common ratios together
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05)); 
# ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
# ax1.set_xticklabels(labels,size = 12);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# #first off get both number of targets search functions together
# x = array([1.0/2,1.0/3,1.0/5]); #they all have the same x for the common ratio stuff
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5]];
# mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [4,6,10]];
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #get errorbars together for all of the data as well
# st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
# mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [4,6,10]];
# nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #plot everything together
# colors=['steelblue','mediumpurple','indigo','orchid']; 
# for y,yerrors,c,alph in zip([st_rts, mt_rts, match_rts, nomatch_rts], [st_bsems, mt_bsems, match_bsems, nomatch_bsems], colors, [1,0.5,1,1]):
#     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0, alpha = alph);
#     for i,yerr in enumerate(yerrors):
#         ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
# #assign some configurations to the plots
# title('Reaction Time by Number of Stimuli', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6, alpha = 0.4,label='Two Targets');
# matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
# ax1.legend(handles=[oneline,twoline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_commonratios_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
# ax1.legend([]);
# filename = 'ratio_nt_commonratios_pc';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
# 
# 
# #finally only plot single target with target shapes match and notmatch pulled out from each other 
# fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05));
# ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
# ax1.set_xticklabels(labels,size = 12);
# ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# #first off get both number of targets search functions together
# x = array([1.0/2,1.0/3,1.0/5]); #they all have the same x for the common ratio stuff
# st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5]];
# nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #get errorbars together for all of the data as well
# st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
# nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #plot everything together
# colors=['steelblue','indigo','orchid']; 
# for y,yerrors,c,alph in zip([st_rts, match_rts, nomatch_rts], [st_bsems, match_bsems, nomatch_bsems], colors, [1,1,1]):
#     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0, alpha = alph);
#     for i,yerr in enumerate(yerrors):
#         ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, alpha = alph, capsize=10, fmt='none');  #plot errorbars if more than 1 subject 
# #assign some configurations to the plots
# title('Reaction Time by Number of Stimuli', fontsize = 22);
# ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # figure NT legend for reference
# oneline=mlines.Line2D([],[],color='steelblue',lw=6,label='One Target'); 
# matchline=mlines.Line2D([],[],color='indigo',lw=6,label='Shapes Match'); mismatchline=mlines.Line2D([],[],color='orchid',lw=6,label='Shapes Mismatch');
# ax1.legend(handles=[oneline, matchline, mismatchline],loc = 'best',ncol=2,fontsize = 14);
# #save the labeled figure as a .png	
# filename = 'ratio_nt_tsm_commonratios_pc_labeled';
# savefig(savepath+filename+'.png',dpi=400);
# #then get rid of labels and save as a .eps
# title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; 
# ax1.set_xticklabels(labels);
# ax1.set_yticklabels(['','','','']); #'','','','','','','','','',''
# ax1.legend([]);
# filename = 'ratio_nt_tsm_commonratios_pc';
# savefig(savepath+filename+'.eps',dpi=400);
# show();
# 
# 
# # ## Plot with nr stim on x axis
# # 
# # # RT
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = 1 + array([2,3,5,10,14]);
# # mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# # mt_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['limegreen','mediumpurple'];
# # for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
# #     ax1.plot(x, y, marker='o', markersize=18, color = c, lw = 5.0);
# # #plot errorbars if more than 1 subject
# # if id=='agg':
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
# #     for x,y,yerrors,c in zip([st_x, mt_x],[st_rts, mt_rts],[st_bsems, mt_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# # #assign some configurations to the plots
# # title('Reaction Time by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # # figure NT legend for reference
# # oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_nrstimXnrdist_nrstim_rt_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_nrstimXnrdist_nrstim_rt';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# # 
# # 
# # 
# # # PC
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.01, 0.05));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = 1 + array([2,3,5,10,14]);
# # mt_pcs = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# # mt_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['limegreen','mediumpurple'];
# # for x,y,c in zip([st_x, mt_x],[st_pcs, mt_pcs], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
# #     for x,y,yerrors,c in zip([st_x, mt_x],[st_pcs, mt_pcs],[st_bsems, mt_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# # #assign some configurations to the plots
# # title('Accuracy by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_nrstimXnrdist_nrstim_pc_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_nrstimXnrdist_nrstim_pc';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# 
# # ## Plot with nr distractors on x axis
# # 
# # # RT
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# # ax1.set_xlim([1, 15]);  ax1.set_xticks([2,3,4,5,6,7,8,9,10,11,12,13,14]);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = array([2,3,5,10,14]);
# # mt_rts = [db['%s_2_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# # mt_x = array([3,4,6,10,13]);
# # #plot them
# # colors=['limegreen','mediumpurple'];
# # for x,y,c in zip([st_x, mt_x],[st_rts, mt_rts], colors):
# #     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# # if id=='agg':
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
# #     for x,y,yerrors,c in zip([st_x, mt_x],[st_rts, mt_rts],[st_bsems, mt_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Number of Distractors', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # # figure NT legend for reference
# # oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_nrstimXnrdist_nrdist_rt_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_nrstimXnrdist_nrdist_rt';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# # 
# # 
# # # PC
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([1, 15]);  ax1.set_xticks([2,3,4,5,6,7,8,9,10,11,12,13,14]);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# # #first off get both number of targets search functions together
# # st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = array([2,3,5,10,14]);
# # mt_pcs = [db['%s_2_targs_%s_dists_%s_nr_stim_pc'%(id,d,(2+d))] for d in [3,4,6,10,13]];
# # mt_x = array([3,4,6,10,13]);
# # #plot them
# # colors=['limegreen','mediumpurple'];
# # for x,y,c in zip([st_x, mt_x],[st_pcs, mt_pcs], colors):
# #     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# # if id=='agg':
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     mt_bsems = [db['%s_2_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(2+d))] for d in [3,4,6,10,13]]
# #     for x,y,yerrors,c in zip([st_x, mt_x],[st_pcs, mt_pcs],[st_bsems, mt_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Number of Distractors', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target'); twoline=mlines.Line2D([],[],color='mediumpurple',lw=6,label='Two Targets');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_nrstimXnrdist_nrdist_pc_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_nrstimXnrdist_nrdist_pc';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# 
# ##########################################################################################################################################################
# # HF relation Analyses
# ##########################################################################################################################################################
# 
# # ## Plot with nr stim on x axis
# # 
# # #RT
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # same_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# # same_x = 2 + array([3,4,6,10,13]);
# # diff_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# # diff_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['dodgerblue','darkorange'];
# # for x,y,c in zip([same_x, diff_x],[same_rts, diff_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# #     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# #     for x,y,yerrors,c in zip([same_x, diff_x],[same_rts, diff_rts],[same_bsems, diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_hfXnrdist_nrstim_rt_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_hfXnrdist_nrstim_rt';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # 
# # # PC
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # same_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# # same_x = 2 + array([3,4,6,10,13]);
# # diff_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# # diff_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['dodgerblue','darkorange'];
# # for x,y,c in zip([same_x, diff_x],[same_pcs, diff_pcs], colors):
# #     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# # if id=='agg':
# #     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# #     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# #     for x,y,yerrors,c in zip([same_x, diff_x],[same_pcs, diff_pcs],[same_bsems, diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_hfXnrdist_nrstim_pc_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]='';
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_hfXnrdist_nrstim_pc';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# # ## Plot with nr distractors on x axis
# # 
# # # RT
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# # #first off get both number of targets search functions together
# # same_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# # same_x = array([3,4,6,10,13]);
# # diff_rts = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# # diff_x = array([3,4,6,10,13]);
# # #plot them
# # colors=['dodgerblue','darkorange'];
# # for x,y,c in zip([same_x, diff_x],[same_rts, diff_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# #     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# #     for x,y,yerrors,c in zip([same_x, diff_x],[same_rts, diff_rts],[same_bsems, diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# # #assign some configurations to the plots
# # title('Reaction Time by Number of Distractors', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_hfXnrdist_nrdist_rt_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_hfXnrdist_nrdist_rt';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # 
# # # PC
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# # #first off get both number of targets search functions together
# # same_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# # same_x = array([3,4,6,10,13]);
# # diff_pcs = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# # diff_x = array([3,4,6,10,13]);
# # #plot them
# # colors=['limegreen','mediumpurple'];
# # colors=['dodgerblue','darkorange'];
# # for x,y,c in zip([same_x, diff_x],[same_pcs, diff_pcs], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     same_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'s',d,(2+d))] for d in [3,4,6,10,13]];
# #     diff_bsems = [db['%s_2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(id,'d',d,(2+d))] for d in [3,4,6,10,13]];
# #     for x,y,yerrors,c in zip([same_x, diff_x],[same_pcs, diff_pcs],[same_bsems, diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Number of Distractors', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',lw=6,label='Same Hemifield'); twoline=mlines.Line2D([],[],color='darkorange',lw=6,label='Different Hemifields');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_hfXnrdist_nrdist_pc_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_hfXnrdist_nrdist_pc';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# 
# ##########################################################################################################################################################
# # Target Shapes Match Analyses
# ##########################################################################################################################################################
# 
# # ## Plot with nr stim on x axis
# # 
# # # RT
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = 1 + array([2,3,5,10,14]);
# # nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_x = 2 + array([3,4,6,10,13]);
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['lightsteelblue','dimgrey','limegreen'];
# # for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# # # #save the labeled figure as a .png	
# # # filename = 'ratio_nt_tsmXnrdist_nrstim_rt_labeled';
# # # savefig(savepath+filename+'.png',dpi=400);
# # # #then get rid of labels and save as a .eps
# # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # ax1.set_xticklabels(labels);
# # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # filename = 'ratio_nt_tsmXnrdist_nrstim_rt';
# # # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# # ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
# # nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # #plot them
# # colors=['lightsteelblue','dimgrey','limegreen'];
# # for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_shapesmatchonetargets_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.legend([]);
# # filename = 'ratio_nt_shapesmatchonetargets_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# # 
# # 
# # #with single target line, only the common ratios
# # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(650,800); ax1.set_yticks(arange(700,801,50));
# # ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5';
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5]];
# # st_x = array([1.0/2,1.0/3,1.0/5]);
# # nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# # nomatch_x = array([1.0/2,1.0/3,1.0/5]);
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
# # match_x = array([1.0/2,1.0/3,1.0/5]);
# # #plot them
# # colors=['lightsteelblue','dimgrey','limegreen'];
# # for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
# #     for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_rts, match_rts, st_rts],[nomatch_bsems, match_bsems, st_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_COMMONRATIOS_shapesmatchonetargets_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; #labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.legend([]);
# # filename = 'ratio_nt_COMMONRATIOS_shapesmatchonetargets_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# # 
# # 
# # #single target and target shapes match only
# # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(650,800); ax1.set_yticks(arange(700,801,50));
# # ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5';
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # st_rts = [db['%s_1_targs_%s_dists_%s_nr_stim_mean_rt'%(id,d,(1+d))] for d in [2,3,5]];
# # st_x = array([1.0/2,1.0/3,1.0/5]);
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
# # match_x = array([1.0/2,1.0/3,1.0/5]);
# # #plot them
# # colors=['dimgrey','limegreen'];
# # for x,y,c in zip([ match_x, st_x],[match_rts, st_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_rt_SEMs'%(id,d,(1+d))] for d in [2,3,5]];
# #     for x,y,yerrors,c in zip([ match_x, st_x],[match_rts, st_rts],[match_bsems, st_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_COMMONRATIOS_standtargetshapesmatch_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; #labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.legend([]);
# # filename = 'ratio_nt_COMMONRATIOS_standtargetshapesmatch_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# 
# 
# # # 
# # # ## without sinlge target line
# # # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(650,800); ax1.set_yticks(arange(700,801,50));
# # ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# # nomatch_x = array([1.0/2,1.0/3,1.0/5]);
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
# # match_x = array([1.0/2,1.0/3,1.0/5]);
# # #plot them
# # colors=['lightsteelblue','dimgrey'];
# # for x,y,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [4,6,10]];
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #     for x,y,yerrors,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts],[nomatch_bsems, match_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_shapesmatchonly_rt_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]='';  
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.legend([]);
# # filename = 'ratio_nt_shapesmatchonly_rt';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# # 
# # #target shapes match only
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(650,800); ax1.set_yticks(arange(700,801,50));
# # ax1.set_xlim([0.6, 0.1]);  ax1.set_xticks([1.0/2,1.0/3,1.0/5]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='1/2'; labels[1]='1/3'; labels[2]='1/5'; 
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [4,6,10]];
# # match_x = array([1.0/2,1.0/3,1.0/5]);
# # #plot them
# # colors=['dimgrey'];
# # for x,y,c in zip([match_x], [match_rts], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [4,6,10]];
# #     for x,y,yerrors,c in zip([match_x],[match_rts],[match_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # #oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match');
# # twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # ax1.legend(handles=[twoline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_shapesmatchonly_MATCH_only_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]='';  
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # ax1.legend([]);
# # filename = 'ratio_nt_shapesmatchonly_MATCH_only';
# # savefig(savepath+filename+'.eps',dpi=400);
# # show();
# 
# 
# # #PC
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13,1.0/10,1.0/14]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; labels[5]='1/10'; labels[6]='1/14';
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Accuracy',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # st_x = array([1.0/2,1.0/3,1.0/5,1.0/10,1.0/14]);
# # st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # colors=['lightsteelblue','dimgrey','limegreen'];
# # for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# #     for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs],[nomatch_bsems, match_bsems, st_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# 
# 
# 
# 
# 
# 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Total Stimuli', size=18);
# # #first off get both number of targets search functions together
# # st_x = 1 + array([2,3,5,10,14]);
# # st_pcs = [db['%s_1_targs_%s_dists_%s_nr_stim_pc'%(id,d,(1+d))] for d in [2,3,5,10,14]];
# # nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_x = 2 + array([3,4,6,10,13]);
# # match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_x = 2 + array([3,4,6,10,13]);
# # #plot them
# # colors=['lightsteelblue','dimgrey','limegreen'];
# # for x,y,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs], colors):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0);
# # if id=='agg':
# #     nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     st_bsems = [db['%s_1_targs_%s_dists_%s_nr_stim_pc_SEMs'%(id,d,(1+d))] for d in [2,3,5,10,14]];    
# #     for x,y,yerrors,c in zip([nomatch_x, match_x, st_x],[nomatch_pcs, match_pcs, st_pcs],[nomatch_bsems, match_bsems, st_bsems,],colors):
# #         for i,yerr in enumerate(yerrors):    
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Number of Stimuli', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # threeline=mlines.Line2D([],[],color='limegreen',lw=6,label='One Target');
# # ax1.legend(handles=[oneline,twoline, threeline],loc = 'best',ncol=2,fontsize = 14);
# # #save the labeled figure as a .png	
# # filename = 'ratio_nt_tsmXnrdist_nrstim_pc_labeled';
# # savefig(savepath+filename+'.png',dpi=400);
# # #then get rid of labels and save as a .eps
# # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # ax1.set_xticklabels(labels);
# # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # filename = 'ratio_nt_tsmXnrdist_nrstim_pc';
# # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # 
# # ## Plot with nr distractors on x axis
# # 
# # # # RT
# # # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # # ax1.set_ylim(400,1000); ax1.set_yticks(arange(450,1001,50));
# # # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Number of Total Distractors', size=18);
# # # #first off get both number of targets search functions together
# # # nomatch_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # # nomatch_x = array([3,4,6,10,13]);
# # # match_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # # match_x = array([3,4,6,10,13]);
# # # #plot them
# # # colors=['lightsteelblue','dimgrey'];
# # # for x,y,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts], colors):
# # #     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# # # if id=='agg':
# # #     nomatch_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # #     match_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # #     for x,y,yerrors,c in zip([nomatch_x, match_x],[nomatch_rts, match_rts],[nomatch_bsems, match_bsems],colors):
# # #         for i,yerr in enumerate(yerrors):
# # #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');   
# # # #assign some configurations to the plots
# # # title('Reaction Time by Number of Distractors', fontsize = 22);
# # # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # # #save the labeled figure as a .png	
# # # # filename = 'ratio_nt_tsmXnrdist_nrdist_rt_labeled';
# # # # savefig(savepath+filename+'.png',dpi=400);
# # # # #then get rid of labels and save as a .eps
# # # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # # ax1.set_xticklabels(labels);
# # # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # # filename = 'ratio_nt_tsmXnrdist_nrdist_rt';
# # # # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # # #PC
# # # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # # ax1.set_xlim([2, 16]);  ax1.set_xticks([3,4,5,6,7,8,9,10,11,12,13,14,15]);
# # # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Number of Distractors', size=18);
# # # #first off get both number of targets search functions together
# # # nomatch_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # # nomatch_x = array([3,4,6,10,13]);
# # # match_pcs = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # # match_x = array([3,4,6,10,13]);
# # # #plot them
# # # colors=['lightsteelblue','dimgrey'];
# # # for x,y,c in zip([nomatch_x, match_x],[nomatch_pcs, match_pcs], colors):
# # #     ax1.plot(x, y, marker='o', markersize=18,color = c, lw = 5.0);
# # # if id=='agg':
# # #     nomatch_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # #     match_bsems =  [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # #     for x,y,yerrrs,c in zip([nomatch_x, match_x],[nomatch_pcs, match_pcs],[nomatch_bsems, match_bsems],colors):
# # #         for i,yerr in enumerate(yerrors):    
# # #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none'); 
# # # #assign some configurations to the plots
# # # title('Accuracy by Number of Distractors', fontsize = 22);
# # # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # # oneline=mlines.Line2D([],[],color='lightsteelblue',lw=6,label='No Match'); twoline=mlines.Line2D([],[],color='dimgrey',lw=6,label='Yes Match');
# # # ax1.legend(handles=[oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # # # #save the labeled figure as a .png	
# # # # filename = 'ratio_nt_tsmXnrdist_nrdist_pc_labeled';
# # # # savefig(savepath+filename+'.png',dpi=400);
# # # # #then get rid of labels and save as a .eps
# # # # title(''); ax1.set_ylabel(''); ax1.set_xlabel('');
# # # # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]=''; labels[1]=''; labels[2]=''; labels[3]=''; labels[4]=''; labels[5]=''; labels[6]='';
# # # #labels[7]=''; labels[8]=''; labels[9]=''; labels[10]=''; labels[11]=''; labels[12]=''; 
# # # # ax1.set_xticklabels(labels);
# # # # ax1.set_yticklabels(['','','','','','','','','','','','','','']);
# # # # filename = 'ratio_nt_tsmXnrdist_nrdist_pc';
# # # # savefig(savepath+filename+'.eps',dpi=400);
# # 
# # ##########################################################################################################################################################
# # # Target Shapes Match By Hemifield Analyses
# # #########################################################################################################################################################
# # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50));
# # ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; 
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Milliseconds',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # nomatch_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_mean_rt'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_mean_rt'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # #plot them
# # colors=['dodgerblue','dodgerblue','darkorange','darkorange']; linestyles = ['solid','dashed','solid','dashed'];
# # for y,c,ls in zip([nomatch_same_rts, match_same_rts, nomatch_diff_rts, match_diff_rts], colors, linestyles):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0, ls = ls);
# # if id=='agg':
# #     nomatch_same_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_same_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     nomatch_diff_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_rt_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_diff_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_rt_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     for y,yerrors,c in zip([nomatch_same_rts, match_same_rts, nomatch_diff_rts, match_diff_rts],[nomatch_same_bsems, match_same_bsems, nomatch_diff_bsems, match_diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Reaction Time by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',ls='dashed',lw=6,label='Same HF Targets Match'); twoline=mlines.Line2D([],[],color='darkorange',ls='dashed',lw=6,label='Different HF Targets Match');
# # one1line=mlines.Line2D([],[],color='dodgerblue',ls='solid',lw=6,label='Same HF Dont Match'); two2line=mlines.Line2D([],[],color='darkorange',ls='solid',lw=6,label='Different HF Dont Match');
# # ax1.legend(handles=[one1line,two2line,oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# 
# ############
# # #comparison with experiment 2
# # 
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(600,900); ax1.set_yticks(arange(650,901,50)); ax1.set_xlim([0.5,2.8]);  ax1.set_xticks([1.2,2.2]);
# # ax1.set_ylabel('Response Time',size=18); ax1.set_xlabel('Hemispheric Location of Targets',size=18,labelpad=40);		
# # ax1.set_xticklabels(['Eyetracking Experiment','Ratio Experiment']);
# # width=0.2; add=0;
# # for h,targ_match in zip(['/',''],['no_match','match']):
# #     ex=1;
# #     for c,hf_match in zip(['dodgerblue','darkorange'],['same','diff']):	
# #         ax1.bar(ex+add,db2['%s_Discrim_%s_hf_%s_mean_rt'%(id,hf_match,targ_match)],color=c,hatch=h,width=width); #,edgecolor='black'
# #         ax1.errorbar(ex+add,db2['%s_Discrim_%s_hf_%s_mean_rt'%(id,hf_match,targ_match)],yerr=[[db2['%s_Discrim_%s_%s_rt_bs_sems'%(id,hf_match,targ_match)]],[db2['%s_Discrim_%s_%s_rt_bs_sems'%(id,hf_match,targ_match)]]],color='black',lw=6.0);
# #         ex+=0.2;
# #     if hf_match=='diff':
# #         add+=0.4;
# # 
# # width=0.2; add=1;
# # for h,targ_match in zip(['/',''],['not_match','match']):
# #     ex=1;
# #     for c,hf_match in zip(['dodgerblue','darkorange'],['same','diff']):	
# #         ax1.bar(ex+add,db['%s_2_targs_shapes_%s_4_dists_6_nr_stim_%s_hf_mean_rt'%(id,targ_match,hf_match)],color=c,hatch=h,width=width); #,edgecolor='black'
# #         ax1.errorbar(ex+add,db['%s_2_targs_shapes_%s_4_dists_6_nr_stim_%s_hf_mean_rt'%(id,targ_match,hf_match)],yerr=[[db['%s_2_targs_shapes_%s_4_dists_6_nr_stim_%s_hf_rt_SEMs'%(id,targ_match,hf_match)]],[db['%s_2_targs_shapes_%s_4_dists_6_nr_stim_%s_hf_rt_SEMs'%(id,targ_match,hf_match)]]],color='black',lw=6.0);
# #         ex+=0.2;
# #     if hf_match=='diff':
# #         add+=0.4;
# # 
# # title('Experiment Comparison', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # 
# # oneline=mlines.Line2D([],[],color='dodgerblue',ls='solid',lw=6,label='Same HF Targets Match'); twoline=mlines.Line2D([],[],color='darkorange',ls='solid',lw=6,label='Different HF Targets Match');
# # one1line=mlines.Line2D([],[],color='dodgerblue',ls = 'dashed',lw=6,label='Same HF Dont Match'); two2line=mlines.Line2D([],[],color='darkorange',ls = 'dashed',lw=6,label='Different HF Dont Match');
# # ax1.legend(handles=[one1line,two2line,oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# 
# #############
# # #pc
# # fig = figure(figsize = (12.8,7.64)); ax1=gca(); #grid(True);
# # ax1.set_ylim(0.75, 1.01); ax1.set_yticks(arange(0.8, 1.001, 0.05));
# # ax1.set_xlim([0.75, 0]);  ax1.set_xticks([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # labels = [item.get_text() for item in ax1.get_xticklabels()]; labels[0]='2/3'; labels[1]='1/2'; labels[2]='1/3'; labels[3]='1/5'; labels[4]='2/13'; 
# # ax1.set_xticklabels(labels,size = 12);
# # ax1.set_ylabel('Proportion Correct',size=18); ax1.set_xlabel('Ratio of Targets:Distractors', size=18);
# # #first off get both number of targets search functions together
# # x = array([2.0/3,1.0/2,1.0/3,1.0/5,2.0/13]);
# # nomatch_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_same_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # nomatch_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_pc'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# # match_diff_rts = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_pc'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# # #plot them
# # colors=['dodgerblue','dodgerblue','darkorange','darkorange']; linestyles = ['solid','dashed','solid','dashed'];
# # for y,c,ls in zip([nomatch_same_rts, match_same_rts, nomatch_diff_rts, match_diff_rts], colors, linestyles):
# #     ax1.plot(x, y,marker='o', markersize=18, color = c, lw = 5.0, ls = ls);
# # if id=='agg':
# #     nomatch_same_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_same_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_same_hf_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     nomatch_diff_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_pc_SEMs'%(id,'not_match',d,(2+d))] for d in [3,4,6,10,13]];
# #     match_diff_bsems = [db['%s_2_targs_shapes_%s_%s_dists_%s_nr_stim_diff_hf_pc_SEMs'%(id,'match',d,(2+d))] for d in [3,4,6,10,13]];
# #     for y,yerrors,c in zip([nomatch_same_rts, match_same_rts, nomatch_diff_rts, match_diff_rts],[nomatch_same_bsems, match_same_bsems, nomatch_diff_bsems, match_diff_bsems],colors):
# #         for i,yerr in enumerate(yerrors):
# #             ax1.errorbar(x[i], y[i], yerr=[[yerr],[yerr]], ecolor=c, lw = 4.0, capsize=10, fmt='none');  
# # #assign some configurations to the plots
# # title('Accuracy by Ratio', fontsize = 22);
# # ax1.spines['right'].set_visible(False); ax1.spines['top'].set_visible(False);
# # ax1.spines['bottom'].set_linewidth(2.0); ax1.spines['left'].set_linewidth(2.0);
# # ax1.yaxis.set_ticks_position('left'); ax1.xaxis.set_ticks_position('bottom');
# # oneline=mlines.Line2D([],[],color='dodgerblue',ls='dashed',lw=6,label='Same HF Targets Match'); twoline=mlines.Line2D([],[],color='darkorange',ls='dashed',lw=6,label='Different HF Targets Match');
# # one1line=mlines.Line2D([],[],color='dodgerblue',ls='solid',lw=6,label='Same HF Dont Match'); two2line=mlines.Line2D([],[],color='darkorange',ls='solid',lw=6,label='Different HF Dont Match');
# # ax1.legend(handles=[one1line,two2line,oneline,twoline],loc = 'best',ncol=2,fontsize = 14);
# # 
# 
# 
# 
# # here's multiple colors for the same line: http://matplotlib.org/examples/pylab_examples/multicolored_line.html
# 
