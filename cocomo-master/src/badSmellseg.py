from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""
from cocomo import *
from badSmells import *
 
 
PROJECTS  = [osp,flight,ground]#,ground,osp2,anything]
TREATMENTS= [doNothing, doSomething, doSomething3,
             screwBadSmell]
             
 
@go
def _badSmells():
  sample(projects=PROJECTS,score=badSmell)
   
@go
def _whatStinks():
    rseed(1)
    for project in PROJECTS:
        print("\n",project.__name__)
        stinks = whatStinks(project)
        worst = stinks[0][0]
        for stink,what in stinks:
            if stink > worst*0.5:
                print('stink = ',stink,' when ',what)

@go
def _badSmellsTreated():
  rseed(1)
  for project in PROJECTS:
    print("\n#### ",project.__name__," ","#"*50,"\n")
    sample(projects=[project],treatments=TREATMENTS,score=badSmell)

 
 

 
