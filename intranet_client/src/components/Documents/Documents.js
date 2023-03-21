import React, {useState, useEffect} from 'react';
import Box from '@mui/material/Box';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

export default function ControlledTreeView() {
    // useState permet de stocker les données dans un état local
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8002/api/Document_Category/')
            .then(response => response.json())
            .then(data => {
                const categories = data.map(c => ({...c, children: []}));
                categories.forEach(category => {
                    if (category.children.length > 0) {
                        category.children = category.children.map(childName =>
                            categories.find(c => c.name === childName)
                        );
                    }
                });
                setCategories(categories);
            })
            .catch(error => console.log(error));
    }, []);

    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8002/api/Document/')
            .then(response => response.json())
            .then(data => setDocuments(data))
            .catch(error => console.log(error));
    }, []);

    const groupCategoriesByParent = (categories) => {
        const groupedCategories = {};
        categories.forEach((category) => {
            const parentId = category.parent;
            const categoryId = category.id;
            if (!categoryId) {
                console.error('No id property found for category:', category);
                return;
            }
            if (!groupedCategories[categoryId]) {
                groupedCategories[categoryId] = {...category, children: []};
            }
            if (parentId) {
                if (!groupedCategories[parentId]) {
                    console.error('No parent found for category:', category);
                    return;
                }
                groupedCategories[parentId].children.push(groupedCategories[categoryId]);
            }
        });
        return Object.values(groupedCategories).filter(category => !category.parent);
    };

    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id.toString()} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
            {Array.isArray(nodes.files) ? nodes.files.map((document) => (
                <TreeItem key={document.id} nodeId={document.id.toString()} label={document.name}/>
            )) : null}
        </TreeItem>
    );

    const groupedCategories = groupCategoriesByParent(categories);

// les fichiers sont regroupés par catégorie
    documents.forEach(document => {
        console.log(document);
        const category = categories.find(c => c.id === document.category);
        if (category) {
            if (!category.files) {
                category.files = [];
            }
            category.files.push(document);
        }
    });

    return (
        <Box sx={{height: 270, flexGrow: 1, maxWidth: 400, overflowY: 'auto'}}>
            <TreeView
                aria-label="controlled"
                defaultCollapseIcon={<ExpandMoreIcon/>}
                defaultExpandIcon={<ChevronRightIcon/>}
            >
                {Object.values(groupedCategories).map((category) => renderTree(category))}
            </TreeView>
        </Box>
    );
}