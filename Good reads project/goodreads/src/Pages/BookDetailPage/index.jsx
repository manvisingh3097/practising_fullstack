import React, {useEffect , useState} from "react";
import BookData from "../Data/book";
import BookDetail from "./components/BookDetail";
import Navbar from "./components/Navbar";
import { useParams } from "react-router-dom";

const BookDetailPage = () => {
    const {id} = useParams()
    const [Book, SetBook] = useState({});

    useEffect(()=> {
        SetBook(BookData[id]);
    })

    return(
        <>
        <Navbar/>
        <BookDetail data={Book}/>
        </>
    );
};

export default BookDetailPage;
