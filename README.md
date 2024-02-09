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

![BPMN Diagram](https://github.com/exampleuser/MSpinczyk/pm-project/blob/main/example.png)
