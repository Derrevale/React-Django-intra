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


