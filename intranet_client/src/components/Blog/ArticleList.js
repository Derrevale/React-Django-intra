import React, { useState, useEffect, useContext } from "react";
import "../../styles/ArticleList.css";
import "../../styles/bootstrap.min.css";
import { LanguageContext } from '../../services/LanguageContext'; // Ajustez le chemin selon votre structure de dossier

function ArticleList() {
  const { language } = useContext(LanguageContext);
  const [articles, setArticles] = useState([]);
  const [filteredArticles, setFilteredArticles] = useState([]);
  const [page, setPage] = useState(1);
  const articlesPerPage = 12;
  const totalPages = Math.ceil(articles.count / articlesPerPage);

  useEffect(() => {
    fetch(`http://localhost:8002/api/blog/articles/?page=${page}`)
      .then((response) => response.json())
      .then((data) => {
        setArticles(data);
      })
      .catch((error) => console.log(error));
  }, [page]);

  useEffect(() => {
    if (articles.results) {
      if (language) {
        setFilteredArticles(articles.results.filter(article => article.language === language));
      } else {
        setFilteredArticles(articles.results);
      }
    }
  }, [language, articles]);

  const pages = [];
  for (let i = Math.max(1, page - 2); i <= Math.min(page + 2, totalPages); i++) {
    pages.push(i);
  }

  return (
    <div>
      <section className="row row-1 cols-3">
        {filteredArticles &&
          filteredArticles.map((article) => (
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
                  <div dangerouslySetInnerHTML={{ __html: article.intro }}></div>
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
