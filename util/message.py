class Message(object):

    @staticmethod
    def get_message_body(message_id, reply_account, tickets, room_id):

        body = ''

        if not tickets:

            message = f'[rp aid={reply_account} to={room_id}-{message_id}]' + \
                      f'[info][title]Search Results(Sort by highest score)[/title]' + \
                      f'There is no result.[/info]'

            return message

        for ticket in tickets:

            body += ticket.subject + '\n' + ticket.url + '\n'

        message = f'[rp aid={reply_account} to={room_id}-{message_id}]' + \
            f'[info][title]Search Results(Sort by highest score)[/title]' + \
            f'{body}[/info]'

        return message
