import React, {useState, useEffect} from "react";
import axios from "axios";
import TreeView from '@mui/lab/TreeView';
import TreeItem from '@mui/lab/TreeItem';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const Documents = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8002/api/Document_Category/").then((response) => {
      setCategories(response.data);
    });
  }, []);

  const buildTree = (categories, parent) => {
    return categories
      .filter((category) => category.parent === parent)
      .map((category) => ({
        id: category.id,
        name: category.name,
        children: buildTree(categories, category.id),
      }));
  };

  const tree = buildTree(categories, null);

  const renderTree = (nodes) => (
    <TreeItem key={nodes.id} nodeId={nodes.id.toString()} label={nodes.name}>
      {Array.isArray(nodes.children)
        ? nodes.children.map((node) => renderTree(node))
        : null}
    </TreeItem>
  );

  return (
    <TreeView
      defaultCollapseIcon={<ExpandMoreIcon />}
      defaultExpandIcon={<ChevronRightIcon />}
    >
      {tree.map((node) => renderTree(node))}
    </TreeView>
  );
};

export default Documents;
