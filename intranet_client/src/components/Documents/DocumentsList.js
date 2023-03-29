import React, {useState, useEffect} from "react";
import axios from "axios";

const DocumentsList = () => {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8002/api/Document/").then((response) => {
            setDocuments(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Liste des documents</h2>
            <ul>
                {documents.map((document) => (
                    <li key={document.id}>
                        {document.name} - {document.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DocumentsList;
