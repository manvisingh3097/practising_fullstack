import BookDetailPage from "./components/BookDetailPage";
import BookPage from "./components/BookPage";
import HomePage from "./components/HomePage";
import {BrowseRouter as Router , Routes , Route, BrowserRouter } from "react-router-dom"
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
          <Route path="/" element={ <HomePage/>} />
          <Route path="/books" element={ <BookPage/>} />
          <Route path="/books/detail" element={ <BookDetailPage/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;
