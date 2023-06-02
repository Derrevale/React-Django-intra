import React, {useState, useEffect} from "react";
import '../../styles/ArticleList.css';

function ArticleList() {
    const [articles, setArticles] = useState([]);
    const [page, setPage] = useState(1);
    const [totalPages, setTotalPages] = useState(0);
    const articlesPerPage = 12; // Nombre d'articles par page

    useEffect(() => {
        fetch(`http://localhost:8002/api/Blog Article/?page=${page}`)
            .then((response) => response.json())
            .then((data) => {
                setArticles(data.results);
                setTotalPages(Math.ceil(data.count / articlesPerPage)); // Calcul du nombre total de pages en prenant en compte les articles par page
            })
            .catch((error) => console.log(error));
    }, [page]);

    const pages = [];
    for (let i = Math.max(1, page - 2); i <= Math.min(page + 2, totalPages); i++) {
        pages.push(i);
    }

    return (
        <div>
            <section className="row row-1 cols-3">
                {articles &&
                    articles.map((article) => (
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
                                    <a className="readmore" href={`/articles/${article.id}`}>
                                        Lire la suite...
                                    </a>
                                </div>
                            </div>
                        </div>
                    ))}
            </section>

            <div className="pagination">
                <span className="pagenumber">page {page} sur {totalPages}</span>
                <div className="pagination-buttons">
                    <button onClick={() => setPage(1)} disabled={page === 1}>{"<<"}</button>
                    <button onClick={() => setPage(Math.max(1, page - 1))} disabled={page === 1}>{"<"}</button>
                    {pages.map((number) => (
                        <button
                            key={number}
                            onClick={() => setPage(number)}
                            className={number === page ? 'active' : ''}
                            style={{display: number > totalPages ? 'none' : 'inline-block'}}
                        >
                            {number}
                        </button>
                    ))}
                    <button onClick={() => setPage(Math.min(page + 1, totalPages))}
                            disabled={page === totalPages || totalPages === 0}>{">"}</button>
                    <button onClick={() => setPage(totalPages)}
                            disabled={page === totalPages || totalPages === 0}>{">>"}</button>
                </div>
            </div>

        </div>
    );
}

export default ArticleList;
