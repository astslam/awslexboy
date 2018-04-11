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

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamoTable = dynamodb.Table('ApptBotTime')


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


def delete_appointment(intent_request):
    """
    Performs dialog management and fulfillment for booking a dentists appointment.

    Beyond fulfillment, the implementation for this intent demonstrates the following:
    1) Use of elicitSlot in slot validation and re-prompting
    2) Use of confirmIntent to support the confirmation of inferred slot values, when confirmation is required
    on the bot model and the inferred slot values fully specify the intent.
    """
    # appointment_type = intent_request['currentIntent']['slots']['AppointmentType']
    output_session_attributes = intent_request['sessionAttributes'] if intent_request[
                                                                           'sessionAttributes'] is not None else {}
    booking_map = json.loads(try_ex(lambda: output_session_attributes['bookingMap']) or '{}')
    intendID = intent_request['userId']
    if intendID is not None:
        userId = intent_request['userId']
        
        try:
            response = dynamoTable.delete_item(
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
    
            print('[DEBUG]' )
            print(json.dumps(response, indent=4, cls=DecimalEncoder))
            
            print('Your appointment is cancelled.')
            print(booking_map)
        
            # return appointment information
            return close(
                output_session_attributes,
                'Fulfilled',
                {
                    'contentType': 'PlainText',
                    'content': 'Your appointment is canceled.'
                }
            )
    else: 
        return close(
            output_session_attributes,
            'Fulfilled',
            {
                'contentType': 'PlainText',
                'content': 'We cannot find your appointment. Please book a new appointment. '
            }
        )
         

""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug(
        'dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'MakeAppointmentCancel':
        return delete_appointment(intent_request)
    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # Changed time zone to Vancouver, Candad
    os.environ['TZ'] = 'America/Vancouver' 
    time.tzset()
    logger.debug('[DEBUG] CANCEL |||||')
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    logger.debug(event)
    return dispatch(event)
