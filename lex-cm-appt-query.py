from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

import json
import dateutil.parser
import datetime
import time
import os
import math
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) #The log level identifies the type of log, such as [INFO], [ERROR], and [DEBUG].

def my_logging_handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('something went wrong')
    return 'Hello from Lambda!'  

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamoTable = dynamodb.Table('ApptBotTime')
# print("print Table")

# def queryDB(userId):
#     # dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
#     # dynamoTable = dynamodb.Table('ApptBot')

#     # userId = 'John'

# # response = table.query(
# #     KeyConditionExpression=Key('UID').eq(1)
# # )

# # for i in response['Items']:
# # #     print(i['Date'], ":", i['title'])
# # # for i in response['Items']:
# #     print(json.dumps(i, cls=DecimalEncoder))

#     response = dynamoTable.get_item(
#         Key={
#             # 'ApptID': 'AWS2018-03-2816:00'
#             'UID' : userId
#         }
#     )

#     # item = response['Item']
#     # print(item)
#     print(response)


""" --- Helper Functions --- """


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)



def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def try_ex(func):
    """
    Call passed in function in try block. If KeyError is encountered return None.
    This function is intended to be used to safely access dictionary.

    Note that this function would have negative impact on performance.
    """

    try:
        return func()
    except KeyError:
        return None


""" --- Functions that control the bot's behavior --- """


def check_appointment(intent_request):
    """
    Performs dialog management and fulfillment for booking a dentists appointment.

    Beyond fulfillment, the implementation for this intent demonstrates the following:
    1) Use of elicitSlot in slot validation and re-prompting
    2) Use of confirmIntent to support the confirmation of inferred slot values, when confirmation is required
    on the bot model and the inferred slot values fully specify the intent.
    """
    appointment_type = intent_request['currentIntent']['slots']['AppointmentType']
    # date = intent_request['currentIntent']['slots']['Date']
    # appointment_time = intent_request['currentIntent']['slots']['Time']
    # source = intent_request['invocationSource']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request[
                                                                           'sessionAttributes'] is not None else {}
    userId = 'Jason'  # intent_request['userId']

    try:
        response = dynamoTable.get_item(
            Key={
                # 'UID' : userId                ### Apptbot key UID
                'ApptID': userId                ### Apptbottime key ApptID
            }
        )

    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:

        # dumps the json object into an element
        json_str = json.dumps(response)
    
        # load the json to a string
        Js_response = json.loads(json_str)
    
        Appointment_date = Js_response['Item']['ApptDate']
        Appointment_time = Js_response['Item']['ApptTime']
        appointment_type = Js_response['Item']['ApptType']
        # print('Your {} appointment is on {} at {}'.format(Appointment_type,Appointment_date,Appointment_time))
        print(json.dumps(response, indent=4, cls=DecimalEncoder))
        print('Your {} appointment is on {} at {}.'.format(Js_response['Item']['ApptType'], Js_response['Item']['ApptDate'],
                                                           Js_response['Item']['ApptTime']))
    
        return close(
            output_session_attributes,
            'Fulfilled',
            {
                'contentType': 'PlainText',
                # 'content': 'Okay, I have booked your appointment.  We will see you at {} on {}'.format(build_time_output_string(appointment_time), date)
                'content': 'Your {} appointment is on {} at {}'.format(Js_response['Item']['ApptType'], Js_response['Item']['ApptDate'],Js_response['Item']['ApptTime'])
            }
        )

    # if source == 'DialogCodeHook':
    #     # Perform basic validation on the supplied input slots.
    #     slots = intent_request['currentIntent']['slots']
    #     validation_result = validate_book_appointment(appointment_type, date, appointment_time)
    #     if not validation_result['isValid']:
    #         slots[validation_result['violatedSlot']] = None
    #         return elicit_slot(
    #             output_session_attributes,
    #             intent_request['currentIntent']['name'],
    #             slots,
    #             validation_result['violatedSlot'],
    #             validation_result['message'],
    #             build_response_card(
    #                 'Specify {}'.format(validation_result['violatedSlot']),
    #                 validation_result['message']['content'],
    #                 build_options(validation_result['violatedSlot'], appointment_type, date, booking_map)
    #             )
    #         )
    #
    #     if not appointment_type:
    #         return elicit_slot(
    #             output_session_attributes,
    #             intent_request['currentIntent']['name'],
    #             intent_request['currentIntent']['slots'],
    #             'AppointmentType',
    #             {'contentType': 'PlainText', 'content': 'What type of appointment would you like to schedule?'},
    #             build_response_card(
    #                 'Specify Appointment Type', 'What type of appointment would you like to schedule?',
    #                 build_options('AppointmentType', appointment_type, date, None)
    #             )
    #         )
    #
    #     if appointment_type and not date:
    #         return elicit_slot(
    #             output_session_attributes,
    #             intent_request['currentIntent']['name'],
    #             intent_request['currentIntent']['slots'],
    #             'Date',
    #             {'contentType': 'PlainText',
    #              'content': 'When would you like to schedule your {}?'.format(appointment_type)},
    #             build_response_card(
    #                 'Specify Date',
    #                 'When would you like to schedule your {}?'.format(appointment_type),
    #                 build_options('Date', appointment_type, date, None)
    #             )
    #         )
    #
    #     updateDB(
    #         appointment_time,
    #         date,
    #         appointment_type,
    #         userId
    # #     )  # SL
    #
    # else:
    #     # This is not treated as an error as this code sample supports functionality either as fulfillment or dialog code hook.
    #     logger.debug('Availabilities for {} were null at fulfillment time.  '
    #                  'This should have been initialized if this function was configured as the dialog code hook'.format(
    #         date))
    #
    # return close(
    #     output_session_attributes,
    #     'Fulfilled',
    #     {
    #         'contentType': 'PlainText',
    #         'content': 'Okay, I have booked your appointment.  We will see you at {} on {}'.format(
    #             build_time_output_string(appointment_time), date)
    #     }
    # )
    #


#####


""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug(
        'dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    # SL
    if intent_name == 'MakeAppointmentQuery':
        return check_appointment(intent_request)
    # if intent_name == 'MakeAppointment':
    #     return make_appointment(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('[DEBUG] QUERY |||||')
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    logger.debug(event)
    return dispatch(event)
