import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const Documents = () => {
  const [data, setData] = useState([]);

  const buildHierarchy = (items) => {
    const itemMap = new Map();
    items.forEach((item) => itemMap.set(item.id, { ...item, children: [] }));
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

  const renderTree = (nodes) =>
    nodes.map((node) => (
      <TreeItem key={node.id} nodeId={node.id.toString()} label={node.name}>
        {node.children.length > 0 && renderTree(node.children)}
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
    ));

  return (
    <TreeView defaultCollapseIcon={<ExpandMoreIcon />} defaultExpandIcon={<ChevronRightIcon />}>
      {renderTree(data)}
    </TreeView>
  );
};

export default Documents;
