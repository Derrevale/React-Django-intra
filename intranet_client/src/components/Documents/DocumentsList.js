import React, { useState, useEffect } from 'react';

const DocumentsList = ({ categoryId }) => {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    const fetchDocuments = async () => {
      const response = await fetch(`http://localhost:8002/api/Document/?categoryId=${categoryId}`);
      const data = await response.json();
      setDocuments(data);
    };
    fetchDocuments();
  }, [categoryId]);

  return (
    <div>
      {documents.map((document) => (
        <div key={document.id}>
          <p>{document.name}</p>
          <a href={document.fileUrl}>Télécharger</a>
        </div>
      ))}
    </div>
  );
};

export default DocumentsList;
