import axios from 'axios';
import config from './Config.js'; // Importer le fichier config pour accéder aux endpoints

// Fonction pour gérer la connexion de l'utilisateur
export const login = async (username, password) => {
    try {
        // Utiliser l'endpoint de connexion depuis config.js
        const response = await axios.post(config.LOGIN_ENDPOINT, {
            username: username,
            password: password,
        });

        // Stocker les tokens d'accès et de rafraîchissement dans le local storage
        localStorage.setItem('access', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);

        // Définir le header d'autorisation par défaut pour les futures requêtes
        axios.defaults.headers['Authorization'] = 'Bearer ' + localStorage.getItem('access');

        // Retourner un succès si la connexion est réussie
        return { success: true };
    } catch (error) {
        // Retourner une erreur si la connexion échoue
        return { success: false, error: 'Invalid username or password' };
    }
};

export const fetchArticle = async (id) => {
    try {
        // Construire l'URL en utilisant l'ID et l'endpoint configuré dans Config.js
        const response = await fetch(`${config.API_ENDPOINT}/blog/articles/${id}/`);

        // Convertir la réponse en JSON
        const data = await response.json();

        // Retourner l'article et un indicateur de succès
        return { success: true, article: data };
    } catch (error) {
        // Gérer les erreurs en les loguant et en retournant un indicateur d'échec
        console.log(error);
        return { success: false, error };
    }
};

// Fonction pour récupérer la liste des articles du blog
export const fetchBlogArticles = async () => {
    try {
        const response = await fetch('http://localhost:8002/api/blog/articles/');
        const data = await response.json();
        return { success: true, articles: data };
    } catch (error) {
        console.log(error);
        return { success: false, error };
    }
};


