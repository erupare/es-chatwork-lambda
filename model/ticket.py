class Ticket(object):

    def __init__(self, ticket):
        self.subject = ticket['_source']['subject']
        self.url = ticket['_source']['url']

    def __repr__(self):
        return "%s, %s \n" % (self.subject, self.url)
