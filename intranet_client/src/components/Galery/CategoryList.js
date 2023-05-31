import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Grid, Card, CardActionArea, CardMedia, CardContent, Typography } from '@mui/material';
import '../../styles/Galerie/CategoryList.css';

const CategoryList = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await axios.get('http://localhost:8002/api/Galerie Categorie/');
        setCategories(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération des catégories:', error);
      }
    };

    fetchCategories();
  }, []);

  // Filtrer les catégories sans parent (parent_category === null)
  const noParentCategories = categories.filter(category => category.parent_category === null);

  return (
    <Grid container spacing={4} className="CategoryList">
      {noParentCategories.map((category) => (
        <Grid item key={category.id} xs={12} sm={6} md={4} className="CategoryList2">
          <Link to={`/Galerie/${category.id}`} style={{ textDecoration: 'none' }}>
            <Card className="CategoryList3">
              <CardActionArea className="CategoryList4">
                {category.image && (
                  <CardMedia
                    component="img"
                    alt={category.name}
                    image={category.image}
                    className="Img_Cadre"
                  />
                )}
                <CardContent>
                  <Typography gutterBottom variant="h5" component="div">
                    {category.name}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Link>
        </Grid>
      ))}
    </Grid>
  );
};

export default CategoryList;
