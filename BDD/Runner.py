from behave import __main__ as Runner
import os
import sys

if __name__ == '__main__':
    sys.stdout.flush()
    FeatureFilePath = 'FeaturesFiles'
    tagname = ' --tags=-Vignesh' #any scenario with this tag it will run

    #tagname = ' --tags=-Regression' #any scenario with this tag it will run
    #tagname = ' --tags=-Regression' #it wont run except regression tag
    #tagname = ' --tags=Regression,Sanity' #Regression or Sanity
    # tagname = ' --tags=Regression --tags=Sanity' #Regression and Sanity

    reporting_config = ' -f allure_behave.formatter:AllureFormatter -o reporting_folder'
    reporting_folder = 'reporting_folder'

    reportdir = os.getcwd()+"\\"+reporting_folder
    singleline = FeatureFilePath+tagname+reporting_config

    Runner.main(singleline)
    os.system('cmd /c "allure serve "'+reportdir)