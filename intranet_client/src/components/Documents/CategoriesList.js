import React, {useState, useEffect} from "react";
import axios from "axios";

const CategoriesList = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8002/api/Document_Category/").then((response) => {
            setCategories(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Liste des catégories</h2>
            <ul>
                {categories.map((category) => (
                    <li key={category.id}>{category.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default CategoriesList;
