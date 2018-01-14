from client.es import EsClient
from client.chatwork import ChatWorkClient
from model.ticket import Ticket
from util.message import Message

# constant
MY_ACCOUNT = chatwork_account_id
ROOM_ID = 'your_room_id'


def lambda_handler(event, context):

    message_id = event['webhook_event']['message_id']
    reply_account = event['webhook_event']['account_id']
    keyword = event['webhook_event']['body']

    if reply_account == MY_ACCOUNT:
        return print('No New Messages')

    es_client = EsClient()
    response = es_client.get_document_and(keyword)

    tickets = []

    for ticket_record in response['hits']['hits']:
        ticket = Ticket(ticket_record)
        tickets.append(ticket)

    message = Message.get_message_body(message_id, reply_account, tickets, ROOM_ID)
    response = ChatWorkClient.post_messages(message, ROOM_ID)

    print(response)
