import React, {useEffect, useState} from "react";
import Navbar from "./Navbar";
import Topbar from "./Topbar";
import MyCalendar from "./Calendar/Calendar";

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

function App() {

    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route path="/" element={<Root/>}>
                <Route index element={<ArticleList/>}/>
                <Route path="/calendar" element={<MyCalendar/>}/>
                <Route path="/eventform" element={<AddEventForm/>}/>
                <Route path="/articlelist" element={<ArticleList/>}/>
                <Route path="/articles/:id" element={<Article/>}/>
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
