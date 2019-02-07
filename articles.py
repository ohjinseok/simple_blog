# object
class Article:
    def __init__(self, id, title, content, author, created_at):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at
        
a1 = Article(1, '제목', '내용', '오진석', '2019-02-07')
a2 = Article(2, '제목2', '내용2', '오진석2', '2019-02-07')

articles3 = [
    a1, a2
]

# list
# articles[0][1]

# dict
# articles[0]['title']

#obj
articles3[0].title