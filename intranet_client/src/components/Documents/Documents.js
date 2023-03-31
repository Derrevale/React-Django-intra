import React, {useState, useEffect} from "react";
import axios from "axios";
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const Documents = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios("http://localhost:8002/api/Document_Category/");
            setData(result.data);
        };
        fetchData();
    }, []);

    const renderTree = (nodes) =>
        nodes.map((node) => (
            <React.Fragment>
                {console.log("node:--------avant-----------")}
                {console.log(node)}
                {console.log("----------après---------")}
                {node.id && (
                    <TreeItem key={node.name} nodeId={node.name} label={node.name}>
                        {Array.isArray(node.children) && node.children.length > 0 && (
                            <React.Fragment>{renderTree(node.children)}</React.Fragment>
                        )}
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
                    </TreeItem>
                )}
            </React.Fragment>
        ));

    return (
        <TreeView
            defaultCollapseIcon={<ExpandMoreIcon/>}
            defaultExpandIcon={<ChevronRightIcon/>}
        >
            {renderTree(data)}
        </TreeView>
    );
};

export default Documents;
