import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import { Grid, Card, CardActionArea, CardMedia, CardContent, Typography, ImageList, ImageListItem } from '@mui/material';

const CategoryDetail = () => {
  const { categoryId } = useParams();
  const [category, setCategory] = useState(null);
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchCategory = async () => {
      try {
        const response = await axios.get(`http://localhost:8002/api/Galerie Categorie/${categoryId}/`);
        setCategory(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération de la catégorie:', error);
      }
    };

    const fetchImages = async () => {
      try {
        const response = await axios.get('http://localhost:8002/api/Galerie Image/');
        setImages(response.data);
      } catch (error) {
        console.error('Erreur lors de la récupération des images:', error);
      }
    };

    fetchCategory();
    fetchImages();
  }, [categoryId]);

  if (!category) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Typography variant="h4" component="h2" gutterBottom>
        {category.name}
      </Typography>
      <Grid container spacing={4}>
        {category.subcategories.map((subcategoryId) => {
          const subcategory = category.subcategories.find((cat) => cat.id === subcategoryId);
          return (
            <Grid item key={subcategory.id} xs={12} sm={6} md={4}>
              <Link to={`/category/${subcategory.id}`} style={{ textDecoration: 'none' }}>
                <Card>
                  <CardActionArea>
                    {subcategory.illustration_image && (
                      <CardMedia
                        component="img"
                        alt={subcategory.name}
                        height="140"
                        image={subcategory.illustration_image.image}
                      />
                    )}
                    <CardContent>
                      <Typography gutterBottom variant="h5" component="div">
                        {subcategory.name}
                      </Typography>
                    </CardContent>
                  </CardActionArea>
                </Card>
              </Link>
            </Grid>
          );
        })}
      </Grid>
      <Typography variant="h5" component="h3" gutterBottom>
        Images
      </Typography>
      <ImageList cols={3} gap={8}>
        {category.images.map((imageId) => {
          const image = images.find((img) => img.id === imageId);
          return (
            image && (
              <ImageListItem key={image.id}>
                <img src={image.image} alt={image.id} loading="lazy" />
              </ImageListItem>
            )
          );
        })}
      </ImageList>
    </div>
  );
};

export default CategoryDetail;
