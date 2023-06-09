import logo from './logo.svg';
import './App.css';
import { useEffect, useState} from 'react';


function fetchBitcoinPrice() {
  fetch('hhttps://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(data => {
      const bitcoinPrice = data.bpi.USD.rate;
      const bitcoinPriceElement = document.getElementById('bitcoin-price');
      
      if (bitcoinPriceElement) {
        bitcoinPriceElement.innerText = bitcoinPrice;
      } else {
        console.log('Element with ID "bitcoin-price" not found.');
      }
    })
    .catch(error => {
      console.log('An error occurred while fetching the Bitcoin price:', error);
    });
}


// function App() {

//   const [todos , setToDos] = useState([]);

//   useEffect (()=>{
//     fetch("https://jsonplaceholder.typicode.com/todos")
//     .then(res=> res.json())
//     .then(res=>{
//       console.log(res);
//       setToDos(res);
//     })
//   },[])

//   return (
//     <div className="App">
//      <table className="table table-dark">
//   <thead>
//     <tr>
//       <th scope="col">User ID</th>
//       <th scope="col">ID</th>
//       <th scope="col">title</th>
//       <th scope="col">Completed</th>
//     </tr>
//   </thead>
//   <tbody>
//     {
//       todos &&
//       todos.map(t=>
//     <tr>
//       <td>{t.userID}</td>
//       <td>{t.id}</td>
//       <td>{t.title}</td>
//       <td>{t.completed ? 'Yes' : 'No'}</td>
//     </tr>
//         )
//     }
//   </tbody>
// </table>
//     </div>
//   );
// }

export default fetchBitcoinPrice;
