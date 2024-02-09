from llm_extraction import *
from spreadsheet_processing import *
from bpmn_transformation import transform_to_bpmn

def main():
    # text input (description of buisness process model)
    text = """A customer brings in a defective computer and the
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
                                finished."""
    
    # praticipants extraction using LLM
    participants = participants_extraction(text)
    
    # svo extraction using LLM
    svos = svo_extraction(text)
    
    # gateways extraction using LLM
    gateways = gateway_extraction(text, svos)

    # process extraction using LLM
    result = extract_process_info_newest(text,participants,svos,gateways)

    # saving spreadsheet in csv format
    save_string_as_csv(result)
    
    # transforming spreadsheet into bpmn model
    transform_to_bpmn("output/output.csv","output.bpmn")

if __name__ == "__main__":
    main()
    
