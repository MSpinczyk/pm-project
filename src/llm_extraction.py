from openai import OpenAI

def extract_process_info(text):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with text description of buisness process model.  Generate Spreadsheet represantation of it. The Order and Activity columns must always be completed. Example of text and spreadshet:
        The goal of this process is the preparation of a tramway car to leave the storage yard in the
        morning. In the workflow, there are two organizational participants: the Depot which is responsible
        for storing and servicing the rolling stock and the Traffic Department which controls and manages
        the daily operations, as well as the human actor, represented by the driver. The desired outcome
        of the process is the successful departure of the car from the depot which results in starting regular
        service with passengers. Based on the departure time taken from the schedule, the Traffic Department
        prepares and prints the Traffic Card which serves as the main document for the driver. In the next step,
        two parallel chains of activities are executed. The Depot prepares the car for the daily service while the
        Traffic Department awaits the driver. If the driver does not arrive, a next employee is called to come.
        Then, the driver is tested fot alcohol level in the exhaled air. If alcohol is detected, a new driver is called
        and the testing procedure is repeated. Finally, when the tramway car is ready for departure and the
        driver is authorized to work, the car can be taken by the driver from the outbound track. The process
        ends when the Traffic Department registers the departure in their systems.

        Order | Activity | Condition | Who | Input | Output
        0 | start at time | Scheduled Departure | Traffic Department | | 
        1 | Print Traffic Card | | | | Traffic card
        2a1 | Take Car from Stock | | Depot | | 
        2a2 | Wash Car | | | | 
        2a3 | Place Car on Track | | | | 
        2b1 | Await Driver | | Traffic Department | | 
        2b2a | goto 2b3 | Driver arrived | | | 
        2b2b | Call for Driver | else | | | 
        2b3 | Check Alcohol Level | | | | 
        2b4a | Authorize Driver | Alcohol level OK | | | 
        2b4b | goto 2b2b | else | | | 
        3 | Take Car from Track | | Driver | Traffic card | 
        4 | Register Departure | | Traffic Department | | 
        5 | end | Registered Departure | | | """
        },
        {
        "role": "user",
        "content": f"""{text}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

def participants_extraction(text):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with text. Try to extract information about possible participants (people, systems or organizations which performs the
                    tasks). Text is about buisness process model. Return only participants found in text, do not guess. Return it in format: Particpiant1, Particpiant2, ..."""
        },
        {
        "role": "user",
        "content": f"""{text}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

def svo_extraction(text):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with text. Try to search of basic SVO constructs (Subject-verb-object). Return it in format: SVO: ; SVO: ; ..."""
        },
        {
        "role": "user",
        "content": f"""{text}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

def gateway_extraction(text, svo):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with text and SVOs. Try to find gateway keywords that signalizes the presence of conditional 
                        (exclusive or inclusive) and parallel gateways (example words: If, otherwise). For every svo, if no gateway then just return Gateway keyword: ; for this SVO. 
                        Return it in format: Gateway keyword: ; Gateway keyword: ; ... Length of return should be the same as input SVO. """
        },
        {
        "role": "user",
        "content": f"""Text:{text}, SVO:{svo}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

def extract_process_info_newest(text, participants, svo, gateway):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with text, particpants, SVOs and gateway kewords. Based on those informations generate a csv with columns: Order,Activity,Condition,Who,Subprocess,Terminated. 
                    Start always with: 0,start,,,,. If there is a split for branches (gateway) from for example Order number 1, then next acctivieties have Order 2a, 2b... 
                    (if we have for example 1 then we later can not have 1a or 1b etc.) . 
                    The values ​​in the Orders column should be increasing.
                    In this branch next activity will have Order 2b2, if again there will be a gateway, then we will have Orders 2b2a and 2b2b. Activity could be also 'goto 2b3'. 
                    If there is no following Activity after some Activity then last Activity should be terminated ('yes'), if after for example 4a and 4b there is 5, and 4b activtes do not have some continuation, 
                    then the shoud be terminated. Not all places in the table need to be filled.
                    Try not to use participants/who in Activity names. Return result in csv format.
                    Make sure that in column Termineted or Subprocess the 'yes' is lowercase. If you have at the end diffrent branches, all should be terminted. 
                    Example two last 7a, 7b should be set 'yes' in Terminated column.
                    In who column there should be participants.

                    Example correct csv's, do it similar way:
                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,start,,,,
                    1,Validate Passenger Ticket & Identification,,Check In Counter,,
                    2a,Confirm Itinerary,Validity,,yes,
                    2b,Reject Passenger,else,,,yes
                    3,Ask Passenger for Prohibited Objects,,,,
                    4a,Remove Prohibited Objects,Prohibited Objects,,,
                    4b,goto 5,else,,,
                    5,Ask Passenger for Baggages,,,,
                    6,Weight Baggages,,,,
                    7,Calculate Additional Fees,,,,
                    8,Inform Passenger of Additional Fees,,,,
                    9,Collect Payment of Fees,,,,
                    10a,Generate and Print Boarding Pass,,,,
                    10b1,Generate and Print Baggage Tags,,,,
                    10b2,Identify and Move Baggages,,,,
                    11,"Hand out Boarding Pass, Ticket and Identification",,,,yes

                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,start,,,,
                    1,Receive Order,,,,
                    2a1,Fill Order,Accepted,,,
                    2a2a1,Send Invoice,,,,
                    2a2a2,Make Payment,,,,
                    2a2a3,Accept Payment,,,,
                    2a2b,Ship Order,,,,
                    2b,goto 3,Rejected,,,
                    3,Close Order,,,,yes

                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,Receive pizza order,,,,
                    1,Answer customer call,,,yes,
                    2,Assign the Order,,,,
                    3,Prepare the Pizza,,,,
                    4,Cook the Pizza,,,,
                    5a1,Package the Pizza,,,,
                    5b1,Assign the Delivery,,,yes,
                    6,Deliver the Pizza,,,,
                    7,Receive Payment,,,,
                    8,,,,,yes

                    """
        },
        {
        "role": "user",
        "content": f"""Text:{text}, Participants:{participants}, SVO:{svo}, Gateway kewords:{gateway}"""
        }
    ],
    temperature=0.3,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

def update_process_info(csv, text, participants, svo, gateway):
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with csv file with spreadsheet representatiom of buisness process model, text, particpants, SVOs and gateway kewords. Based on those informations generate a csv with columns: Order,Activity,Condition,Who,Subprocess,Terminated. 
                    Start always with: 0,start,,,,. If there is a split for branches (gateway) from for example Order number 1, then next acctivieties have Order 2a, 2b... 
                    (if we have for example 1 then we later can not have 1a or 1b etc.) . 
                    The values ​​in the Orders column should be increasing.
                    In this branch next activity will have Order 2b2, if again there will be a gateway, then we will have Orders 2b2a and 2b2b. Activity could be also 'goto 2b3'. 
                    If there is no following Activity after some Activity then last Activity should be terminated ('yes'), if after for example 4a and 4b there is 5, and 4b activtes do not have some continuation, 
                    then the shoud be terminated. Not all places in the table need to be filled.
                    Try not to use participants/who in Activity names. Return result in csv format.
                    Make sure that in column Termineted or Subprocess the 'yes' is lowercase. If you have at the end diffrent branches, all should be terminted. 
                    Example two last 7a, 7b should be set 'yes' in Terminated column.
                    In who column there should be participants.

                    Example correct csv's, do it similar way:
                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,start,,,,
                    1,Validate Passenger Ticket & Identification,,Check In Counter,,
                    2a,Confirm Itinerary,Validity,,yes,
                    2b,Reject Passenger,else,,,yes
                    3,Ask Passenger for Prohibited Objects,,,,
                    4a,Remove Prohibited Objects,Prohibited Objects,,,
                    4b,goto 5,else,,,
                    5,Ask Passenger for Baggages,,,,
                    6,Weight Baggages,,,,
                    7,Calculate Additional Fees,,,,
                    8,Inform Passenger of Additional Fees,,,,
                    9,Collect Payment of Fees,,,,
                    10a,Generate and Print Boarding Pass,,,,
                    10b1,Generate and Print Baggage Tags,,,,
                    10b2,Identify and Move Baggages,,,,
                    11,"Hand out Boarding Pass, Ticket and Identification",,,,yes

                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,start,,,,
                    1,Receive Order,,,,
                    2a1,Fill Order,Accepted,,,
                    2a2a1,Send Invoice,,,,
                    2a2a2,Make Payment,,,,
                    2a2a3,Accept Payment,,,,
                    2a2b,Ship Order,,,,
                    2b,goto 3,Rejected,,,
                    3,Close Order,,,,yes

                    Order,Activity,Condition,Who,Subprocess,Terminated
                    0,Receive pizza order,,,,
                    1,Answer customer call,,,yes,
                    2,Assign the Order,,,,
                    3,Prepare the Pizza,,,,
                    4,Cook the Pizza,,,,
                    5a1,Package the Pizza,,,,
                    5b1,Assign the Delivery,,,yes,
                    6,Deliver the Pizza,,,,
                    7,Receive Payment,,,,
                    8,,,,,yes
        """
        },
        {
        "role": "user",
        "content": f"""CSV: {csv}, Text:{text}, Participants:{participants}, SVO:{svo}, Gateway kewords:{gateway}"""
        }
    ],
    temperature=0.3,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

