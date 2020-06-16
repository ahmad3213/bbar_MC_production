# bbar_MC_production

cmsrel CMSSW_10_2_5

cd CMSSW_10_2_5/src

cmsenv

voms-proxy-init -voms cm --valid 172:00

git clone https://github.com/ahmad3213/bbar_MC_production/ 

scram b 

#submitting crab jobs for GS step production 

crab submit -c crabConfig_MC_Production_GS.py

#Run the following script to monitor the jobs, It will keep checking jobs after every 30 mints and resubmit the failed jobs 

nohup python manageCrabTask.py -l -r -t bbarTo4mu_GENSIM >& bbarTo4mu_GENSIM.log &

#submitting crab jobs for DIGI step production 

To be included  yet repository

#submitting crab jobs for RECO step production 

To be included yet in repository 


