from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsername
username = getUsername()
config = config()

config.General.requestName = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-bbarTo4mu'
config.General.workArea = 'bbarTo4mu_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs = False
import os
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'BPH-RunIIFall18GS_cfg_crab.py'
config.Data.outputPrimaryDataset = 'bbarTo4mu_13TeV_pythia8'
config.JobType.inputFiles = [os.environ.get('CMSSW_BASE')+'/src/bbar_MC_production/myBBarnoJpsi.dec']
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100000
NJOBS = 1000   # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS


config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/l1upgrades/MC2020/Sample_Production/bbarTo4mu/GS/'
#config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = True

config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
