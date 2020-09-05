from behave import __main__ as runner
import sys
import os
if __name__ == '__main__':
    sys.stdout.flush()
    FeatureFilePath = 'FeaturesFiles'
    #tagList = ' --tags=mytag1 '  # any scenario tagged with this tag
    #    tagList = ' --tags=-mytag2 '                       # any scenario except tagged with this tag
    #    tagList = ' --tags=mytag1,mytag4 '             # mytag1 OR mytag4
    #    tagList = ' --tags=mytag1 --tags=mytag4 '   # mytag1 AND mytag4

    tagList = ' --tags=Vignesh,Tulasi,Regression'
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o reporting_folder'
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain'
    featureFileFolder = 'reporting_folder'
    reportdir = os.getcwd()+"\\"+featureFileFolder
    singleline = FeatureFilePath+tagList+reportingRelated+commonRunnerOptions
    runner.main(singleline)

    os.system('cmd /c "allure serve "'+reportdir)
