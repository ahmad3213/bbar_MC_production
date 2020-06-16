
#!/usr/bin/python
#-----------------------------------------------
# Latest update: 2014.09.14
#-----------------------------------------------
import sys, os, pwd, commands
import optparse, shlex, re
import time
from time import gmtime, strftime
import math

#define function for parsing options
def parseOptions():
    global observalbesTags, modelTags, runAllSteps

    usage = ('usage: %prog [options]\n'
             + '%prog -h for help')
    parser = optparse.OptionParser(usage)

    # input options
    parser.add_option('-r', '--requestname', dest='TAG_request', type='string',default='', help='tag to be appended crab request name, default is an empty string')
    parser.add_option('-o', '--outputdatasetname', dest='TAG_data', type='string',default='', help='tag to be appended with dataset name, default is an empty string')
    parser.add_option('-d', '--datasets', dest='DATASETS', type='string', default='datasets_Zp_sample_GENSIM_2017.txt', help='txt file with datasets to run over')
    parser.add_option('-s', '--substring', dest='SUBSTRING', type='string', default='', help='only submit datasets with this string in the name')
    parser.add_option('-c', '--cfg', dest='CONFIGFILE', type='string', default='', help='CMSSW configuration  file ')
    parser.add_option('-f', '--filesperjob', dest='FILESPERJOB', type='string', default='1', help='Files per crab job')
    # store options and arguments as global variables
    global opt, args
    (opt, args) = parser.parse_args()

# define function for processing the external os commands
def processCmd(cmd, quite = 0):
    #    print cmd
    status, output = commands.getstatusoutput(cmd)
    if (status !=0 and not quite):
        print 'Error in processing command:\n   ['+cmd+']'
        print 'Output:\n   ['+output+'] \n'
        return "ERROR!!! "+output
    else:
        return output

def submitAnalyzer():

    # parse the arguments and options
    global opt, args
    parseOptions()

    # save working dir
    currentDir = os.getcwd()

    tag = opt.TAG_request
    tag2 = opt.TAG_data
    outDir= tag
    outData= tag2
    CONFILE = opt.CONFIGFILE
    filesperjob = opt.FILESPERJOB
    if (not os.path.isdir(outDir)):
        cmd = 'mkdir '+outDir
        processCmd(cmd)
        cmd = 'mkdir '+outDir+'/cfg/'
        processCmd(cmd)
    # get the datasets
    print '[Gathering Dataset Information]'
    datasets = []
    cross_section = {}
    nfiles = {}
    nevents = {}
    datasetfiles = {}

    with open(opt.DATASETS, "r") as datasetfile:
        for line in datasetfile:

            if (line.startswith('#')): continue

            if ( not (opt.SUBSTRING=="")):
                if (not (opt.SUBSTRING in line)): continue

            dataset = line.split()[0]
            dataset = dataset.rstrip()
            dataset = dataset.lstrip()
            print 'dataset:',dataset
            datasets.append(dataset)

            #cmd = './das_client.py --query="file dataset='+dataset+'" --limit=10 | grep ".root"'
            #output = processCmd(cmd)
            #while ('error' in output):
            #    time.sleep(1.0);
            #    output = processCmd(cmd)
            #datasetfiles[dataset] =  output.split()
            #nfiles[dataset] = len(datasetfiles[dataset])

            #cmd = './das_client.py --query="dataset dataset='+dataset+' | grep dataset.nevents" --limit=0'
            #output = processCmd(cmd)
            #while ('error' in output):
            #    time.sleep(1.0);
            #    output = processCmd(cmd)
            #nevents[dataset] = output

            #print dataset,'xs:',cross_section[dataset],'nfiles:',nfiles[dataset]#,'nevents:',nevents[dataset]



    # submit the jobs
    print '[Submitting jobs]'
    jobCount=0
    for dataset in datasets:

        #continue
        filename = dataset.split('/')[1]+'_'+dataset.split('/')[2]

        cfgfile = dataset.lstrip('/')
        cfgfile = cfgfile.replace('/','_')+'.py'

        #cmd = 'cp '+cfgtemplate+' '+outDir+'/cfg/'+cfgfile
        #output = processCmd(cmd)

        filelist = ''

#        if (len(filename)>99):
#          newfilename = filename.split('_')[0]
#          filename = newfilename
        filename =  'crab_'+outDir
        crabcfgfile = 'crabConfig_'+filename+'.py'
        cmd = 'cp crabConfig_TEMPLATE.py '+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)

        cmd = "sed -i 's~JOBTAG~"+tag+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)

        cmd = "sed -i 's~CFGFILE~"+outDir+"/cfg/"+cfgfile+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)
        
        cmd = "sed -i 's~OUTFILENAME~"+filename+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)
        
        cmd = "sed -i 's~OUTDATANAME~"+outData+"~g' "+outDir+'/cfg/'+crabcfgfile        
        output = processCmd(cmd) 
        cmd = "sed -i 's~DATASETNAME~"+dataset+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)

        cmd = "sed -i 's~pset.py~"+CONFILE+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)

        cmd = "sed -i 's~OUTDIR~"+outDir+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)
   
        cmd = "sed -i 's~FPJ~"+filesperjob+"~g' "+outDir+'/cfg/'+crabcfgfile
        output = processCmd(cmd)

        print 'Submitting dataset:', dataset
        cmd = 'crab submit -c '+outDir+'/cfg/'+crabcfgfile
        print cmd

        output = processCmd(cmd)
        if ("ERROR!!!" in output):
            print " "
            print " "
            print " "
            print " Something when wrong submitting the last dataset. You should:"
            print "     1) Remove the folder in your resultsAna directory"
            print "     2) Comment out the datasets which have been submitted in the datasets txt file"
            print "     3) Rerun the SubmitCrabJobs.py with the same arguments"
            print " "
            print " "
            print " "
            break
        else:
            print output

# run the submitAnalyzer() as main() 
if __name__ == "__main__":
    submitAnalyzer()

