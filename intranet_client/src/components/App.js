import React, {useEffect, useState} from "react";
import Navbar from "./Navbar";
import Events from "./Event";
import Topbar from "./Topbar";
import MyCalendar from "./Calendar";

import {createBrowserRouter, createRoutesFromElements, Route, Link, Outlet, RouterProvider, useParams} from "react-router-dom";
import Event from "./Event";
import ArticleList from "./ArticleList";
import Article from "./Article";

function App() {

    const router = createBrowserRouter(
        createRoutesFromElements(
            <Route path="/" element={<Root/>}>
                <Route index element={<ArticleList/>}/>
                <Route path="/events" element={<Events/>}/>
                <Route path="/calendar" element={<MyCalendar/>}/>
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

            <div>
                <Outlet/>
            </div>
        </>
    )
}
export default App
