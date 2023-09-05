import React, { useState, useEffect } from "react";
import BookData from "../../data/book";
import Book from "./Book";
import {useDispatch , useSelector} from "react-redux";
import { setBooks } from '../../redux/actions/book.action';

const BookList = () => {
  // const [books, setBooks] = useState([]);

  const books = useSelector(state => state.allbooks.books)
  const dispatch = useDispatch()

  useEffect(() => {
    // setBooks(BookData);
    dispatch(setBooks(BookData));
  }, []);

  return (
    <div className="container">
      <div className="text-center">All Books</div>
      <div className="row">
        {books.map((book, index) => (
          <Book data={book} key={index} />
        ))}
      </div>
    </div>
  );
};
export default BookList;
