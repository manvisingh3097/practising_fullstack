import { ActionTypes } from "../constants/action-types";

export const setBooks = (books) => {
    return{
        type: ActionTypes.SET_BOOKS,
        payload: books
    }
}

export const addBook = (book) => {
    return{
        type: ActionTypes.ADD_BOOK,
        payload : book
    }
}

export const removeBook = () => {
    return{
        type: ActionTypes.REMOVE_BOOK,
        
    }
} 