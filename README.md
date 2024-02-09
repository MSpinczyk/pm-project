# pm-project

## Project topic: Creating and updating spreadsheet-based processes from LLMs and transforming them to BPMN

Potential tasks: 
* Develop a method that uses Large Language Model (LLM) for extraction of process-related information and transform it to a predefined spreadsheet format.
* Develop a system that uses this method and transforms the spreadsheet to a BPMN model.

Preliminaries: 
https://www.mdpi.com/2076-3417/9/2/345
https://github.com/KrzyHonk/bpmn-python 
(check: bpmn_process_csv_import, bpmn_process_csv_export)



```csv
Task ID, Task Description, Previous Tasks
1,Receive Order,
2,Check Inventory,1
3,Process Payment,1
4,Update Inventory,2 3
5,Dispatch Order,4
```
