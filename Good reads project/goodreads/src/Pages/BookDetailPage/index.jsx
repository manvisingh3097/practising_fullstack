import React, { useState, useEffect } from "react";
import BookData from "../../data/book";
import BookDetail from "../../components/BookDetail";
import Navbar from "../../components/Navbar";

const BookDetailPage = () => {
  const [book, setBook] = useState({});

  useEffect(() => {
    setBook(BookData[0]);
  });

  return (
    <>
      <Navbar />
      <BookDetail data={book} />
    </>
  );
};
export default BookDetailPage;
