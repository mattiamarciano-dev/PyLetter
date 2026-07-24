from Article import Article

class ContentFormatter:
    @staticmethod
    def get_formatted_content(article: Article, index: int) -> str:
        return f"""
                <h2>{index + 1}.{article.title}</h2>
                <b>Source:</b> {article.source}<br><br>
                <img src="{article.img_url}" style="max-width:600px; width:100%; 
                height:auto; border-radius:8px;"><br>
                <p>{article.content}</p>
                <p><b>Url: </b>{article.url}</p>
                <hr>
                """
