import React, {useState, useEffect} from "react";
import {useParams} from "react-router-dom";


function Article({match}) {
    const [article, setArticle] = useState({});
    const params = useParams();

    useEffect(() => {
        fetch(`http://localhost:8002/api/Blog Article/${params.id}/`)
            .then((response) => response.json())
            .then((data) => setArticle(data))
            .catch((error) => console.log(error));
    }, [params.id]);

    return (
        <section className="Article">
            <div className="article-header">
                <p className="article-title">{article.title}</p>
            </div>
            {article.header_image && (
                <img
                    src={article.header_image}
                    alt={article.title}
                    className="article-img"
                />
            )}
            <div className="article-content">
                <div dangerouslySetInnerHTML={{__html: article.intro}}></div>
                <div dangerouslySetInnerHTML={{__html: article.content}}></div>
            </div>
        </section>
    );
}

export default Article;
