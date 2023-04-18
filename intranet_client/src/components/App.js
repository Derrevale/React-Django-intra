import React, {useEffect, useState} from "react";
import Navbar from "./Navbar";
import Topbar from "./Topbar";


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
import Gallery from "./Galery/Galery";
import FileImports from "./Documents/FileImports";
import SearchResult from "./Search/SearchResult";
import CalendarEvent from "./Calendar/CalendarEvent";

function App() {

    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route path="/" element={<Root/>}>
                <Route index element={<ArticleList/>}/>
                <Route path="/calendrier/:id" element={<CalendarEvent/>}/>

                <Route path="/eventform" element={<AddEventForm/>}/>
                <Route path="/fileimport" element={<FileImports/>}/>
                <Route path="/search" element={<SearchResult/>}/>

                <Route path="/articlelist" element={<ArticleList/>}/>
                <Route path="/articles/:id" element={<Article/>}/>
                <Route path="/documents" element={<Documents/>}/>
                <Route path="/Galerie" element={<Gallery/>}/>
                <Route element={<Navbar/>}/>
            </Route>
        )
    );


    return (
        <div className="App">
            <Topbar/>
            <Navbar/>
            <RouterProvider router={router}/>
        </div>
    );
}

const Root = () => {
    return (
        <>

            <div className="container">
                <Outlet/>
            </div>
        </>
    )
}
export default App
