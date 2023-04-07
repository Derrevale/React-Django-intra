import React, {useState, useEffect} from 'react';
import axios from 'axios';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import "../../styles/Documents/Document.css";

const Documents = () => {
    const [data, setData] = useState([]);

    const buildHierarchy = (items) => {
        const itemMap = new Map();
        items.forEach((item) => itemMap.set(item.id, {...item, children: []}));
        const result = [];

        for (const item of itemMap.values()) {
            if (item.parent) {
                const parent = itemMap.get(item.parent.id);
                parent.children.push(item);
            } else {
                result.push(item);
            }
        }

        return result;
    };

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios('http://localhost:8002/api/FileManager Categorie/');
            const hierarchy = buildHierarchy(result.data);
            setData(hierarchy);
        };
        fetchData();
    }, []);

    const renderTree = (nodes, isChild = false) =>
        nodes.map((node) => (
            <TreeItem
                key={node.id}
                nodeId={node.id.toString()}
                label={node.name}
                sx={isChild ? {ml: 2} : {}}
            >
                {Array.isArray(node.files) &&
                    node.files.map((file) => (
                        <TreeItem
                            key={file.name}
                            nodeId={file.name}
                            label={
                                <a
                                    href={`http://localhost:8002${file.fileUrl}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    {file.name}
                                </a>
                            }
                        />
                    ))}
                {node.children.length > 0 && renderTree(node.children, true)}
            </TreeItem>
        ));

    return (
        <div className="test" style={{margin: '2%', padding: '1%',width:'75%'}}>
            <TreeView defaultCollapseIcon={<ExpandMoreIcon/>} defaultExpandIcon={<ChevronRightIcon/>}>
                {renderTree(data)}
            </TreeView>
        </div>
    );
};

export default Documents;

