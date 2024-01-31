

# from bpmn_python.bpmn_process_csv_import import BpmnDiagramGraphCSVImport
# from bpmn_python.bpmn_diagram_rep import BpmnDiagramGraph
from bpmn_process_csv_import import BpmnDiagramGraphCSVImport
# Create an instance of BpmnDiagramGraph
bpmn_diagram = BpmnDiagramGraph()

# Specify the path to your CSV file
csv_filepath = 'path/to/your/csv/file.csv'

# Load the BPMN diagram from the CSV file
BpmnDiagramGraphCSVImport.load_diagram_from_csv(csv_filepath, bpmn_diagram)