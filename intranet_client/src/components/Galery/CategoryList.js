import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Grid, Card, CardActionArea, CardMedia, CardContent, Typography } from '@mui/material';

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

  return (
    <Grid container spacing={4}>
      {categories.map((category) => (
        <Grid item key={category.id} xs={12} sm={6} md={4}>
          <Link to={`/category/${category.id}`} style={{ textDecoration: 'none' }}>
            <Card>
              <CardActionArea>
                {category.illustration_image && (
                  <CardMedia
                    component="img"
                    alt={category.name}
                    height="140"
                    image={category.illustration_image.image}
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
