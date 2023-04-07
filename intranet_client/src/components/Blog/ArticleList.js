import React, {useState, useEffect} from "react";
import '../../styles/ArticleList.css';

function ArticleList() {
    const [articles, setArticles] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8002/api/Blog Article/")
            .then((response) => response.json())
            .then((data) => setArticles(data))
            .catch((error) => console.log(error));
    }, []);

    return (
        <section className="row row-1 cols-3">
            {articles.map((article) => (
                <div className="col-lg-4" key={article.id}>
                    <div className="articleList-item">
                        {article.header_image && (
                            <img
                                src={article.header_image}
                                alt={article.title}
                                className="articleList-img"
                            />
                        )}
                        <div className="article-header">
                            <h2 className="articlelist-title">{article.title}</h2>
                        </div>
                        <div className="article-content">
                            <div dangerouslySetInnerHTML={{__html: article.intro}}></div>
                            <a href={`/articles/${article.id}`}>Lire la suite...</a>
                        </div>
                    </div>
                </div>
            ))}
        </section>
    );
}

export default ArticleList;
