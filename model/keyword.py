class Keyword(object):

    def __init__(self, keyword):

        self.keyword = keyword

    def get_keyword(self):

        must_keywords = []

        keywords = self.keyword.split()

        for keyword in keywords:

            must_keyword = {
                "match": {"comment.body": keyword}
            }

            must_keywords.append(must_keyword)

        return must_keywords
