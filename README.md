# CSC 510- Homework3
Effort Estimation and Bad Smells

#Theory Question 1
<b>List 1</b>

* Scale Factors
 1. Precedentedness (Prec)<br/>
    Description: Has this project/problem been seen before. <br/>
    Story: The management gave an innovative requirement in the project that has never been done before. This makes the Prec value low causing an exponential increase in effort  

 2. Flexibility (Flex)<br/> 
    Description: It tells how flexible is the development requirement  
    Story: The management gave an in-house project which did not have many rigid development requirements. this makes the value as well as effort required pretty high.    

 3. Risk Resolution (Resl)  
    Description: It means if any risk resolution activities were carried out during the project ideation and development phase.  
    Story: The management needed multiple risk resolution activities during the course of the project. This made the value of Resl to be high causing a decrease in effort.  

 4. Team Cohesion (Team)  
    Description: It denotes how well did the team work as a single group and how compatible are they with each other.    
    Story: The management took a team of people who have worked together earlier in multiple projects. This made the Team value high causing exponential decrease in effort.  

 5. Process Maturity (Pmat)  
    Description: It denotes how good is the team while following the development process like the Dev-Test-Prod cycle or the project scrums that each organization follows.  
    Story: The management used a tried and tested process which had been a norm in that company for a long time for this project. This ensured that eveyone is comforable with the process and knows how to work with that process in mind. This caused a high value of Pmat and decreased effort.  

<b>List 2</b>

* Upsies (Add effort)  
  1. Required Reliability (rely)  
     Description: It determines how reliable the system should be.  
     Story: The management decided that the system should be highly reliable causing the value of rely to be high and the effort to increase.  

  2. Secondary Memory Storage Requirements (data)    
     Description: This describes if the project requires secondary storage like databases etc.  
     Story: The management wanted to have databses for storing all the data required by the system causing the data value as well as effort to go up.  

  3. Program Complexity (cplx)  
    Description: It determines how complex the program is.  
    Story: When the program is highly complex, the value of cplx will go up and effort required will be increased as well.  

  4. Software Reuse (ruse)    
    Description: It determines how much of the software has been reused from previous projects.  
    Story: The management mandated that no previous software should be used or referenced while making this project. This caused the ruse value to be high and effort to increase.  

  5. Documentation Requirements (docu)  
    Description: It denotes how much documentation should be undertaken during the project.  
    Story: The management required that the system should have thorough documentation for each function of each file. This caused a high docu value and increased the effort.  

  6. Runtime Pressure (time)    
    Description: It is an indicator of the execution time constraints imposed on the system.  
    Story: The management required that the system should be able to do it's work in 1 second or less. It also mandated that it should not use more than 1 MB of RAM during execution. This caused time to have a high value and hence increased the effort.  

  7. Main Memory Requirements (stor)    
    Description: This denotes the amount or dependence of the system on the main memory.  
    Story: The management wanted no data to be stored in secondary storage and make the system fully dependant on the main memory. This made making the system to depend on and handle the highly volatile main memory causing a high stor value and a corresponding increase in the effort.  

  8. Platform Volatility (pvol)  
    Description: This determines the volatility of the platform. This determines the value of stability of the platform that is being used for the project.  
    Story: The management required that the project be developed on Rust. Rust is highly volatile and has a new release every week. This amounts to a high pvol value and an increase in effort.  


**List 3**    

* Downsies (Reduce effort) 
  1. Analyst Capability (acap)  
    Description: This determines the capability of the Analyst.  
    Story: The management chose to have experienced analysts in this project. This corresponds to a high acap value and a reduction in effort.  

  2. Programmer Capability (pcap)  
    Description: This determines the capability of the programmer.  
   Story: The management chose to have skilled programmers for this project. This corresponds to a high pcap value and a reduction in effort.  

  3. Programmer Continuity (pcon)  
    Description: This determines the value corresponding to the continuity of the programmer. It means retaining the programmer for the entire duration of the project.  
  Story: The management fixed the team members for the project and they were not taken out in the middle of the project. This results in a high pcon value and reduced effort.

  4. Analyst Experience (aexp)  
    Description: It determines the experience of the analyst.  
   Story: The management involved experienced analysts in the project resulting in a high aexp value and thus reduced effort.  

  5. Programmer Experience (pexp)  
    Description: It determines the experience of the programmer.  
   Story: The management involved experienced programmers in the project resulting in a high pexp value and thus reduced effort.  

  6. Language and Tool Experience (ltex)  
    Description: This determines the experience of the team with the tool and the language used in the project.  
  Story: The management used tools and language in which the team members were experienced and comfortable. This corresponded to a high ltex value and reduced effort.  

  7. Use of Tools (tool)  
   Description: It determines the quality and quantity of tools used in the project.  
  Story: The management decided to use many tools to help ease the work in the project. This led to a high tool value and thus reduced effort.  

  8. Multiple Site Development (site)  
    Description: This denotes whether the development was done over multiple sites or on a single site.  
   Story: The management decided to go with development over multiple sites which led to concurrent and distributed work corresponding to a high site value and a reduced effort.  

  9. Length of Schedule (sced)  
    Description: This determines the length of the schedule or project duration granted.  
  Story: The management decided to go with a relaxed schedule causing a high sced value and hence reduced effort.  
  
#Theory Question 2  : Treatments (Management Actions)  
  *  
   <code> def reduceQuality():  return dict(
rely = [1], docu=[1], time = [3], cplx = [1]) </code>  
   Management of the company decided to reduce the effort by reducing the amount of information to be documented. Also, they decided that the product that they are developing need not be highly reliable and it need not be complex at all so that the effort they need to put in would be less.  

  *  
   <code>  def relaxSchedule(): return dict(sced = [5]) </code>  
   The management of the company noted that the existing schedule is too rigid and decided to reduce the effort by relaxing the schedule so that everyone gets more time to work on the project.  

  *  
   <code> def improveProcessMaturity(): return dict(Pmat = [5]) </code>  
   The management of the company tested a process for long time to ensure that everyone in the company is comfortable with the process and they could work with the process in mind.They used this tested process in the project.  


#Theory Question 3  

* flight and ground
 1. range is different :  
  flight : 7,418  
  ground : 11,392  
   This corresponds to the fact that it took a significantly higher amount of effort for ground as compared to flight project.  
 
 2. cplx is different :  
  flight : 3,4,5,6  
  ground : 1,2,3,4  
   This corresponds to the fact that flight project was more complex as compared to ground project.  
 
 3. rely is different :  
  flight : 3,4,5  
  ground : 1,2,3,4  
   This corresponds to the fact that flight project had a higher required reliability than the ground one.  


* osp and osp2  
 1. flex is different :  
  osp : 2,3,4,5  
  osp2 : 3  
   This corresponds to the fact that osp2 was rigid in terms of flexibility while osp ranged between high and low flexibility.  
 
 2. precedentness is different :  
  osp : 1,2
  osp2 : 3,4,5  
   This corresponds to the fact that osp was novel in terms of what it was doing and people had no prior experience while in osp2, similar kinds of problems were seen earlier.  
 
 3. aexp is higher for osp2 :  
  osp : 2,3  
  osp2 : 4  
   This corresponds to the fact that osp2 had analysts who were more experienced than those in osp. 

#Theory Question 4 (Bad Smells)    
  *   
   Stink[('sced','cplx')] = [  
 [0,0,0,1,2,4],  
 [0,0,0,0,1,2],   
 [0,0,0,0,0,1],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0]]    
  The management decided to take a highly complex project and gave a very tight schedule to finish the same resulting in a bad smell.    

  *  
   Stink[('sced','rely')] = [  
 [0,0,0,1,2,0],  
 [0,0,0,0,1,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0]]  
  The management decided to make the project highly reliable but gave only a small amount of time to finish the same resulting in a bad smell.  

  *  
   Stink[('ltex','pcap')] = [   
 [4,2,1,0,0,0],  
 [2,1,0,0,0,0],  
 [1,0,0,0,0,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0],  
 [0,0,0,0,0,0]]  
  The management decided to work with programmers who had low capability and also had very little language and tool experience resulting in a bad smell.  

##Practice Tasks  

 * Task 1: Worse Bad Smells and Better Effort  
  Treatment  
<code>
def screwBadSmell(): return dict (
  Team = [1], Flex = [5], cplx = [6])
</code>  

* Task 2: Better Bad Smell and Worse Effort  
  Treatment  

<code>
def doSomething(): return dict(  
 acap=[5],pcap=[2],pcon=[1], aexp=[5], pexp=[1], ltex=[2], docu=[5])  </code>

* Task 3: Better Bas Smell and Better Effort    
  Treatment  
<code>  
def doSomething3(): return dict(
 time=[3],stor=[3],pvol=[3],tool=[3], site=[6], acap=[5],pcap=[1])</code>

###Effects:  

* Bad Smells:  
  ![Bad Smells] (https://github.com/incognito666/homework3/blob/master/bad%20smells.png)  
* Effort:  
  ![Effort] (https://github.com/incognito666/homework3/blob/master/effort.png)  
