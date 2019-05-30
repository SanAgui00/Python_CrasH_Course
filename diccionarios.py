Nomad = {'type':'rover','color':'black','processor':'JetsonTX1'}
print(Nomad['type'])

BARB = {'type':'test-bed','color':'black','type':'wheeled'}
BARB

myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}
myRobots

myRobots['Llamabot'] = 'Getting to it'
myRobots

del myRobots['Llamabot']
myRobots

workingRobots = myRobots.copy()
workingRobots

otherRobots = {'Rasbot-pi':'Pi-bot frombook','spiderbot':'broken'}
myRobots.update(otherRobots)
myRobots
