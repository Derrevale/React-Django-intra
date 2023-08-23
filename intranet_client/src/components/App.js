import React, {useEffect, useState} from "react";
import Navbar from "./Navigation/Navbar";
import Topbar from "./Navigation/Topbar";
import { Button } from 'react-bootstrap';
import OffcanvasRight from './Navigation/OffcanvasRight';

import {
    createBrowserRouter,
    createRoutesFromElements,
    Route,
    Link,
    Outlet,
    RouterProvider,
    useParams
} from "react-router-dom";
import ArticleList from "./Blog/ArticleList";
import Article from "./Blog/Article";

import AddEventForm from "./Formulaire/EventForm";
import Documents from "./Documents/Documents";
import FileImports from "./Documents/FileImports";

import SearchResult from "./Search/SearchResult";

import CalendarEvent from "./Calendar/CalendarEvent";

import CategoryList from "./Galery/CategoryList";
import CategoryDetail from "./Galery/CategoryDetail";

import Login from "./Authentication/Login";

function App() {

    const [showOffcanvas, setShowOffcanvas] = useState(false);

    const handleClose = () => setShowOffcanvas(false);
    const handleShow = () => setShowOffcanvas(true);

    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route path="/" element={<Root handleShow={handleShow}/>}>
                <Route index element={<ArticleList/>}/>
                <Route path="/calendrier/:id" element={<CalendarEvent/>}/>

                <Route path="/login" element={<Login/>}/>
                <Route path="/eventform" element={<AddEventForm/>}/>
                <Route path="/fileimport" element={<FileImports/>}/>
                <Route path="/search" element={<SearchResult/>}/>

                <Route path="/articlelist" element={<ArticleList/>}/>
                <Route path="/articles/:id" element={<Article/>}/>

                <Route path="/documents" element={<Documents/>}/>

                <Route path="/Galerie" element={<CategoryList/>}/>
                <Route path="/Galerie/:categoryId" element={<CategoryDetail/>}/>
            </Route>
        )
    );


    return (
        <div className="App">
            <Topbar/>

            <OffcanvasRight show={showOffcanvas} handleClose={handleClose} />

            <RouterProvider router={router}/>
        </div>
    );
}

const Root = ({handleShow}) => {
    return (
        <>
            <Navbar handleShow={handleShow}/>
            <div className="container">
                <Outlet/>
            </div>
        </>
    )
}
export default App
