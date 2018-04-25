RequestID: 4de49920-32d5-11e8-950e-c1139b0742a3
{
  "dialogState": "ElicitSlot",
  "intentName": "MakeAppointmentQuery",
  "message": "What Appointment Type did you schedule for?",
  "messageFormat": "PlainText",
  "responseCard": {
    "contentType": "application/vnd.amazonaws.card.generic",
    "genericAttachments": [
      {
        "attachmentLinkUrl": null,
        "buttons": [
          {
            "text": "AWS",
            "value": "AWS"
          },
          {
            "text": "IoT",
            "value": "IoT"
          },
          {
            "text": "General Inquiry",
            "value": "General"
          }
        ],
        "imageUrl": null,
        "subTitle": "Do you know your appointment type? ",
        "title": "Appointment Type"
      }
    ],
    "version": "1"
  },
  "sessionAttributes": {},
  "slotToElicit": "ApptType",
  "slots": {
    "ApptType": null
  }
}