# pm-project

## Project topic: Creating and updating spreadsheet-based processes from LLMs and transforming them to BPMN

Potential tasks: 
* Develop a method that uses Large Language Model (LLM) for extraction of process-related information and transform it to a predefined spreadsheet format.
* Develop a system that uses this method and transforms the spreadsheet to a BPMN model.

Preliminaries: 
https://www.mdpi.com/2076-3417/9/2/345
https://github.com/KrzyHonk/bpmn-python 
(check: bpmn_process_csv_import, bpmn_process_csv_export)

### Implementation

Using OpenAI, bpmn-python it was posssible to develop a method that uses LLM for extraction of process related information, transforming it into predefined spreadsheet format and then transforming the spreadsheet to a BPMN model.

Example of textual description:

A customer brings in a defective computer and the
CRS checks the defect and hands out a repair cost
calculation back. If the customer decides that the
costs are acceptable, the process continues, otherwise
she takes her computer home unrepaired. The ongoing
repair consists of two activities, which are executed,
in an arbitrary order. The first activity is to check
and repair the hardware, whereas the second activity
checks and configures the software. After each of
these activities, the proper system functionality
is tested. If an error is detected another arbitrary
repair activity is executed, otherwise the repair is
finished.

Example generated `csv` file is shown below:

```csv
Order,Activity,Condition,Who,Subprocess,Terminated
0,start,,,,
1,Receive defective computer,,Customer,,
2,Check the defect,,CRS,,
3,Hand out a repair cost calculation,,CRS,,
4a,Decide that the costs are acceptable,Acceptable,Customer,yes,
4b,Take computer home unrepaired,Not Acceptable,Customer,,yes
5,Execute repair activities,,CRS,,
6a,Check and repair the hardware,,CRS,,
6b,Check and configure the software,,CRS,,
7,Test system functionality,,CRS,,
8a,Execute another repair activity,Error detected,CRS,,yes
8b,Finish the repair,No error,CRS,,yes
```

Example generated `bpmn` model is shown below:

![alt text](https://github.com/MSpinczyk/pm-project/blob/main/example.png)

The textual description of process and some idea comes from: https://www.researchgate.net/publication/326974252_A_Concept_for_Generating_Business_Process_Models_from_Natural_Language_Description
