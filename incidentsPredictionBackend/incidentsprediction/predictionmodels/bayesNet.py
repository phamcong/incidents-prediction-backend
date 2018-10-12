import os
import pyAgrum as gum
import pyAgrum.lib.ipython as gnb
def bayesNet(evs):

    # Creating BayesNet with 4 variables
    bayesNets = gum.BayesNet('Quality Prediction')

    # Adding nodes the long way
    commitNumber = bayesNets.add(gum.LabelizedVariable('Commit Number','cloudy ?',0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfDevloper = bayesNets.add(gum.LabelizedVariable("Number Of Devlopers", "Devs",0).addLabel("Low").addLabel("Medium").addLabel("High"))
    buildFailures = bayesNets.add(gum.LabelizedVariable('Build Failures','cloudy ?',0).addLabel("Low").addLabel("Medium").addLabel("High"))
    numberOfFixedBug = bayesNets.add(gum.LabelizedVariable('Numbers Of Fixed Bug','cloudy ?',2))
    nbFunctionalEvolution = bayesNets.add(gum.LabelizedVariable("nb functional evolution", "Evol",0).addLabel("Low").addLabel("Medium").addLabel("High"))
    categoryOfIncident = bayesNets.add(gum.LabelizedVariable("Incident Category", "Devs",0).addLabel("Tertiaire").addLabel("Secondaire").addLabel("Prmaire"))

    # creation of the links between  nodes 
    for link in [(commitNumber,buildFailures),(numberOfDevloper,buildFailures),(nbFunctionalEvolution,numberOfFixedBug),(buildFailures,numberOfFixedBug),(buildFailures, categoryOfIncident),(numberOfFixedBug,categoryOfIncident )]:
        bayesNets.addArc(*link)
        print(bayesNets)

    bayesNets.cpt(commitNumber)[:]= [0.5,0.3,0.2]
    bayesNets.cpt(numberOfDevloper)[:]= [0.5,0.4,0.5]
    bayesNets.cpt(nbFunctionalEvolution)[:]= [0.5,0.4,0.5]
    print(bayesNets.cpt(numberOfFixedBug).var_names)
    bayesNets.cpt(buildFailures).var_names
    bayesNets.cpt(numberOfDevloper)
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'nb functional evolution': "Medium"}]=[0.5,0.4]
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'nb functional evolution': "High"}]=[0.54,0.46]
    #bayesNets.cpt(numberOfFixedBug)[{'buildFailures': 1, 'nb functional evolution': "Low"}]=[0.54,0.46]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'nb functional evolution': "Medium"}]=[0.5,0.4]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'nb functional evolution': "High"}]=[0.54,0.46]
    bayesNets.cpt(numberOfFixedBug)[{'Build Failures': 0, 'nb functional evolution': "Low"}]=[0.53,0.47]
    bayesNets.cpt(numberOfFixedBug)

    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Devlopers': "Low"}] = 0.2
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Devlopers': "High"}] = 0.4
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Devlopers': "Low"}] = 0.2
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Devlopers': "High"}] =  0.9
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Devlopers': "Medium"}] = 1
    bayesNets.cpt(buildFailures)[{'Commit Number': "Low", 'Number Of Devlopers': "Medium"}] =  0.9
    bayesNets.cpt(buildFailures)[{'Commit Number': "High", 'Number Of Devlopers': "Medium"}] = 0.1
    bayesNets.cpt(buildFailures)[{'Commit Number': "Medium", 'Number Of Devlopers': "Medium"}] = 0.6
    bayesNets.cpt(buildFailures)

    bayesNets.cpt(categoryOfIncident)[{'Build Failures': 0,'Numbers Of Fixed Bug':0}] = [0.2,0.3,0.5]
    bayesNets.cpt(categoryOfIncident)[{'Build Failures': 0,'Numbers Of Fixed Bug':1}] = [0.5,0.3,0.2]
    bayesNets.cpt(categoryOfIncident)
    ie=gum.LazyPropagation(bayesNets)
    gum.saveBN(bayesNets, "QualtiyPrediction.bifxml")
    bn = gum.loadBN("QualtiyPrediction.bifxml")

    bn

    ie=gum.LazyPropagation(bn)
    ie.makeInference()
    #ie.posterior(buildFailures)
    ie.posterior(categoryOfIncident)
    #ie.posterior(numberOfFixedBug)
    #gnb.showInference(bn,evs={})
    gnb.showInference(bn,evs=evs) # evs = {'Commit Number':"High",'Number Of Devlopers':"Medium", 'nb functional evolution': "High", 'Numbers Of Fixed Bug': 1})
    gum.saveBN(bn, "output.bif")

bayesNet({'Commit Number':"High",'Number Of Devlopers':"Medium", 'nb functional evolution': "High", 'Numbers Of Fixed Bug': 1})