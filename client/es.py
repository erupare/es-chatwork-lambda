from elasticsearch import Elasticsearch, RequestsHttpConnection


class EsClient(object):

    def __init__(self):

        self.es = Elasticsearch(
            hosts=[
                {
                    'host': 'your_host',
                    'port': 443
                }
            ],
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        return

    def get_document_and(self, keyword):

        must_keywords = []

        keywords = keyword.split()

        for keyword in keywords:
            must_keyword = {
                "match": {"comment.body": keyword}
            }

            must_keywords.append(must_keyword)

        search_query = {
            "query":
                {
                    "bool":
                        {
                            "must": [
                                must_keywords
                            ]
                        }
                },
            "_source":
                [
                    "subject",
                    "url"
                ]
        }

        response = self.es.search(index="zendesk", body=search_query)

        return response
