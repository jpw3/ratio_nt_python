#Data anlaysis code for ratio number of targets search experiment
#Author: James Wilmott, Summer 2017

#Designed to import et_hemifield_data and analyze it

from pylab import *
import shelve #for database writing and reading
from scipy.io import loadmat #used to load .mat files in as dictionaries
from scipy import stats
from glob import glob #for use in searching for/ finding data files
import random #general purpose
from collections import namedtuple
import pyvttbl as pt
pc = lambda x:sum(x)/float(len(x)); #create a percent correct lambda function

datapath = '/Users/jameswilmott/Documents/MATLAB/data/ratio_nt_data/'; #'/Users/james/Documents/MATLAB/data/ratio_nt_data/'; #
shelvepath =  '/Users/jameswilmott/Documents/Python/ratio_nt/data/'; # '/Users/james/Documents/Python/ratio_nt/data/'; #  

#import the persistent database to save data analysis for future use (plotting)
subject_data = shelve.open(shelvepath+'ratio_nt_data');
individ_subject_data = shelve.open(shelvepath+'individ_ratio_nt_data');

ids=['jpw'];

# 1 targets: nr dists was 2,3,5,10,14
# 2 targets: 3, 4, 6, 10, 13

# Data Analysis Methods #########################################################################################################

def getStats(id='agg',ids = ids):
	#cut_out argument refers to whether I want to cut the subjects I choose to from the analysis
	if (id=='agg'):
		blocks = getAllSubjectBlocks(ids);
		trials = getTrials(blocks);
	else:
		blocks = loadAllBlocks(id);
		trials = getTrials([blocks]);
	#run the analyses	
	print 'Starting the suite of analyses...';
	computeNrStim(trials, id);
	computeHFRelation(trials, id);
	computeTargetShapesMatch(trials, id);
	#simple effects stuff
	computeSimpleEffectNrTargets(trial_matrix, id);
	computeSimpleEffectHFRelation(trials, id);
	print ; print 'Done! '; print ;

#must do a simple effects calculation of hemifield relation and whether shapes match and nr targets
#Can I do it for nr of dists? don't think so, as each level of number of targets is different
def computeSimpleEffectNrTargets(trial_matrix, id='agg'):
	if id=='agg':
		db=subject_data;
		#add in anova stuff later
	else:
		db=individ_subject_data;
	#go through all trials and look for whether it was 1 or 2 targets
	for nr_t in [1,2]:
		#collect the appropriate results and RTs for this condition
		all_res_matrix = [[tee.result for tee in ts if (tee.nr_targets==nr_t)] for ts in trial_matrix];
		all_rt_matrix = [[tee.response_time for tee in ts if ((tee.nr_targets==nr_t)&(tee.result==1))] for ts in trial_matrix];
		all_il_matrix = [[tee.initiation_latency for tee in ts if ((tee.nr_targets==nr_t)&(tee.result==1))] for ts in trial_matrix];
		all_mt_matrix = [[tee.movement_time for tee in ts if ((tee.nr_targets==nr_t)&(tee.result==1))] for ts in trial_matrix];
		res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not		
		# #get individual rt sds and il sds to 'shave' the rts of extreme outliers
		# ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
		# rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
		# il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
		# mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
		# rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
		#for now, dont' shave the RTs 
		rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
		mts = [ms for j in all_mt_matrix for ms in j];
		if len(rts)==0:
			continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
		#now find the relevant stats and set up the data into the database
		db['%s_targs_mean_rt'%(nr_t)] = mean(rts); db['%s_targs_median_rt'%(nr_t)] = median(rts); db['%s_targs_var_rt'%(nr_t)] = var(rts);
		db['%s_targs_mean_il'%(nr_t)] = mean(ils); db['%s_targs_median_il'%(nr_t)] = median(ils); db['%s_targs_var_il'%(nr_t)] = var(ils);
		db['%s_targs_mean_mt'%(nr_t)] = mean(mts); db['%s_targs_median_mt'%(nr_t)] = median(mts); db['%s_targs_var_mt'%(nr_t)] = var(mts);
		db['%s_targs_pc'%(nr_t)] = pc(res);
		if id=='agg':
			#calculate the SEMs
			db['%s_targs_rt_SEMs'%(nr_t)] = compute_BS_SEM(all_rt_matrix, 'time'); db['%s_targs_il_SEMs'%(nr_t)] = compute_BS_SEM(all_il_matrix, 'time');
			db['%s_targs_mt_SEMs'%(nr_t)] = compute_BS_SEM(all_mt_matrix, 'time'); db['%s_targs_pc_SEMs'%(nr_t)] = compute_BS_SEM(all_res_matrix, 'result');
			# do ANOVA stuff
			    
			db.sync();			
	print 'Completed simple effects analysis of number of targets';		
			
def computeSimpleEffectHFRelation(trial_matrix, id='agg'):
	if id=='agg':
		db=subject_data;
		#add in anova stuff later
	else:
		db=individ_subject_data;
	#go through all trials and look for whether it was 1 or 2 targets
	for hf,bool in zip(['s','d'],[1,0]):
		#collect the appropriate results and RTs for this condition
		all_res_matrix = [[tee.result for tee in ts if (tee.same_hf==bool)] for ts in trial_matrix];
		all_rt_matrix = [[tee.response_time for tee in ts if ((tee.same_hf==bool)&(tee.result==1))] for ts in trial_matrix];
		all_il_matrix = [[tee.initiation_latency for tee in ts if ((tee.same_hf==bool)&(tee.result==1))] for ts in trial_matrix];
		all_mt_matrix = [[tee.movement_time for tee in ts if ((tee.same_hf==bool)&(tee.result==1))] for ts in trial_matrix];
		res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not		
		# #get individual rt sds and il sds to 'shave' the rts of extreme outliers
		# ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
		# rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
		# il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
		# mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
		# rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
		#for now, dont' shave the RTs 
		rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
		mts = [ms for j in all_mt_matrix for ms in j];
		if len(rts)==0:
			continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
		#now find the relevant stats and set up the data into the database
		db['%s_hf_mean_rt'%(hf)] = mean(rts); db['%s_hf_median_rt'%(hf)] = median(rts); db['%s_hf_var_rt'%(hf)] = var(rts);
		db['%s_hf_mean_il'%(hf)] = mean(ils); db['%s_hf_median_il'%(hf)] = median(ils); db['%s_hf_var_il'%(hf)] = var(ils);
		db['%s_hf_mean_mt'%(hf)] = mean(mts); db['%s_hf_median_mt'%(hf)] = median(mts); db['%s_hf_var_mt'%(hf)] = var(mts);
		db['%s_hf_pc'%(hf)] = pc(res);
		if id=='agg':
			#calculate the SEMs
			db['%s_hf_rt_SEMs'%(hf)] = compute_BS_SEM(all_rt_matrix, 'time'); db['%s_hf_il_SEMs'%(hf)] = compute_BS_SEM(all_il_matrix, 'time');
			db['%s_hf_mt_SEMs'%(hf)] = compute_BS_SEM(all_mt_matrix, 'time'); db['%s_hf_pc_SEMs'%(hf)] = compute_BS_SEM(all_res_matrix, 'result');
			# do ANOVA stuff
			    
			db.sync();			
	print 'Completed simple effects analysis of number of targets';			

def computeSimpleEffectTargetsMatch(trial_matrix, id='agg'):
	if id=='agg':
		db=subject_data;
		#add in anova stuff later
	else:
		db=individ_subject_data;
	#go through all trials and look for whether it was 1 or 2 targets
	for tsm,bool in zip(['match','not_match'],[1,0]):
		#collect the appropriate results and RTs for this condition
		all_res_matrix = [[tee.result for tee in ts if ((tee.target_types[0]==tee.target_types[1])==bool)] for ts in trial_matrix];
		all_rt_matrix = [[tee.response_time for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.result==1))] for ts in trial_matrix];
		all_il_matrix = [[tee.initiation_latency for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.result==1))] for ts in trial_matrix];
		all_mt_matrix = [[tee.movement_time for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.result==1))] for ts in trial_matrix];
		res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not		
		# #get individual rt sds and il sds to 'shave' the rts of extreme outliers
		# ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
		# rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
		# il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
		# mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
		# rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
		#for now, dont' shave the RTs 
		rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
		mts = [ms for j in all_mt_matrix for ms in j];
		if len(rts)==0:
			continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
		#now find the relevant stats and set up the data into the database
		db['shapes_%s_mean_rt'%(tsm)] = mean(rts); db['shapes_%s_median_rt'%(tsm)] = median(rts); db['shapes_%s_var_rt'%(tsm)] = var(rts);
		db['shapes_%s_mean_il'%(tsm)] = mean(ils); db['shapes_%s_median_il'%(tsm)] = median(ils); db['shapes_%s_var_il'%(tsm)] = var(ils);
		db['shapes_%s_mean_mt'%(tsm)] = mean(mts); db['shapes_%s_median_mt'%(tsm)] = median(mts); db['shapes_%s_var_mt'%(tsm)] = var(mts);
		db['shapes_%s_pc'%(tsm)] = pc(res);
		if id=='agg':
			#calculate the SEMs
			db['shapes_%s_rt_SEMs'%(tsm)] = compute_BS_SEM(all_rt_matrix, 'time'); db['shapes_%s_il_SEMs'%(tsm)] = compute_BS_SEM(all_il_matrix, 'time');
			db['shapes_%s_mt_SEMs'%(tsm)] = compute_BS_SEM(all_mt_matrix, 'time'); db['shapes_%s_pc_SEMs'%(tsm)] = compute_BS_SEM(all_res_matrix, 'result');
			# do ANOVA stuff
			    
			db.sync();			
	print 'Completed simple effects analysis of number of targets';


def computeNrStim(trial_matrix, id='agg'):
    if id=='agg':
        db=subject_data;
        #add in anova stuff later
    else:
        db=individ_subject_data;
    #here cycle through the total number of stimuli and number of distractors, finding the RT and accuracy for each combo
    for nr_t, nr_dists in zip([1,2],[[2,3,5,10,14],[3,4,6,10,13]]):
        print 'Number of targets: %d'%nr_t; print ;
        for d in nr_dists:
            print 'Number of dists: %d'%d; print ;
            #collect the appropriate results and RTs for this condition
            all_res_matrix = [[tee.result for tee in ts if ((tee.nr_targets==nr_t)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors)))] for ts in trial_matrix];
            all_rt_matrix = [[tee.response_time for tee in ts if ((tee.nr_targets==nr_t)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
            all_il_matrix = [[tee.initiation_latency for tee in ts if ((tee.nr_targets==nr_t)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
            all_mt_matrix = [[tee.movement_time for tee in ts if ((tee.nr_targets==nr_t)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
            res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not
            # #get individual rt sds and il sds to 'shave' the rts of extreme outliers
            # ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
            # rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
            # il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
            # mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
            # rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
            #for now, dont' shave the RTs 
            rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
            mts = [ms for j in all_mt_matrix for ms in j];
            if len(rts)==0:
                continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
            #now find the relevant stats and set up the data into the database
            db['%s_targs_%s_dists_%s_nr_stim_mean_rt'%(nr_t,d,(nr_t+d))] = mean(rts); db['%s_targs_%s_dists_%s_nr_stim_median_rt'%(nr_t,d,(nr_t+d))] = median(rts); db['%s_targs_%s_dists_%s_nr_stim_var_rt'%(nr_t,d,(nr_t+d))] = var(rts);
            db['%s_targs_%s_dists_%s_nr_stim_mean_il'%(nr_t,d,(nr_t+d))] = mean(ils); db['%s_targs_%s_dists_%s_nr_stim_median_il'%(nr_t,d,(nr_t+d))] = median(ils); db['%s_targs_%s_dists_%s_nr_stim_var_il'%(nr_t,d,(nr_t+d))] = var(ils);
            db['%s_targs_%s_dists_%s_nr_stim_mean_mt'%(nr_t,d,(nr_t+d))] = mean(mts); db['%s_targs_%s_dists_%s_nr_stim_median_mt'%(nr_t,d,(nr_t+d))] = median(mts); db['%s_targs_%s_dists_%s_nr_stim_var_mt'%(nr_t,d,(nr_t+d))] = var(mts);
            db['%s_targs_%s_dists_%s_nr_stim_pc'%(nr_t,d,(nr_t+d))] = pc(res);
            if id=='agg':
                #calculate the SEMs
                db['%s_targs_%s_dists_%s_nr_stim_rt_SEMs'%(nr_t,d,(nr_t+d))] = compute_BS_SEM(all_rt_matrix, 'time'); db['%s_targs_%s_dists_%s_nr_stim_il_SEMs'%(nr_t,d,(nr_t+d))] = compute_BS_SEM(all_il_matrix, 'time');
                db['%s_targs_%s_dists_%s_nr_stim_mt_SEMs'%(nr_t,d,(nr_t+d))] = compute_BS_SEM(all_mt_matrix, 'time'); db['%s_targs_%s_dists_%s_nr_stim_pc_SEMs'%(nr_t,d,(nr_t+d))] = compute_BS_SEM(all_res_matrix, 'result');
                # do ANOVA stuff
                
            db.sync();
    print 'Completed computation of number of stimuli data...';


def computeHFRelation(trial_matrix, id='agg'):
	#this code should go through for each subject and calculate the same vs. different HF contrast
	#for two target trials for each level of the number of stimuli.
    if id=='agg':
        db=subject_data;
        #add in anova stuff later
    else:
        db=individ_subject_data;
	#cycle through the two target trials, looking for whetehr the targets were in the same hf or not
	for hf,bool in zip(['s','d'],[1,0]):
		print 'Starting looking at %s hemifield relation'%hf; print ;
		#then go through the number of distractors
		for d in [3,4,6,10,13]:
			print 'Starting %s distractors'%d; print ;
            #collect the appropriate results and RTs for this condition
			all_res_matrix = [[tee.result for tee in ts if ((tee.same_hf==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors)))] for ts in trial_matrix];
			all_rt_matrix = [[tee.response_time for tee in ts if ((tee.same_hf==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			all_il_matrix = [[tee.initiation_latency for tee in ts if ((tee.same_hf==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			all_mt_matrix = [[tee.movement_time for tee in ts if ((tee.same_hf==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not			
            # #get individual rt sds and il sds to 'shave' the rts of extreme outliers
            # ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
            # rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
            # il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
            # mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
            # rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
            #for now, dont' shave the RTs 
			rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
			mts = [ms for j in all_mt_matrix for ms in j];
			if len(rts)==0:
				continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
            #now find the relevant stats and set up the data into the database
			db['2_targs_%s_hf_%s_dists_%s_nr_stim_mean_rt'%(hf,d,(2+d))] = mean(rts); db['2_targs_%s_hf_%s_dists_%s_nr_stim_median_rt'%(hf,d,(2+d))] = median(rts); db['2_targs_%s_hf_%s_dists_%s_nr_stim_var_rt'%(hf,d,(2+d))] = var(rts);
			db['2_targs_%s_hf_%s_dists_%s_nr_stim_mean_il'%(hf,d,(2+d))] = mean(ils); db['2_targs_%s_hf_%s_dists_%s_nr_stim_median_il'%(hf,d,(2+d))] = median(ils); db['2_targs_%s_hf_%s_dists_%s_nr_stim_var_il'%(hf,d,(2+d))] = var(ils);
			db['2_targs_%s_hf_%s_dists_%s_nr_stim_mean_mt'%(hf,d,(2+d))] = mean(mts); db['2_targs_%s_hf_%s_dists_%s_nr_stim_median_mt'%(hf,d,(2+d))] = median(mts); db['2_targs_%s_hf_%s_dists_%s_nr_stim_var_mt'%(hf,d,(2+d))] = var(mts);
			db['2_targs_%s_hf_%s_dists_%s_nr_stim_pc'%(hf,d,(2+d))] = pc(res);
			if id=='agg':
                #calculate the SEMs
				db['2_targs_%s_hf_%s_dists_%s_nr_stim_rt_SEMs'%(hf,d,(2+d))] = compute_BS_SEM(all_rt_matrix, 'time'); db['2_targs_%s_hf_%s_dists_%s_nr_stim_il_SEMs'%(hf,d,(2+d))] = compute_BS_SEM(all_il_matrix, 'time');
				db['2_targs_%s_hf_%s_dists_%s_nr_stim_mt_SEMs'%(hf,d,(2+d))] = compute_BS_SEM(all_mt_matrix, 'time'); db['2_targs_%s_hf_%s_dists_%s_nr_stim_pc_SEMs'%(hf,d,(2+d))] = compute_BS_SEM(all_res_matrix, 'result');
                # do ANOVA stuff
                
			db.sync();			
    print 'Completed computation of hemifield relation data...';			

def computeTargetShapesMatch(trial_matrix, id='agg'):
	#this code should go through for each subject and calculate the targets match vs. not contrast
	#for two target trials for each level of the number of stimuli.
    if id=='agg':
        db=subject_data;
        #add in anova stuff later
    else:
        db=individ_subject_data;
	#cycle through the two target trials, looking for whetehr the targets were in the same hf or not
	for tsm,bool in zip(['match','not_match'],[1,0]):
		print 'Starting looking at %s level of target shapes matching'%hf; print ;
		#then go through the number of distractors
		for d in [3,4,6,10,13]:
			print 'Starting %s distractors'%d; print ;
            #collect the appropriate results and RTs for this condition
			all_res_matrix = [[tee.result for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors)))] for ts in trial_matrix];
			all_rt_matrix = [[tee.response_time for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			all_il_matrix = [[tee.initiation_latency for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			all_mt_matrix = [[tee.movement_time for tee in ts if (((tee.target_types[0]==tee.target_types[1])==bool)&(tee.nr_targets==2)&(tee.nr_distractors==d)&(tee.nr_stimuli==(tee.nr_targets+tee.nr_distractors))&(tee.result==1))] for ts in trial_matrix];
			res = [rs for h in all_res_matrix for rs in h]; #get all the results together; this won't change whether Im trimming or not			
            # #get individual rt sds and il sds to 'shave' the rts of extreme outliers
            # ind_rt_sds=[std(are) for are in all_rt_matrix]; ind_il_sds=[std(eye) for eye in all_il_matrix]; ind_mt_sds=[std(em) for em in all_mt_matrix];
            # rt_matrix=[[r for r in individ_rts if (r>=(mean(individ_rts)-(3*ind_rt_sd)))&(r<=(mean(individ_rts)+(3*ind_rt_sd)))] for individ_rts,ind_rt_sd in zip(all_rt_matrix,ind_rt_sds)]; #trim matrixed rts of outliers greater than 3 s.d.s from the mean
            # il_matrix=[[i for i in individ_ils if (i>=(mean(individ_ils)-(3*ind_il_sd)))&(i<=(mean(individ_ils)+(3*ind_il_sd)))] for individ_ils,ind_il_sd in zip(all_il_matrix,ind_il_sds)];
            # mt_matrix=[[m for m in individ_mts if (m>=(mean(individ_mts)-(3*ind_mt_sd)))&(m<=(mean(individ_mts)+(3*ind_mt_sd)))] for individ_mts,ind_mt_sd in zip(all_mt_matrix,ind_mt_sds)];
            # rts = [r for y in rt_matrix for r in y]; ils = [i for l in il_matrix for i in l]; mts = [ms for j in mt_matrix for ms in j];	
            #for now, dont' shave the RTs 
			rts = [r for y in all_rt_matrix for r in y]; ils = [i for l in all_il_matrix for i in l];
			mts = [ms for j in all_mt_matrix for ms in j];
			if len(rts)==0:
				continue; #skip computing and saving data if there was no data that matched the criteria (so the array is empty)
            #now find the relevant stats and set up the data into the database
			db['2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_rt'%(tsm,d,(2+d))] = mean(rts); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_median_rt'%(tsm,d,(2+d))] = median(rts); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_var_rt'%(tsm,d,(2+d))] = var(rts);
			db['2_targs_shapes_%s_%s_dists_%s_nr_stim_mean_il'%(tsm,d,(2+d))] = mean(ils); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_median_il'%(tsm,d,(2+d))] = median(ils); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_var_il'%(tsm,d,(2+d))] = var(ils);
			db['2_targs_shapes_%s_dists_%s_nr_stim_mean_mt'%(tsm,d,(2+d))] = mean(mts); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_median_mt'%(tsm,d,(2+d))] = median(mts); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_var_mt'%(tsm,d,(2+d))] = var(mts);
			db['2_targs_shapes_%s_%s_dists_%s_nr_stim_pc'%(tsm,d,(2+d))] = pc(res);
			if id=='agg':
                #calculate the SEMs
				db['2_targs_shapes_%s_%s_dists_%s_nr_stim_rt_SEMs'%(tsm,d,(2+d))] = compute_BS_SEM(all_rt_matrix, 'time'); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_il_SEMs'%(tsm,d,(2+d))] = compute_BS_SEM(all_il_matrix, 'time');
				db['2_targs_shapes_%s_%s_dists_%s_nr_stim_mt_SEMs'%(tsm,d,(2+d))] = compute_BS_SEM(all_mt_matrix, 'time'); db['2_targs_shapes_%s_%s_dists_%s_nr_stim_pc_SEMs'%(tsm,d,(2+d))] = compute_BS_SEM(all_res_matrix, 'result');
                # do ANOVA stuff
                
			db.sync();			
    print 'Completed computation of target shapes matching data...';
				

def compute_BS_SEM(data_matrix, type):
    #calculate the between-subjects standard error of the mean. data_matrix should be matrix of trials including each subject
    #should only pass data matrix into this function after segmenting into relevant conditions
	agg_data = [datum for person in data_matrix for datum in person]; #get all the data together
	n = len(data_matrix);
	if type=='time':
		grand_mean = mean(agg_data);
		matrix = [[dee for dee in datas] for datas in data_matrix]
		err = [mean(d) for d in matrix if (len(d)>0)]-grand_mean;
		squared_err = err**2;
		MSE = sum(squared_err)/(n-1);
	elif type=='result':
		grand_pc = pc(agg_data);
		matrix = [[dee for dee in datas] for datas in data_matrix]
		err = [pc(d) for d in matrix if (len(d)>0)]-grand_pc;
		squared_err = err**2;
		MSE = sum(squared_err)/(n-1);
	denom = sqrt(n);
	standard_error_estimate=sqrt(MSE)/float(denom);
	return standard_error_estimate;


# Importing Methods #############################################################################################################

#define a function to import individual .mat data files
def loadBlock(subid,block_type,block_nr):
	#returns a single Block object corresponding to the block number and subject id
	#block type should be a string corresponding to the task type(e.g. 'Discrim')
	filename = glob(datapath+'%s'%subid+'/'+'*_%s_%d.mat'%(subid,block_nr)); #Not sure if this regex will work here, must check
	matdata = loadmat(filename[0],struct_as_record=False,squeeze_me=True)['block']; #use scipy loadmat() to load in the files
	block=Block(matdata); #here, create Block object with dictionary of trial data in matdata
	return block;

#define a function to import all .mat data files for a given subject
def loadAllBlocks(subid):
    filenames = glob(datapath+'%s'%subid+'/'+'*_%s_[1-9].mat'%subid); #got to check that this regex works here
    blocks = []; #empty list to hold loaded blocks
    for filename in filenames:
        matdata=loadmat(filename,struct_as_record=False,squeeze_me=True)['block'];
        block=Block(matdata);
        blocks.append(block);
    return blocks #return the loaded blocks as a list for later purposes..

#define functions to get subject specific blocks and aggregate blocks together for analysis, respectively
def getAllSubjectBlocks(ids):
    blocks = [[] for i in range(len(ids))]; #create a list of empty lists to append the individual blocks to
    for i,sub_id in enumerate(ids):
        blocks[i] = loadAllBlocks(sub_id);
        #print "Imported data for subject %s\n"%sub_id;
    #print "Done getting all subject blocks..\n";
    return blocks;

def getTrials(all_blocks):
	#find and add the number of stimuli that trial
    foo = [processTrials(b) for blocks in all_blocks for b in blocks];
    #then segment the trials all together
    trial_matrix = [[t for b in blocks for t in b.trials] for blocks in all_blocks];
    print "Done getting trials together..\n"
    return trial_matrix; #trial matrix will be a n by m, n is the number of trials for a subject and m is the number of subjects

def processTrials(b):
    for t in b.trials:
        t.nr_stimuli = t.nr_targets+t.nr_distractors;

## Data Structures ###############################################################################################################

#define a Block object that will hold the Trials for each block along with relevant data (e.g. date)
class Block(object):
	#object being passed into this class should be a scipy mat_structure of data from the block
	def __init__(self, matStructure=None):
		self.block_nr= matStructure.block_nr;
		self.date = str(matStructure.date);
		self.sub_id = str(matStructure.sub_id);
		self.block_type = str(matStructure.type);
		self.nr_invalids = matStructure.nr_invalids;
		self.sp = matStructure.sp;
		self.dp = matStructure.dp;
		self.trials = [trial(trialData,self.block_type,self.sub_id) for trialData in  matStructure.trial_data];

#define a Trial object that will hold the individual trial data 
class trial(object):
	#object being passed into this Trial instance should be a dictionary corresponding to the trial data for this given trial
    def __init__(self, trialData, block_type, sub_id):
        self.sub_id = sub_id;
        self.block_nr = trialData.block_nr; #self.trial_nr = trialData.trial_nr;
        self.block_type = block_type;
        self.trial_type = trialData.trial_type; #determines the colors, distances, nr of targets
        self.nr_targets = trialData.nr_targets;
        self.nr_distractors = trialData.nr_distractors;
        self.target_col = str(trialData.target_col); #red or green
        self.dist_col = str(trialData.dist_col); #red or green
        self.target_types = trialData.t_types;
        self.inter_target_distance = trialData.t_dist;
        self.same_hf = trialData.same_hf;
        self.nr_left_side = trialData.nr_left_side;
        self.nr_right_side = trialData.nr_right_side;
        self.target_shapes_match = trialData.target_shapes_match;
        #below here is the coordinates and distances
        self.target_coors = trialData.target_coors;
        self.dist_coors = trialData.dist_coors;
        self.target_distance = trialData.target_distances;
        self.dist_distances = trialData.distractor_distances;
        #trial times
        self.trial_times = trialData.trial_times;
        self.initiation_latency = trialData.trial_times.initiation_latency*1000;
        self.response_time = self.trial_times.response_time*1000; #put every time into seconds  
        self.movement_time = self.response_time-self.initiation_latency;
        #response and results
        self.reponse = str(trialData.response); #letter corresponding to presented
        self.result = trialData.result; #right or wrong, 1 or 0
        self.selected_type = trialData.selected_type; #precense or absence
        self.abort = trialData.abort_trial;
        #finally, eye position and pupil size information
        self.eyeX = trialData.eyeX;
        self.eyeY = trialData.eyeY;
        self.p_size = trialData.pSize;
        self.sample_times = trialData.sampleTimes;
        self.drift_shift = trialData.drift_shift;