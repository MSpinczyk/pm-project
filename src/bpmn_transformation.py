import bpmn_python.bpmn_diagram_rep as diagram
import bpmn_python.bpmn_diagram_layouter as layouter

import os

def transform_to_bpmn(spreadsheet_path, bpmn_output_path):
    bpmn_graph = diagram.BpmnDiagramGraph()
    bpmn_graph.load_diagram_from_csv_file(os.path.abspath(spreadsheet_path))
    layouter.generate_layout(bpmn_graph)
    bpmn_graph.export_xml_file('output/', bpmn_output_path)

transform_to_bpmn('test.csv', 'test_2.bpmn')