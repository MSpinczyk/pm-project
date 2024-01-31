from llm_extraction import extract_process_info
from spreadsheet_processing import create_spreadsheet, update_spreadsheet
from bpmn_transformation import transform_to_bpmn

def main():
    # Example workflow
    with open('data/input_text.txt', 'r') as file:
        text = file.read()

    process_info = extract_process_info(text)

    # For the first time
    spreadsheet_path = 'data/extracted_info.csv'
    create_spreadsheet(process_info).to_csv(spreadsheet_path, index=False)

    # For subsequent updates
    new_process_info = extract_process_info('New information from LLM...')
    existing_spreadsheet = pd.read_csv(spreadsheet_path)
    updated_spreadsheet = update_spreadsheet(existing_spreadsheet, new_process_info)
    updated_spreadsheet.to_csv(spreadsheet_path, index=False)

    # Transform to BPMN
    bpmn_output_path = 'data/bpmn_model.bpmn'
    transform_to_bpmn(spreadsheet_path, bpmn_output_path)

if __name__ == "__main__":
    main()
    
