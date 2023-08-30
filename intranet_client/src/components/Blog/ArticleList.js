import React, {useState, useEffect} from "react";
import "../../styles/ArticleList.css";
import "../../styles/bootstrap.min.css";

function ArticleList() {
    const [articles, setArticles] = useState([]);
    const [page, setPage] = useState(1);
    const articlesPerPage = 12; // Nombre d'articles par page
    const totalPages = Math.ceil(articles.count / articlesPerPage);

    useEffect(() => {
        fetch(`http://localhost:8002/api/blog/articles/?page=${page}`)
            .then((response) => response.json())
            .then((data) => {
                setArticles(data); // Utiliser les données directement
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
                {articles.results &&
                    articles.results.map((article) => (
                        <div className="col-lg-4" key={article.slug}>
                            <div className="articleList-item">
                                {article.header_image && (
                                    <img
                                        src={`http://localhost:8002${article.header_image}`}
                                        alt={article.title}
                                        className="articleList-img"
                                    />
                                )}
                                <div className="article-header">
                                    <h2 className="articlelist-title">{article.title}</h2>
                                </div>
                                <div className="article-content">
                                    <div dangerouslySetInnerHTML={{__html: article.intro}}></div>
                                    <a className="readmore" href={`/articles/${article.slug}`}>
                                        Lire la suite...
                                    </a>
                                </div>
                            </div>
                        </div>
                    ))}
            </section>

            <div className="pagination">
        <span className="pagenumber">
          page {page} sur {totalPages}
        </span>
                <div className="pagination-buttons">
                    <button className={`btn btn-outline-primary btn-rounded`} onClick={() => setPage(1)} disabled={page === 1}>
                        {"<<"}
                    </button>
                    <button  className={`btn btn-outline-primary btn-rounded`} onClick={() => setPage(Math.max(1, page - 1))} disabled={page === 1}>
                        {"<"}
                    </button>
                    {pages.map((number) => (
                        <button
                            key={number}
                            onClick={() => setPage(number)}
                            className={`btn btn-primary btn-rounded ${number === page ? "active" : ""}`}
                            style={{display: number > totalPages ? "none" : "inline-block"}}
                        >
                            {number}
                        </button>
                    ))}
                    <button className={`btn btn-outline-primary btn-rounded`} onClick={() => setPage(Math.min(page + 1, totalPages))}
                            disabled={page === totalPages || totalPages === 0}>
                        {">"}
                    </button>
                    <button className={`btn btn-outline-primary btn-rounded`} onClick={() => setPage(totalPages)} disabled={page === totalPages || totalPages === 0}>
                        {">>"}
                    </button>
                </div>
            </div>
        </div>
    );
}

export default ArticleList;
