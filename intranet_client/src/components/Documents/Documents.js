import React, {useState, useEffect} from 'react';
import {TreeView, TreeItem} from '@mui/lab';
import {Typography} from '@mui/material';
import DocumentsList from './DocumentsList';

const Documents = () => {
    const [categories, setCategories] = useState([]);
    const [selectedCategoryId, setSelectedCategoryId] = useState(null);

    useEffect(() => {
        const fetchCategories = async () => {
            const response = await fetch('http://localhost:8002/api/Document_Category/');
            const data = await response.json();
            setCategories(data);
        };
        fetchCategories();
    }, []);

    const getCategoryChildren = (categoryId) => {
        return categories.filter((category) => category.parent === categoryId);
    };

    const renderTree = (category) => {
        const categoryChildren = getCategoryChildren(category.id);

        return (
            <TreeItem key={category.id} nodeId={category.id.toString()} label={category.name}
                      onClick={() => setSelectedCategoryId(category.id)}>
                {categoryChildren.map((childCategory) => renderTree(childCategory))}
                {selectedCategoryId === category.id && (
                    <DocumentsList categoryId={category.id}/>
                )}
            </TreeItem>
        );
    };

    return (
        <TreeView
            defaultCollapseIcon={<Typography variant="body2">-</Typography>}
            defaultExpandIcon={<Typography variant="body2">+</Typography>}
        >
            {categories.map((category) => {
                if (category.parent === null) {
                    return renderTree(category);
                }
                return null;
            })}
        </TreeView>
    );
};

export default Documents;
