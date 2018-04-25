RequestID: a5d2c820 - 32d4 - 11e8 - b3c3 - 19b4ee5f9180
{
    "dialogState": "ElicitSlot",
    "intentName": "MakeAppointment",
    "message": "What type of appointment would you like to schedule?",
    "messageFormat": "PlainText",
    "responseCard": {
        "contentType": "application/vnd.amazonaws.card.generic",
        "genericAttachments": [
            {
                "attachmentLinkUrl": null,
                "buttons": [
                    {
                        "text": "General",
                        "value": "General"
                    },
                    {
                        "text": "AWS",
                        "value": "AWS"
                    },
                    {
                        "text": "IoT",
                        "value": "IoT"
                    }
                ],
                "imageUrl": null,
                "subTitle": "What type of appointment would you like to schedule?",
                "title": "Specify Appointment Type"
            }
        ],
        "version": "1"
    },
    "sessionAttributes": {},
    "slotToElicit": "AppointmentType",
    "slots": {
        "AppointmentType": null,
        "Date": null,
        "Time": null
    }

RequestID: 86a1498c-32d5-11e8-b3c3-19b4ee5f9180
{
  "dialogState": "ElicitSlot",
  "intentName": "MakeAppointment",
  "message": "When would you like to schedule your aws appointment ?",
  "messageFormat": "PlainText",
  "responseCard": {
    "contentType": "application/vnd.amazonaws.card.generic",
    "genericAttachments": [
      {
        "attachmentLinkUrl": null,
        "buttons": [
          {
            "text": "3-29 (Thu)",
            "value": "Thursday, March 29, 2018"
          },
          {
            "text": "3-30 (Fri)",
            "value": "Friday, March 30, 2018"
          },
          {
            "text": "4-2 (Mon)",
            "value": "Monday, April 02, 2018"
          },
          {
            "text": "4-3 (Tue)",
            "value": "Tuesday, April 03, 2018"
          },
          {
            "text": "4-4 (Wed)",
            "value": "Wednesday, April 04, 2018"
          }
        ],
        "imageUrl": null,
        "subTitle": "When would you like to schedule your aws appointment?",
        "title": "Specify Date"
      }
    ],
    "version": "1"
  },
  "sessionAttributes": {},
  "slotToElicit": "Date",
  "slots": {
    "AppointmentType": "aws",
    "Date": null,
    "Time": null
  }
}