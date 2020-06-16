from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsername
username = getUsername()
config = config()
config.section_('General')
config.General.workArea = 'OUTFILENAME'
config.General.requestName = 'OUTFILENAME'
config.General.transferOutputs = True
config.General.transferLogs=True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pset.py'
config.JobType.maxMemoryMB = 3000
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = 'DATASETNAME'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = FPJ
config.Data.outputDatasetTag = 'OUTDATANAME'

config.Data.publication = True
config.Data.outLFNDirBase = '/store/group/l1upgrades/%s/MC2020/Sample_Production/bbarTo4mu/OUTDIR/'%username
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.whitelist = ['T2_US_*']
