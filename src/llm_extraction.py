import openai
from openai import OpenAI

def extract_process_info(text):
    client = OpenAI(api_key='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')

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
        "content": f"""A customer brings in a defective computer and the
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
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )
    return response.choices[0].message.content

print(extract_process_info('ok'))