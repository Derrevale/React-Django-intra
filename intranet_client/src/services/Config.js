// URL de base pour l'API - peut être modifiée pour différents environnements (développement, production, etc.)
const BASE_URL = "http://localhost:8002/";

const config = {
    // Endpoint général pour l'API
    API_ENDPOINT: BASE_URL + "api",

    // Endpoint pour la recherche, si différent de l'endpoint général de l'API
    SEARCH_ENDPOINT: BASE_URL,

    // Endpoint pour récupérer les calendriers des événements
    EVENT_CALENDAR_ENDPOINT: BASE_URL + "api/event/calendar/",

    // Endpoint pour récupérer les événements
    EVENT_EVENTS_ENDPOINT: BASE_URL + "api/event/events/",

    // Endpoint pour récupérer les catégories de fichiers
    FILE_CATEGORIES_ENDPOINT: BASE_URL + "api/file/categories/",

    // Endpoint pour récupérer les fichiers
    FILE_FILES_ENDPOINT: BASE_URL + "api/file/files/",

    // Endpoint pour récupérer les catégories de la galerie
    GALLERY_CATEGORIES_ENDPOINT: BASE_URL + "api/gallery/categories/",

    // Endpoint pour récupérer les images de la galerie
    GALLERY_IMAGES_ENDPOINT: BASE_URL + "api/gallery/images/",

    // Endpoint pour la connexion (obtention d'un token)
    LOGIN_ENDPOINT: BASE_URL + "api/token/",
};

// Exportation de l'objet config pour être utilisé dans d'autres parties de l'application
export default config;
