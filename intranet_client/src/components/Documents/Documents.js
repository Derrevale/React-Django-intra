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
                // créer une liste des catégories avec une propriété children vide
                const categories = data.map(c => ({...c, children: []}));

                // remplir les propriétés children avec les noms des enfants
                categories.forEach(category => {
                    if (category.children.length > 0) {
                        category.children = category.children.map(childName =>
                            categories.find(c => c.name === childName)
                        );
                    }
                });

                // mettre à jour l'état local avec les catégories modifiées
                setCategories(categories);
            })
            .catch(error => console.log(error));
    }, []);

    // groupCategoriesByParent permet de grouper les catégories par parent
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


    // renderTree permet de rendre un arbre à partir des catégories
    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id.toString()} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
        </TreeItem>
    );

    // Les catégories sont groupées par parent
    const groupedCategories = groupCategoriesByParent(categories);

    return (
        // Le composant TreeView permet de rendre l'arbre
        <Box sx={{height: 270, flexGrow: 1, maxWidth: 400, overflowY: 'auto'}}>
            <TreeView
                aria-label="controlled"
                defaultCollapseIcon={<ExpandMoreIcon/>}
                defaultExpandIcon={<ChevronRightIcon/>}
            >
                {/* Object.values permet de transformer l'objet en tableau */}
                {Object.values(groupedCategories).map((category) => renderTree(category))}
            </TreeView>
        </Box>
    );
}
