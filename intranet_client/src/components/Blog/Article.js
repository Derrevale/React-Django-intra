import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { fetchArticle } from '../../services/Api'; // Importer la fonction depuis Api.js

function Article() {
    const [article, setArticle] = useState({}); // État pour stocker l'article
    const params = useParams(); // Obtenir les paramètres d'URL (ID de l'article)

    // Utiliser l'effet pour récupérer l'article lors du montage du composant
    useEffect(() => {
        const getArticle = async () => {
            // Appeler la fonction fetchArticle depuis Api.js
            const result = await fetchArticle(params.id);
            if (result.success) {
                // Mettre à jour l'état avec les données de l'article récupérées
                setArticle(result.article);
            }
        };

        // Appeler la fonction asynchrone
        getArticle();
    }, [params.id]); // Réexécuter l'effet si l'ID de l'article change

    return (
        <section className="Article">
            <div className="article-header">
                <p className="article-title">{article.title}</p>
            </div>
            {article.header_image && (
                // Afficher l'image de l'en-tête si elle existe
                <img
                    src={article.header_image}
                    alt={article.title}
                    className="article-img"
                />
            )}
            <div className="article-content">
                {/* Utiliser dangerouslySetInnerHTML pour insérer le HTML de l'introduction et du contenu */}
                <div dangerouslySetInnerHTML={{ __html: article.intro }}></div>
                <div dangerouslySetInnerHTML={{ __html: article.content }}></div>
            </div>
        </section>
    );
}

export default Article;
