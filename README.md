# bbar_MC_production

cmsrel CMSSW_10_2_5

cd CMSSW_10_2_5/src

cmsenv

voms-proxy-init -voms cms --valid 172:00

git clone https://github.com/ahmad3213/bbar_MC_production/ 

scram b (not really needed)

#submitting crab jobs for GS step production 

crab submit -c crabConfig_MC_Production_GS.py

#Run the following script to monitor the jobs, It will keep checking jobs after every 30 mints and resubmit the failed jobs 

nohup python manageCrabTask.py -l -r -t bbarTo4mu_GENSIM >& bbarTo4mu_GENSIM.log &

#submitting crab jobs for DIGI step production 

step1: include the published dataset name of GS(previous) step in file 'dataset_GENSIM.txt' (one dataset per line in case if they are more than one)
step2: Submitting jobs by following command
python SubmitCrabJobs.py -r bbarTo4mu-DIGI -o RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIMRAW -c BPH-RunIIAutumn18DRPremix-01798_bbar_cfg.py -d dataset_GENSIM.txt
step3:Monitoring of jobs
nohup python manageCrabTask.py -l -r -t crab_bbarTo4mu_DIGI >& crab_bbarTo4mu_DIGI.log &

#submitting crab jobs for RECO step production 
step1: include the published dataset name of DIGI (previous) step in file 'dataset_DIGI.txt' (one dataset per line in case if they are more than one)
step2: Submitting jobs by following command
python SubmitCrabJobs.py -r bbarTo4mu-RECO -o RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-RECO -c BPH-RunIIAutumn18DRPremix-01798_bbar_cfg_2.py -d dataset_DIGI.txt -f 2
# -f 2 means 2 input dataset files per job, default is one. Generally RECO step is much faster than previous
step3:Monitoring of jobs
nohup python manageCrabTask.py -l -r -t crab_bbarTo4mu_RECO >& crab_bbarTo4mu_RECO.log &

