from bpmn_python.bpmn_diagram_rep import BpmnDiagramGraph
from bpmn_python.bpmn_diagram_export import  BpmnDiagramGraphExport
from bpmn_python.bpmn_process_csv_import import BpmnDiagramGraphCSVImport

def transform_to_bpmn(spreadsheet_path, bpmn_output_path):
    bpmn_importer = BpmnDiagramGraphCSVImport()

    # Assume bpmn_diagram is an instance of your BPMN diagram class
    # e.g., bpmn_diagram = YourBpmnDiagramClass()

    # Provide the file path to your CSV file
    csv_filepath = 'test.csv'
    bpmn_diagram = BpmnDiagramGraph()
    # Call the load_diagram_from_csv method to import data from the CSV file
    bpmn_importer.load_diagram_from_csv(csv_filepath, bpmn_diagram)

    
    # Add nodes and edges to the bpmn_diagram...

    # Specify the output directory and filename for the BPMN XML file
    output_directory = "./output/"
    output_filename = "exported_bpmn.xml"

    # Export BPMN diagram to BPMN XML file with Diagram Interchange data
    BpmnDiagramGraphExport.export_xml_file(output_directory, output_filename, bpmn_diagram)
    pass

transform_to_bpmn('x','y')