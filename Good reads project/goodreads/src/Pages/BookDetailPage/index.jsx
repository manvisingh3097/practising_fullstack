import React, {useEffect , useState} from "react";
import BookData from "../data/book";
import BookDetail from "./components/BookDetail";
import Navbar from "./components/Navbar";
// import { useParams } from "react-router-dom";

const BookDetailPage = () => {
    const [book, SetBook] = useState({});

    useEffect(()=> {
        SetBook(BookData[0]);
    });

    return(
        <>
        <Navbar/>
        <BookDetail data={book}/>
        </>
    );
};

export default BookDetailPage;
