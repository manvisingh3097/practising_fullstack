import React, {useEffect , useState} from "react";
import BookData from "../Data/Book";
import BookDetail from "./components/BookDetail";
import Navbar from "./components/Navbar";
// import { useParams } from "react-router-dom";

const BookDetailPage = () => {
    const [Book, SetBook] = useState({});

    useEffect(()=> {
        SetBook(BookData[0]);
    });

    return(
        <>
        <Navbar/>
        <BookDetail data={Book}/>
        </>
    );
};

export default BookDetailPage;
